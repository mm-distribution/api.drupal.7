# LocaleImportFunctionalTest

- **Type:** Class
- **File:** [`modules/locale/locale.test`](_file.md), lines 915–1346 · [local source](../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L915-L1346)
- **Module/theme:** locale

## Signature

```php
class LocaleImportFunctionalTest extends DrupalWebTestCase
```

## Documentation

```text
Functional tests for the import of translation files.
```

## Properties

### $admin_user

```php
protected $admin_user = NULL;
```

```text
A user able to create languages and import translations.
```

## Methods (derived index)

- [getInfo()](LocaleImportFunctionalTest/getInfo.md)
- [setUp()](LocaleImportFunctionalTest/setUp.md)
- [testStandalonePoFile()](LocaleImportFunctionalTest/testStandalonePoFile.md) — Test import of standalone .po files.
- [testAutomaticModuleTranslationImportLanguageEnable()](LocaleImportFunctionalTest/testAutomaticModuleTranslationImportLanguageEnable.md) — Test automatic import of a module's translation files when a language is enabled.
- [testLanguageContext()](LocaleImportFunctionalTest/testLanguageContext.md) — Test msgctxt context support.
- [testEmptyMsgstr()](LocaleImportFunctionalTest/testEmptyMsgstr.md) — Test empty msgstr at end of .po file see #611786.
- [importPoFile()](LocaleImportFunctionalTest/importPoFile.md) — Helper function: import a standalone .po file in a given language.
- [getPoFile()](LocaleImportFunctionalTest/getPoFile.md) — Helper function that returns a proper .po file.
- [getBadPoFile()](LocaleImportFunctionalTest/getBadPoFile.md) — Helper function that returns a bad .po file.
- [getOverwritePoFile()](LocaleImportFunctionalTest/getOverwritePoFile.md) — Helper function that returns a proper .po file, for testing overwriting existing translations.
- [getPoFileWithContext()](LocaleImportFunctionalTest/getPoFileWithContext.md) — Helper function that returns a .po file with context.
- [getPoFileWithEmptyMsgstr()](LocaleImportFunctionalTest/getPoFileWithEmptyMsgstr.md) — Helper function that returns a .po file with an empty last item.
- [getPoFileWithMsgstr()](LocaleImportFunctionalTest/getPoFileWithMsgstr.md) — Helper function that returns a .po file with an empty last item.
- [getPoFileWithMissingPlural()](LocaleImportFunctionalTest/getPoFileWithMissingPlural.md) — Returns a .po file with a missing plural formula.
- [getPoFileWithBrokenPlural()](LocaleImportFunctionalTest/getPoFileWithBrokenPlural.md) — Returns a .po file with a broken plural formula.

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
