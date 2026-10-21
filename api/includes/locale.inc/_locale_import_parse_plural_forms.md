# _locale_import_parse_plural_forms()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 1242–1272 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L1242-L1272)
- **Topics:** [locale-api-import-export](../../topics/locale-api-import-export.md)

## Signature

```php
function _locale_import_parse_plural_forms($pluralforms, $filepath)
```

## Documentation

```text
Parses a Plural-Forms entry from a Gettext Portable Object file header

@param $pluralforms
  A string containing the Plural-Forms entry.
@param $filepath
  A string containing the filepath.

@return
  An array containing the number of plurals and a
  formula in PHP for computing the plural form.
```

## Code

```php
function _locale_import_parse_plural_forms($pluralforms, $filepath) {
  // First, delete all whitespace
  $pluralforms = strtr($pluralforms, array(" " => "", "\t" => ""));

  // Select the parts that define nplurals and plural
  $nplurals = strstr($pluralforms, "nplurals=");
  if (strpos($nplurals, ";")) {
    $nplurals = substr($nplurals, 9, strpos($nplurals, ";") - 9);
  }
  else {
    return FALSE;
  }
  $plural = strstr($pluralforms, "plural=");
  if (strpos($plural, ";")) {
    $plural = substr($plural, 7, strpos($plural, ";") - 7);
  }
  else {
    return FALSE;
  }

  // Get PHP version of the plural formula
  $plural = _locale_import_parse_arithmetic($plural);

  if ($plural !== FALSE) {
    return array($nplurals, $plural);
  }
  else {
    drupal_set_message(t('The translation file %filepath contains an error: the plural formula could not be parsed.', array('%filepath' => $filepath)), 'error');
    return FALSE;
  }
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
