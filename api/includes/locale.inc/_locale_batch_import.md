# _locale_batch_import()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 2365–2373 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L2365-L2373)
- **Topics:** [locale-autoimport](../../topics/locale-autoimport.md)

## Signature

```php
function _locale_batch_import($filepath, &$context)
```

## Documentation

```text
Implements callback_batch_operation().

Perform interface translation import as a batch step.

@param $filepath
  Path to a file to import.
@param $results
  Contains a list of files imported.
```

## Code

```php
function _locale_batch_import($filepath, &$context) {
  // The filename is either {langcode}.po or {prefix}.{langcode}.po, so
  // we can extract the language code to use for the import from the end.
  if (preg_match('!(/|\.)([^\./]+)\.po$!', $filepath, $langcode)) {
    $file = (object) array('filename' => drupal_basename($filepath), 'uri' => $filepath);
    _locale_import_read_po('db-store', $file, LOCALE_IMPORT_KEEP, $langcode[2]);
    $context['results'][] = $filepath;
  }
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
