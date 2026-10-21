# drupal_array_nested_key_exists()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7063–7069 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7063-L7069)

## Signature

```php
function drupal_array_nested_key_exists(array $array, array $parents)
```

## Documentation

```text
Determines whether a nested array contains the requested keys.

This helper function should be used when the depth of the array element to be
checked may vary (that is, the number of parent keys is variable). See
drupal_array_set_nested_value() for details. It is primarily used for form
structures and renderable arrays.

If it is required to also get the value of the checked nested key, use
drupal_array_get_nested_value() instead.

If the number of array parent keys is static, this helper function is
unnecessary and the following code can be used instead:
@code
$value_exists = isset($form['signature_settings']['signature']);
$key_exists = array_key_exists('signature', $form['signature_settings']);
@endcode

@param $array
  The array with the value to check for.
@param $parents
  An array of parent keys of the value, starting with the outermost key.

@return
  TRUE if all the parent keys exist, FALSE otherwise.

@see drupal_array_get_nested_value()
```

## Code

```php
function drupal_array_nested_key_exists(array $array, array $parents) {
  // Although this function is similar to PHP's array_key_exists(), its
  // arguments should be consistent with drupal_array_get_nested_value().
  $key_exists = NULL;
  drupal_array_get_nested_value($array, $parents, $key_exists);
  return $key_exists;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
