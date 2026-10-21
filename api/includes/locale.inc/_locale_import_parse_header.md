# _locale_import_parse_header()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 1218–1228 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L1218-L1228)
- **Topics:** [locale-api-import-export](../../topics/locale-api-import-export.md)

## Signature

```php
function _locale_import_parse_header($header)
```

## Documentation

```text
Parses a Gettext Portable Object file header

@param $header
  A string containing the complete header.

@return
  An associative array of key-value pairs.
```

## Code

```php
function _locale_import_parse_header($header) {
  $header_parsed = array();
  $lines = array_map('trim', explode("\n", $header));
  foreach ($lines as $line) {
    if ($line) {
      list($tag, $contents) = explode(":", $line, 2);
      $header_parsed[trim($tag)] = trim($contents);
    }
  }
  return $header_parsed;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
