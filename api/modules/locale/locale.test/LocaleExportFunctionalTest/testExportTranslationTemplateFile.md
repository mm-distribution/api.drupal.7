# LocaleExportFunctionalTest::testExportTranslationTemplateFile()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1400–1408 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1400-L1408)
- **Class:** [LocaleExportFunctionalTest](../LocaleExportFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testExportTranslationTemplateFile()
```

## Documentation

```text
Test exportation of translation template file.
```

## Code

```php
  function testExportTranslationTemplateFile() {
    // Get the translation template file.
    // There are two 'Export' buttons on this page, but it somehow works.  It'd
    // be better if we could use the submit button id like documented but that
    // doesn't work.
    $this->drupalPost('admin/config/regional/translate/export', array(), t('Export'));
    // Ensure we have a translation file.
    $this->assertRaw('# LANGUAGE translation of PROJECT', 'Exported translation template file.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
