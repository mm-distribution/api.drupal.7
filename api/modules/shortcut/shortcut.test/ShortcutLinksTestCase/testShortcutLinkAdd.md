# ShortcutLinksTestCase::testShortcutLinkAdd()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 115–149 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L115-L149)
- **Class:** [ShortcutLinksTestCase](../ShortcutLinksTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testShortcutLinkAdd()
```

## Documentation

```text
Tests that creating a shortcut works properly.
```

## Code

```php
  function testShortcutLinkAdd() {
    $set = $this->set;

    // Create an alias for the node so we can test aliases.
    $path = array(
      'source' => 'node/' . $this->node->nid,
      'alias' => $this->randomName(8),
    );
    path_save($path);

    // Create some paths to test.
    $test_cases = array(
      array('path' => ''),
      array('path' => 'admin'),
      array('path' => 'admin/config/system/site-information'),
      array('path' => "node/{$this->node->nid}/edit"),
      array('path' => $path['alias']),
    );

    // Check that each new shortcut links where it should.
    foreach ($test_cases as $test) {
      $title = $this->randomName(10);
      $form_data = array(
        'shortcut_link[link_title]' => $title,
        'shortcut_link[link_path]'  => $test['path'],
      );
      $this->drupalPost('admin/config/user-interface/shortcut/' . $set->set_name . '/add-link', $form_data, t('Save'));
      $this->assertResponse(200);
      $saved_set = shortcut_set_load($set->set_name);
      $paths = $this->getShortcutInformation($saved_set, 'link_path');
      $test_path = empty($test['path']) ? '<front>' : $test['path'];
      $this->assertTrue(in_array(drupal_get_normal_path($test_path), $paths), 'Shortcut created: '. $test['path']);
      $this->assertLink($title, 0, 'Shortcut link found on the page.');
    }
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
