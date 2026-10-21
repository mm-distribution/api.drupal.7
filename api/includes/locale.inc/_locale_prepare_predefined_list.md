# _locale_prepare_predefined_list()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 2209–2229 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L2209-L2229)
- **Topics:** [locale-api-predefined](../../topics/locale-api-predefined.md)

## Signature

```php
function _locale_prepare_predefined_list()
```

## Documentation

```text
Prepares the language code list for a select form item with only the unsupported ones
```

## Code

```php
function _locale_prepare_predefined_list() {
  include_once DRUPAL_ROOT . '/includes/iso.inc';
  $languages = language_list();
  $predefined = _locale_get_predefined_list();
  foreach ($predefined as $key => $value) {
    if (isset($languages[$key])) {
      unset($predefined[$key]);
      continue;
    }
    // Include native name in output, if possible
    if (count($value) > 1) {
      $tname = t($value[0]);
      $predefined[$key] = ($tname == $value[1]) ? $tname : "$tname ($value[1])";
    }
    else {
      $predefined[$key] = t($value[0]);
    }
  }
  asort($predefined);
  return $predefined;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
