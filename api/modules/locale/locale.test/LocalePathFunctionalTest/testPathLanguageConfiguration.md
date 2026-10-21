# LocalePathFunctionalTest::testPathLanguageConfiguration()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2026–2143 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2026-L2143)
- **Class:** [LocalePathFunctionalTest](../LocalePathFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testPathLanguageConfiguration()
```

## Documentation

```text
Test if a language can be associated with a path alias.
```

## Code

```php
  function testPathLanguageConfiguration() {
    global $base_url;

    // User to add and remove language.
    $admin_user = $this->drupalCreateUser(array('administer languages', 'create page content', 'administer url aliases', 'create url aliases', 'access administration pages'));

    // Add custom language.
    $this->drupalLogin($admin_user);
    // Code for the language.
    $langcode = 'xx';
    // The English name for the language.
    $name = $this->randomName(16);
    // The native name for the language.
    $native = $this->randomName(16);
    // The domain prefix.
    $prefix = $langcode;
    $edit = array(
      'langcode' => $langcode,
      'name' => $name,
      'native' => $native,
      'prefix' => $prefix,
      'direction' => '0',
    );
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add custom language'));

    // Check that the "xx" front page is not available when path prefixes are
    // not enabled yet.
    $this->drupalPost('admin/config/regional/language/configure', array(), t('Save settings'));
    $this->drupalGet($prefix);
    $this->assertResponse(404, 'The "xx" front page is not available yet.');

    // Enable URL language detection and selection.
    $edit = array('language[enabled][locale-url]' => 1);
    $this->drupalPost('admin/config/regional/language/configure', $edit, t('Save settings'));

    // Create a node.
    $node = $this->drupalCreateNode(array('type' => 'page'));

    // Create a path alias in default language (English).
    $path = 'admin/config/search/path/add';
    $english_path = $this->randomName(8);
    $edit = array(
      'source'   => 'node/' . $node->nid,
      'alias'    => $english_path,
      'language' => 'en',
    );
    $this->drupalPost($path, $edit, t('Save'));

    // Create a path alias in new custom language.
    $custom_language_path = $this->randomName(8);
    $edit = array(
      'source'   => 'node/' . $node->nid,
      'alias'    => $custom_language_path,
      'language' => $langcode,
    );
    $this->drupalPost($path, $edit, t('Save'));

    // Confirm English language path alias works.
    $this->drupalGet($english_path);
    $this->assertText($node->title, 'English alias works.');

    // Confirm custom language path alias works.
    $this->drupalGet($prefix . '/' . $custom_language_path);
    $this->assertText($node->title, 'Custom language alias works.');

    // Create a custom path.
    $custom_path = $this->randomName(8);

    // Check priority of language for alias by source path.
    $edit = array(
      'source'   => 'node/' . $node->nid,
      'alias'    => $custom_path,
      'language' => LANGUAGE_NONE,
    );
    path_save($edit);
    $lookup_path = drupal_lookup_path('alias', 'node/' . $node->nid, 'en');
    $this->assertEqual($english_path, $lookup_path, 'English language alias has priority.');
    // Same check for language 'xx'.
    $lookup_path = drupal_lookup_path('alias', 'node/' . $node->nid, $prefix);
    $this->assertEqual($custom_language_path, $lookup_path, 'Custom language alias has priority.');
    path_delete($edit);

    // Create language nodes to check priority of aliases.
    $first_node = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1));
    $second_node = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1));

    // Assign a custom path alias to the first node with the English language.
    $edit = array(
      'source'   => 'node/' . $first_node->nid,
      'alias'    => $custom_path,
      'language' => 'en',
    );
    path_save($edit);

    // Assign a custom path alias to second node with LANGUAGE_NONE.
    $edit = array(
      'source'   => 'node/' . $second_node->nid,
      'alias'    => $custom_path,
      'language' => LANGUAGE_NONE,
    );
    path_save($edit);

    // Test that both node titles link to our path alias.
    $this->drupalGet('<front>');
    $custom_path_url = base_path() . (variable_get('clean_url', 0) ? $custom_path : '?q=' . $custom_path);
    $elements = $this->xpath('//a[@href=:href and .=:title]', array(':href' => $custom_path_url, ':title' => $first_node->title));
    $this->assertTrue(!empty($elements), 'First node links to the path alias.');
    $elements = $this->xpath('//a[@href=:href and .=:title]', array(':href' => $custom_path_url, ':title' => $second_node->title));
    $this->assertTrue(!empty($elements), 'Second node links to the path alias.');

    // Confirm that the custom path leads to the first node.
    $this->drupalGet($custom_path);
    $this->assertText($first_node->title, 'Custom alias returns first node.');

    // Confirm that the custom path with prefix leads to the second node.
    $this->drupalGet($prefix . '/' . $custom_path);
    $this->assertText($second_node->title, 'Custom alias with prefix returns second node.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
