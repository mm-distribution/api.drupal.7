# _locale_import_message()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 987–994 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L987-L994)
- **Topics:** [locale-api-import-export](../../topics/locale-api-import-export.md)

## Signature

```php
function _locale_import_message($message, $file, $lineno = NULL)
```

## Documentation

```text
Sets an error message occurred during locale file parsing.

@param $message
  The message to be translated.
@param $file
  Drupal file object corresponding to the PO file to import.
@param $lineno
  An optional line number argument.
```

## Code

```php
function _locale_import_message($message, $file, $lineno = NULL) {
  $vars = array('%filename' => $file->filename);
  if (isset($lineno)) {
    $vars['%line'] = $lineno;
  }
  $t = get_t();
  drupal_set_message($t($message, $vars), 'error');
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
