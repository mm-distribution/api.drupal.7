# LocaleConfigurationTest::testLanguageConfiguration()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 43–178 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L43-L178)
- **Class:** [LocaleConfigurationTest](../LocaleConfigurationTest.md)
- **Module/theme:** locale

## Signature

```php
function testLanguageConfiguration()
```

## Documentation

```text
Functional tests for adding, editing and deleting languages.
```

## Code

```php
  function testLanguageConfiguration() {
    global $base_url;

    // User to add and remove language.
    $admin_user = $this->drupalCreateUser(array('administer languages', 'access administration pages'));
    $this->drupalLogin($admin_user);

    // Add predefined language.
    $edit = array(
      'langcode' => 'fr',
    );
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add language'));
    $this->assertText('fr', 'Language added successfully.');
    $this->assertEqual($this->getUrl(), url('admin/config/regional/language', array('absolute' => TRUE)), 'Correct page redirection.');

    // Add custom language.
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
    $this->assertEqual($this->getUrl(), url('admin/config/regional/language', array('absolute' => TRUE)), 'Correct page redirection.');
    $this->assertText($langcode, 'Language code found.');
    $this->assertText($name, 'Name found.');
    $this->assertText($native, 'Native found.');
    $this->assertText($native, 'Test language added.');

    // Check if we can change the default language.
    $path = 'admin/config/regional/language';
    $this->drupalGet($path);
    $this->assertFieldChecked('edit-site-default-en', 'English is the default language.');
    // Change the default language.
    $edit = array(
      'site_default' => $langcode,
    );
    $this->drupalPost(NULL, $edit, t('Save configuration'));
    $this->assertNoFieldChecked('edit-site-default-en', 'Default language updated.');
    $this->assertEqual($this->getUrl(), url('admin/config/regional/language', array('absolute' => TRUE)), 'Correct page redirection.');

    // Check if a valid language prefix is added after changing the default
    // language.
    $this->drupalGet('admin/config/regional/language/edit/en');
    $this->assertFieldByXPath('//input[@name="prefix"]', 'en', 'A valid path prefix has been added to the previous default language.');

    // Ensure we can't delete the default language.
    $this->drupalGet('admin/config/regional/language/delete/' . $langcode);
    $this->assertEqual($this->getUrl(), url('admin/config/regional/language', array('absolute' => TRUE)), 'Correct page redirection.');
    $this->assertText(t('The default language cannot be deleted.'), 'Failed to delete the default language.');

    // Check if we can disable a language.
    $edit = array(
      'enabled[en]' => FALSE,
    );
    $this->drupalPost($path, $edit, t('Save configuration'));
    $this->assertNoFieldChecked('edit-enabled-en', 'Language disabled.');

    // Set disabled language to be the default and ensure it is re-enabled.
    $edit = array(
      'site_default' => 'en',
    );
    $this->drupalPost(NULL, $edit, t('Save configuration'));
    $this->assertFieldChecked('edit-enabled-en', 'Default language re-enabled.');

    // Ensure 'edit' link works.
    $this->clickLink(t('edit'));
    $this->assertTitle(t('Edit language | Drupal'), 'Page title is "Edit language".');
    // Edit a language.
    $name = $this->randomName(16);
    $edit = array(
      'name' => $name,
    );
    $this->drupalPost('admin/config/regional/language/edit/' . $langcode, $edit, t('Save language'));
    $this->assertRaw($name, 'The language has been updated.');
    $this->assertEqual($this->getUrl(), url('admin/config/regional/language', array('absolute' => TRUE)), 'Correct page redirection.');

    // Ensure 'delete' link works.
    $this->drupalGet('admin/config/regional/language');
    $this->clickLink(t('delete'));
    $this->assertText(t('Are you sure you want to delete the language'), '"delete" link is correct.');
    // Delete an enabled language.
    $this->drupalGet('admin/config/regional/language/delete/' . $langcode);
    // First test the 'cancel' link.
    $this->clickLink(t('Cancel'));
    $this->assertEqual($this->getUrl(), url('admin/config/regional/language', array('absolute' => TRUE)), 'Correct page redirection.');
    $this->assertRaw($name, 'The language was not deleted.');
    // Delete the language for real. This a confirm form, we do not need any
    // fields changed.
    $this->drupalPost('admin/config/regional/language/delete/' . $langcode, array(), t('Delete'));
    // We need raw here because %locale will add HTML.
    $this->assertRaw(t('The language %locale has been removed.', array('%locale' => $name)), 'The test language has been removed.');
    $this->assertEqual($this->getUrl(), url('admin/config/regional/language', array('absolute' => TRUE)), 'Correct page redirection.');
    // Verify that language is no longer found.
    $this->drupalGet('admin/config/regional/language/delete/' . $langcode);
    $this->assertResponse(404, 'Language no longer found.');
    // Make sure the "language_count" variable has been updated correctly.
    drupal_static_reset('language_list');
    $enabled = language_list('enabled');
    $this->assertEqual(variable_get('language_count', 1), count($enabled[1]), 'Language count is correct.');
    // Delete a disabled language.
    // Disable an enabled language.
    $edit = array(
      'enabled[fr]' => FALSE,
    );
    $this->drupalPost($path, $edit, t('Save configuration'));
    $this->assertNoFieldChecked('edit-enabled-fr', 'French language disabled.');
    // Get the count of enabled languages.
    drupal_static_reset('language_list');
    $enabled = language_list('enabled');
    // Delete the disabled language.
    $this->drupalPost('admin/config/regional/language/delete/fr', array(), t('Delete'));
    // We need raw here because %locale will add HTML.
    $this->assertRaw(t('The language %locale has been removed.', array('%locale' => 'French')), 'Disabled language has been removed.');
    $this->assertEqual($this->getUrl(), url('admin/config/regional/language', array('absolute' => TRUE)), 'Correct page redirection.');
    // Verify that language is no longer found.
    $this->drupalGet('admin/config/regional/language/delete/fr');
    $this->assertResponse(404, 'Language no longer found.');
    // Make sure the "language_count" variable has not changed.
    $this->assertEqual(variable_get('language_count', 1), count($enabled[1]), 'Language count is correct.');


    // Ensure we can't delete the English language.
    $this->drupalGet('admin/config/regional/language/delete/en');
    $this->assertEqual($this->getUrl(), url('admin/config/regional/language', array('absolute' => TRUE)), 'Correct page redirection.');
    $this->assertText(t('The English language cannot be deleted.'), 'Failed to delete English language.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
