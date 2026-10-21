# _list_update_7001_extract_allowed_values()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.install`](_file.md), lines 103–124 · [local source](../../../../../../source/modules/field/modules/list/list.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.install#L103-L124)
- **Module/theme:** list

## Signature

```php
function _list_update_7001_extract_allowed_values($string, $position_keys)
```

## Documentation

```text
Helper function for list_update_7001: extract allowed values from a string.

This reproduces the parsing logic in use before D7 RC2.
```

## Code

```php
function _list_update_7001_extract_allowed_values($string, $position_keys) {
  $values = array();

  $list = explode("\n", $string);
  $list = array_map('trim', $list);
  $list = array_filter($list, 'strlen');

  foreach ($list as $key => $value) {
    // Check for a manually specified key.
    if (strpos($value, '|') !== FALSE) {
      list($key, $value) = explode('|', $value);
    }
    // Otherwise see if we need to use the value as the key. The "list" type
    // will automatically convert non-keyed lines to integers.
    elseif (!$position_keys) {
      $key = $value;
    }
    $values[$key] = (isset($value) && $value !== '') ? $value : $key;
  }

  return $values;
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.install](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.install) · Licensed GPL-2.0-or-later (see LICENSE)._
