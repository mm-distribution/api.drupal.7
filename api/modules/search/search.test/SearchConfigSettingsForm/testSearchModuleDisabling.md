# SearchConfigSettingsForm::testSearchModuleDisabling()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1527–1611 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1527-L1611)
- **Class:** [SearchConfigSettingsForm](../SearchConfigSettingsForm.md)
- **Module/theme:** search

## Signature

```php
function testSearchModuleDisabling()
```

## Documentation

```text
Verify that you can disable individual search modules.
```

## Code

```php
  function testSearchModuleDisabling() {
    // Array of search modules to test: 'path' is the search path, 'title' is
    // the tab title, 'keys' are the keywords to search for, and 'text' is
    // the text to assert is on the results page.
    $module_info = array(
      'node' => array(
        'path' => 'node',
        'title' => 'Content',
        'keys' => 'pizza',
        'text' => $this->search_node->title,
      ),
      'user' => array(
        'path' => 'user',
        'title' => 'User',
        'keys' => $this->search_user->name,
        'text' => $this->search_user->mail,
      ),
      'search_extra_type' => array(
        'path' => 'dummy_path',
        'title' => 'Dummy search type',
        'keys' => 'foo',
        'text' => 'Dummy search snippet to display',
      ),
    );
    $modules = array_keys($module_info);

    // Test each module if it's enabled as the only search module.
    foreach ($modules as $module) {
      // Enable the one module and disable other ones.
      $info = $module_info[$module];
      $edit = array();
      foreach ($modules as $other) {
        $edit['search_active_modules[' . $other . ']'] = (($other == $module) ? $module : FALSE);
      }
      $edit['search_default_module'] = $module;
      $this->drupalPost('admin/config/search/settings', $edit, t('Save configuration'));

      // Run a search from the correct search URL.
      $this->drupalGet('search/' . $info['path'] . '/' . $info['keys']);
      $this->assertNoText('no results', $info['title'] . ' search found results');
      $this->assertText($info['text'], 'Correct search text found');

      // Verify that other module search tab titles are not visible.
      foreach ($modules as $other) {
        if ($other != $module) {
          $title = $module_info[$other]['title'];
          $this->assertNoText($title, $title . ' search tab is not shown');
        }
      }

      // Run a search from the search block on the node page. Verify you get
      // to this module's search results page.
      $terms = array('search_block_form' => $info['keys']);
      $this->drupalPost('node', $terms, t('Search'));
      $this->assertEqual(
        $this->getURL(),
        url('search/' . $info['path'] . '/' . $info['keys'], array('absolute' => TRUE)),
        'Block redirected to right search page');

      // Try an invalid search path. Should redirect to our active module.
      $this->drupalGet('search/not_a_module_path');
      $this->assertEqual(
        $this->getURL(),
        url('search/' . $info['path'], array('absolute' => TRUE)),
        'Invalid search path redirected to default search page');
    }

    // Test with all search modules enabled. When you go to the search
    // page or run search, all modules should be shown.
    $edit = array();
    foreach ($modules as $module) {
      $edit['search_active_modules[' . $module . ']'] = $module;
    }
    $edit['search_default_module'] = 'node';

    $this->drupalPost('admin/config/search/settings', $edit, t('Save configuration'));

    foreach (array('search/node/pizza', 'search/node') as $path) {
      $this->drupalGet($path);
      foreach ($modules as $module) {
        $title = $module_info[$module]['title'];
        $this->assertText($title, format_string('%title search tab is shown', array('%title' => $title)));
      }
    }
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
