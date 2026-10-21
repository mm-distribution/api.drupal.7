# list_extract_allowed_values()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 280–331 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L280-L331)
- **Module/theme:** list

## Signature

```php
function list_extract_allowed_values($string, $field_type, $generate_keys)
```

## Documentation

```text
Parses a string of 'allowed values' into an array.

@param $string
  The list of allowed values in string format described in
  list_allowed_values_string().
@param $field_type
  The field type. Either 'list_number' or 'list_text'.
@param $generate_keys
  Boolean value indicating whether to generate keys based on the position of
  the value if a key is not manually specified, and if the value cannot be
  used as a key. This should only be TRUE for fields of type 'list_number'.

@return
  The array of extracted key/value pairs, or NULL if the string is invalid.

@see list_allowed_values_string()
```

## Code

```php
function list_extract_allowed_values($string, $field_type, $generate_keys) {
  $values = array();

  $list = explode("\n", $string);
  $list = array_map('trim', $list);
  $list = array_filter($list, 'strlen');

  $generated_keys = $explicit_keys = FALSE;
  foreach ($list as $position => $text) {
    $value = $key = FALSE;

    // Check for an explicit key.
    $matches = array();
    if (preg_match('/(.*)\|(.*)/', $text, $matches)) {
      $key = $matches[1];
      $value = $matches[2];
      $explicit_keys = TRUE;
    }
    // Otherwise see if we can use the value as the key. Detecting true integer
    // strings takes a little trick.
    elseif ($field_type == 'list_text'
    || ($field_type == 'list_float' && is_numeric($text))
    || ($field_type == 'list_integer' && is_numeric($text) && (float) $text == intval($text))) {
      $key = $value = $text;
      $explicit_keys = TRUE;
    }
    // Otherwise see if we can generate a key from the position.
    elseif ($generate_keys) {
      $key = (string) $position;
      $value = $text;
      $generated_keys = TRUE;
    }
    else {
      return;
    }

    // Float keys are represented as strings and need to be disambiguated
    // ('.5' is '0.5').
    if ($field_type == 'list_float' && is_numeric($key)) {
      $key = (string) (float) $key;
    }

    $values[$key] = $value;
  }

  // We generate keys only if the list contains no explicit key at all.
  if ($explicit_keys && $generated_keys) {
    return;
  }

  return $values;
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
