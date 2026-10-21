# drupal_array_get_nested_value()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7019–7033 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7019-L7033)

## Signature

```php
function &drupal_array_get_nested_value(array &$array, array $parents, &$key_exists = NULL)
```

## Documentation

```text
Retrieves a value from a nested array with variable depth.

This helper function should be used when the depth of the array element being
retrieved may vary (that is, the number of parent keys is variable). It is
primarily used for form structures and renderable arrays.

Without this helper function the only way to get a nested array value with
variable depth in one line would be using eval(), which should be avoided:
@code
// Do not do this! Avoid eval().
// May also throw a PHP notice, if the variable array keys do not exist.
eval('$value = $array[\'' . implode("']['", $parents) . "'];");
@endcode

Instead, use this helper function:
@code
$value = drupal_array_get_nested_value($form, $parents);
@endcode

A return value of NULL is ambiguous, and can mean either that the requested
key does not exist, or that the actual value is NULL. If it is required to
know whether the nested array key actually exists, pass a third argument that
is altered by reference:
@code
$key_exists = NULL;
$value = drupal_array_get_nested_value($form, $parents, $key_exists);
if ($key_exists) {
  // ... do something with $value ...
}
@endcode

However if the number of array parent keys is static, the value should always
be retrieved directly rather than calling this function. For instance:
@code
$value = $form['signature_settings']['signature'];
@endcode

@param $array
  The array from which to get the value.
@param $parents
  An array of parent keys of the value, starting with the outermost key.
@param $key_exists
  (optional) If given, an already defined variable that is altered by
  reference.

@return
  The requested nested value. Possibly NULL if the value is NULL or not all
  nested parent keys exist. $key_exists is altered by reference and is a
  Boolean that indicates whether all nested parent keys exist (TRUE) or not
  (FALSE). This allows to distinguish between the two possibilities when NULL
  is returned.

@see drupal_array_set_nested_value()
```

## Code

```php
function &drupal_array_get_nested_value(array &$array, array $parents, &$key_exists = NULL) {
  $ref = &$array;
  foreach ($parents as $parent) {
    if (is_array($ref) && (isset($ref[$parent]) || array_key_exists($parent, $ref))) {
      $ref = &$ref[$parent];
    }
    else {
      $key_exists = FALSE;
      $null = NULL;
      return $null;
    }
  }
  $key_exists = TRUE;
  return $ref;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
