# LocaleContentFunctionalTest::testContentTypeLanguageConfiguration()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2194–2292 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2194-L2292)
- **Class:** [LocaleContentFunctionalTest](../LocaleContentFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testContentTypeLanguageConfiguration()
```

## Documentation

```text
Test if a content type can be set to multilingual and language setting is
present on node add and edit forms.
```

## Code

```php
  function testContentTypeLanguageConfiguration() {
    global $base_url;

    // User to add and remove language.
    $admin_user = $this->drupalCreateUser(array('administer languages', 'administer content types', 'access administration pages'));
    // User to create a node.
    $web_user = $this->drupalCreateUser(array('create article content', 'create page content', 'edit any page content'));

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

    // Add disabled custom language.
    // Code for the language.
    $langcode_disabled = 'xx-yy';
    // The English name for the language.
    $name_disabled = $this->randomName(16);
    // The native name for the language.
    $native_disabled = $this->randomName(16);
    // The domain prefix.
    $prefix_disabled = $langcode_disabled;
    $edit = array(
      'langcode' => $langcode_disabled,
      'name' => $name_disabled,
      'native' => $native_disabled,
      'prefix' => $prefix_disabled,
      'direction' => '0',
    );
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add custom language'));
    // Disable second custom language.
    $path = 'admin/config/regional/language';
    $edit = array(
      'enabled[' . $langcode_disabled . ']' => FALSE,
    );
    $this->drupalPost($path, $edit, t('Save configuration'));

    // Set "Basic page" content type to use multilingual support.
    $this->drupalGet('admin/structure/types/manage/page');
    $this->assertText(t('Multilingual support'), 'Multilingual support fieldset present on content type configuration form.');
    $edit = array(
      'language_content_type' => 1,
    );
    $this->drupalPost('admin/structure/types/manage/page', $edit, t('Save content type'));
    $this->assertRaw(t('The content type %type has been updated.', array('%type' => 'Basic page')), 'Basic page content type has been updated.');
    $this->drupalLogout();

    // Verify language selection is not present on add article form.
    $this->drupalLogin($web_user);
    $this->drupalGet('node/add/article');
    // Verify language select list is not present.
    $this->assertNoFieldByName('language', NULL, 'Language select not present on add article form.');

    // Verify language selection appears on add "Basic page" form.
    $this->drupalGet('node/add/page');
    // Verify language select list is present.
    $this->assertFieldByName('language', NULL, 'Language select present on add Basic page form.');
    // Ensure enabled language appears.
    $this->assertText($name, 'Enabled language present.');
    // Ensure disabled language doesn't appear.
    $this->assertNoText($name_disabled, 'Disabled language not present.');

    // Create "Basic page" content.
    $node_title = $this->randomName();
    $node_body =  $this->randomName();
    $edit = array(
      'type' => 'page',
      'title' => $node_title,
      'body' => array($langcode => array(array('value' => $node_body))),
      'language' => $langcode,
    );
    $node = $this->drupalCreateNode($edit);
    // Edit the content and ensure correct language is selected.
    $path = 'node/' . $node->nid . '/edit';
    $this->drupalGet($path);
    $this->assertRaw('<option value="' . $langcode . '" selected="selected">' .  $name . '</option>', 'Correct language selected.');
    // Ensure we can change the node language.
    $edit = array(
      'language' => 'en',
    );
    $this->drupalPost($path, $edit, t('Save'));
    $this->assertRaw(t('%title has been updated.', array('%title' => $node_title)), 'Basic page content updated.');

    $this->drupalLogout();
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
