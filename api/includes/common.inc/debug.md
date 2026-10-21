# debug()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7911–7919 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7911-L7919)

## Signature

```php
function debug($data, $label = NULL, $print_r = FALSE)
```

## Documentation

```text
Outputs debug information.

The debug information is passed on to trigger_error() after being converted
to a string using _drupal_debug_message().

@param $data
  Data to be output.
@param $label
  Label to prefix the data.
@param $print_r
  Flag to switch between print_r() and var_export() for data conversion to
  string. Set $print_r to TRUE when dealing with a recursive data structure
  as var_export() will generate an error.
```

## Code

```php
function debug($data, $label = NULL, $print_r = FALSE) {
  // Print $data contents to string.
  $string = check_plain($print_r ? print_r($data, TRUE) : var_export($data, TRUE));

  // Display values with pre-formatting to increase readability.
  $string = '<pre>' . $string . '</pre>';

  trigger_error(trim($label ? "$label: $string" : $string));
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
