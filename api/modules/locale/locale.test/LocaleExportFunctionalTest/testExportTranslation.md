# LocaleExportFunctionalTest::testExportTranslation()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1375–1395 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1375-L1395)
- **Class:** [LocaleExportFunctionalTest](../LocaleExportFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testExportTranslation()
```

## Documentation

```text
Test exportation of translations.
```

## Code

```php
  function testExportTranslation() {
    // First import some known translations.
    // This will also automatically enable the 'fr' language.
    $name = drupal_tempnam('temporary://', "po_") . '.po';
    file_put_contents($name, $this->getPoFile());
    $this->drupalPost('admin/config/regional/translate/import', array(
      'langcode' => 'fr',
      'files[file]' => $name,
    ), t('Import'));
    drupal_unlink($name);

    // Get the French translations.
    $this->drupalPost('admin/config/regional/translate/export', array(
      'langcode' => 'fr',
    ), t('Export'));

    // Ensure we have a translation file.
    $this->assertRaw('# French translation of Drupal', 'Exported French translation file.');
    // Ensure our imported translations exist in the file.
    $this->assertRaw('msgstr "lundi"', 'French translations present in exported file.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
