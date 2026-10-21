# LocaleImportFunctionalTest::testAutomaticModuleTranslationImportLanguageEnable()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1057–1090 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1057-L1090)
- **Class:** [LocaleImportFunctionalTest](../LocaleImportFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testAutomaticModuleTranslationImportLanguageEnable()
```

## Documentation

```text
Test automatic import of a module's translation files when a language is
enabled.
```

## Code

```php
  function testAutomaticModuleTranslationImportLanguageEnable() {
    // Code for the language - manually set to match the test translation file.
    $langcode = 'xx';
    // The English name for the language.
    $name = $this->randomName(16);
    // The native name for the language.
    $native = $this->randomName(16);
    // The domain prefix.
    $prefix = $langcode;

    // Create a custom language.
    $edit = array(
      'langcode' => $langcode,
      'name' => $name,
      'native' => $native,
      'prefix' => $prefix,
      'direction' => '0',
    );
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add custom language'));

    // Ensure the translation file was automatically imported when language was
    // added.
    $this->assertText(t('One translation file imported for the enabled modules.'), 'Language file automatically imported.');

    // Ensure strings were successfully imported.
    $search = array(
      'string' => 'lundi',
      'language' => $langcode,
      'translation' => 'translated',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    $this->assertNoText(t('No strings available.'), 'String successfully imported.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
