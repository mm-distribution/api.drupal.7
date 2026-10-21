# list_allowed_values_string()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 347–353 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L347-L353)
- **Module/theme:** list

## Signature

```php
function list_allowed_values_string($values)
```

## Documentation

```text
Generates a string representation of an array of 'allowed values'.

This string format is suitable for edition in a textarea.

@param $values
  An array of values, where array keys are values and array values are
  labels.

@return
  The string representation of the $values array:
   - Values are separated by a carriage return.
   - Each value is in the format "value|label" or "value".
```

## Code

```php
function list_allowed_values_string($values) {
  $lines = array();
  foreach ($values as $key => $value) {
    $lines[] = "$key|$value";
  }
  return implode("\n", $lines);
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
