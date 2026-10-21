# LocaleImportFunctionalTest::importPoFile()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1150–1156 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1150-L1156)
- **Class:** [LocaleImportFunctionalTest](../LocaleImportFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function importPoFile($contents, array $options = array())
```

## Documentation

```text
Helper function: import a standalone .po file in a given language.

@param $contents
  Contents of the .po file to import.
@param $options
  Additional options to pass to the translation import form.
```

## Code

```php
  function importPoFile($contents, array $options = array()) {
    $name = drupal_tempnam('temporary://', "po_") . '.po';
    file_put_contents($name, $contents);
    $options['files[file]'] = $name;
    $this->drupalPost('admin/config/regional/translate/import', $options, t('Import'));
    drupal_unlink($name);
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
