# LocaleImportFunctionalTest::testStandalonePoFile()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 939–1051 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L939-L1051)
- **Class:** [LocaleImportFunctionalTest](../LocaleImportFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testStandalonePoFile()
```

## Documentation

```text
Test import of standalone .po files.
```

## Code

```php
  function testStandalonePoFile() {
    // Try importing a .po file.
    $this->importPoFile($this->getPoFile(), array(
      'langcode' => 'fr',
    ));

    // The import should automatically create the corresponding language.
    $this->assertRaw(t('The language %language has been created.', array('%language' => 'French')), 'The language has been automatically created.');

    // The import should have created 7 strings.
    $this->assertRaw(t('The translation was successfully imported. There are %number newly created translated strings, %update strings were updated and %delete strings were removed.', array('%number' => 9, '%update' => 0, '%delete' => 0)), 'The translation file was successfully imported.');

    // This import should have saved plural forms to have 2 variants.
    $this->assert(db_query("SELECT plurals FROM {languages} WHERE language = 'fr'")->fetchField() == 2, 'Plural number initialized.');

    // Ensure we were redirected correctly.
    $this->assertEqual($this->getUrl(), url('admin/config/regional/translate', array('absolute' => TRUE)), 'Correct page redirection.');


    // Try importing a .po file with invalid tags in the default text group.
    $this->importPoFile($this->getBadPoFile(), array(
      'langcode' => 'fr',
    ));

    // The import should have created 1 string and rejected 2.
    $this->assertRaw(t('The translation was successfully imported. There are %number newly created translated strings, %update strings were updated and %delete strings were removed.', array('%number' => 1, '%update' => 0, '%delete' => 0)), 'The translation file was successfully imported.');
    $skip_message = format_plural(2, 'One translation string was skipped because it contains disallowed HTML.', '@count translation strings were skipped because they contain disallowed HTML.');
    $this->assertRaw($skip_message, 'Unsafe strings were skipped.');


    // Try importing a .po file with invalid tags in a non default text group.
    $this->importPoFile($this->getBadPoFile(), array(
      'langcode' => 'fr',
      'group' => 'custom',
    ));

    // The import should have created 3 strings.
    $this->assertRaw(t('The translation was successfully imported. There are %number newly created translated strings, %update strings were updated and %delete strings were removed.', array('%number' => 3, '%update' => 0, '%delete' => 0)), 'The translation file was successfully imported.');


    // Try importing a .po file which doesn't exist.
    $name = $this->randomName(16);
    $this->drupalPost('admin/config/regional/translate/import', array(
      'langcode' => 'fr',
      'files[file]' => $name,
      'group' => 'custom',
    ), t('Import'));
    $this->assertEqual($this->getUrl(), url('admin/config/regional/translate/import', array('absolute' => TRUE)), 'Correct page redirection.');
    $this->assertText(t('File to import not found.'), 'File to import not found message.');


    // Try importing a .po file with overriding strings, and ensure existing
    // strings are kept.
    $this->importPoFile($this->getOverwritePoFile(), array(
      'langcode' => 'fr',
      'mode' => 1, // Existing strings are kept, only new strings are added.
    ));

    // The import should have created 1 string.
    $this->assertRaw(t('The translation was successfully imported. There are %number newly created translated strings, %update strings were updated and %delete strings were removed.', array('%number' => 1, '%update' => 0, '%delete' => 0)), 'The translation file was successfully imported.');
    // Ensure string wasn't overwritten.
    $search = array(
      'string' => 'Montag',
      'language' => 'fr',
      'translation' => 'translated',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    $this->assertText(t('No strings available.'), 'String not overwritten by imported string.');

    // This import should not have changed number of plural forms.
    $this->assert(db_query("SELECT plurals FROM {languages} WHERE language = 'fr'")->fetchField() == 2, 'Plural numbers untouched.');

    $this->importPoFile($this->getPoFileWithBrokenPlural(), array(
      'langcode' => 'fr',
      'mode' => 1, // Existing strings are kept, only new strings are added.
    ));

    // Attempt to import broken .po file as well to prove that this
    // will not overwrite the proper plural formula imported above.
    $this->assert(db_query("SELECT plurals FROM {languages} WHERE language = 'fr'")->fetchField() == 2, 'Broken plurals: plural numbers untouched.');

    $this->importPoFile($this->getPoFileWithMissingPlural(), array(
      'langcode' => 'fr',
      'mode' => 1, // Existing strings are kept, only new strings are added.
    ));

    // Attempt to import .po file which has no plurals and prove that this
    // will not overwrite the proper plural formula imported above.
    $this->assert(db_query("SELECT plurals FROM {languages} WHERE language = 'fr'")->fetchField() == 2, 'No plurals: plural numbers untouched.');


    // Try importing a .po file with overriding strings, and ensure existing
    // strings are overwritten.
    $this->importPoFile($this->getOverwritePoFile(), array(
      'langcode' => 'fr',
      'mode' => 0, // Strings in the uploaded file replace existing ones, new ones are added.
    ));

    // The import should have updated 2 strings.
    $this->assertRaw(t('The translation was successfully imported. There are %number newly created translated strings, %update strings were updated and %delete strings were removed.', array('%number' => 0, '%update' => 2, '%delete' => 0)), 'The translation file was successfully imported.');
    // Ensure string was overwritten.
    $search = array(
      'string' => 'Montag',
      'language' => 'fr',
      'translation' => 'translated',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    $this->assertNoText(t('No strings available.'), 'String overwritten by imported string.');
    // This import should have changed number of plural forms.
    $this->assert(db_query("SELECT plurals FROM {languages} WHERE language = 'fr'")->fetchField() == 3, 'Plural numbers changed.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
