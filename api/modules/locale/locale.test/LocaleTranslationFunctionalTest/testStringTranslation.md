# LocaleTranslationFunctionalTest::testStringTranslation()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 342–474 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L342-L474)
- **Class:** [LocaleTranslationFunctionalTest](../LocaleTranslationFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testStringTranslation()
```

## Documentation

```text
Adds a language and tests string translation by users with the appropriate permissions.
```

## Code

```php
  function testStringTranslation() {
    global $base_url;

    // User to add and remove language.
    $admin_user = $this->drupalCreateUser(array('administer languages', 'access administration pages'));
    // User to translate and delete string.
    $translate_user = $this->drupalCreateUser(array('translate interface', 'access administration pages'));
    // Code for the language.
    $langcode = 'xx';
    // The English name for the language. This will be translated.
    $name = $this->randomName(16);
    // The native name for the language.
    $native = $this->randomName(16);
    // The domain prefix.
    $prefix = $langcode;
    // This is the language indicator on the translation search screen for
    // untranslated strings. Copied straight from locale.inc.
    $language_indicator = "<em class=\"locale-untranslated\">$langcode</em> ";
    // This will be the translation of $name.
    $translation = $this->randomName(16);

    // Add custom language.
    $this->drupalLogin($admin_user);
    $edit = array(
      'langcode' => $langcode,
      'name' => $name,
      'native' => $native,
      'prefix' => $prefix,
      'direction' => '0',
    );
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add custom language'));
    // Add string.
    t($name, array(), array('langcode' => $langcode));
    // Reset locale cache.
    locale_reset();
    $this->assertText($langcode, 'Language code found.');
    $this->assertText($name, 'Name found.');
    $this->assertText($native, 'Native found.');
    // No t() here, we do not want to add this string to the database and it's
    // surely not translated yet.
    $this->assertText($native, 'Test language added.');
    $this->drupalLogout();

    // Search for the name and translate it.
    $this->drupalLogin($translate_user);
    $search = array(
      'string' => $name,
      'language' => 'all',
      'translation' => 'all',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    // assertText() seems to remove the input field where $name always could be
    // found, so this is not a false assert. See how assertNoText succeeds
    // later.
    $this->assertText($name, 'Search found the name.');
    $this->assertRaw($language_indicator, 'Name is untranslated.');
    // Assume this is the only result, given the random name.
    $this->clickLink(t('edit'));
    // We save the lid from the path.
    $matches = array();
    preg_match('!admin/config/regional/translate/edit/(\d+)!', $this->getUrl(), $matches);
    $lid = $matches[1];
    // No t() here, it's surely not translated yet.
    $this->assertText($name, 'name found on edit screen.');
    $edit = array(
      "translations[$langcode]" => $translation,
    );
    $this->drupalPost(NULL, $edit, t('Save translations'));
    $this->assertText(t('The string has been saved.'), 'The string has been saved.');
    $this->assertEqual($this->getUrl(), url('admin/config/regional/translate/translate', array('absolute' => TRUE)), 'Correct page redirection.');
    $this->assertTrue($name != $translation && t($name, array(), array('langcode' => $langcode)) == $translation, 't() works.');
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    // The indicator should not be here.
    $this->assertNoRaw($language_indicator, 'String is translated.');

    // Verify that a translation set which has an empty target string can be
    // updated without any database error.
    db_update('locales_target')
      ->fields(array('translation' => ''))
      ->condition('language', $langcode, '=')
      ->condition('lid', $lid, '=')
      ->execute();
    $this->drupalPost('admin/config/regional/translate/edit/' . $lid, $edit, t('Save translations'));
    $this->assertText(t('The string has been saved.'), 'The string has been saved.');

    // Try to edit a non-existent string and ensure we're redirected correctly.
    // Assuming we don't have 999,999 strings already.
    $random_lid = 999999;
    $this->drupalGet('admin/config/regional/translate/edit/' . $random_lid);
    $this->assertText(t('String not found'), 'String not found.');
    $this->assertEqual($this->getUrl(), url('admin/config/regional/translate/translate', array('absolute' => TRUE)), 'Correct page redirection.');
    $this->drupalLogout();

    // Delete the language.
    $this->drupalLogin($admin_user);
    $path = 'admin/config/regional/language/delete/' . $langcode;
    // This a confirm form, we do not need any fields changed.
    $this->drupalPost($path, array(), t('Delete'));
    // We need raw here because %locale will add HTML.
    $this->assertRaw(t('The language %locale has been removed.', array('%locale' => $name)), 'The test language has been removed.');
    // Reload to remove $name.
    $this->drupalGet($path);
    // Verify that language is no longer found.
    $this->assertResponse(404, 'Language no longer found.');
    $this->drupalLogout();

    // Delete the string.
    $this->drupalLogin($translate_user);
    $search = array(
      'string' => $name,
      'language' => 'all',
      'translation' => 'all',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    // Assume this is the only result, given the random name.
    $this->clickLink(t('delete'));
    $this->assertText(t('Are you sure you want to delete the string'), '"delete" link is correct.');
    // Delete the string.
    $path = 'admin/config/regional/translate/delete/' . $lid;
    $this->drupalGet($path);
    // First test the 'cancel' link.
    $this->clickLink(t('Cancel'));
    $this->assertEqual($this->getUrl(), url('admin/config/regional/translate/translate', array('absolute' => TRUE)), 'Correct page redirection.');
    $this->assertRaw($name, 'The string was not deleted.');
    // Delete the name string.
    $this->drupalPost('admin/config/regional/translate/delete/' . $lid, array(), t('Delete'));
    $this->assertText(t('The string has been removed.'), 'The string has been removed message.');
    $this->assertEqual($this->getUrl(), url('admin/config/regional/translate/translate', array('absolute' => TRUE)), 'Correct page redirection.');
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    $this->assertNoText($name, 'Search now can not find the name.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
