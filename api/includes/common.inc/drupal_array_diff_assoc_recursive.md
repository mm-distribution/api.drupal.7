# drupal_array_diff_assoc_recursive()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6868–6889 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6868-L6889)

## Signature

```php
function drupal_array_diff_assoc_recursive($array1, $array2)
```

## Documentation

```text
Recursively computes the difference of arrays with additional index check.

This is a version of array_diff_assoc() that supports multidimensional
arrays.

@param array $array1
  The array to compare from.
@param array $array2
  The array to compare to.

@return array
  Returns an array containing all the values from array1 that are not present
  in array2.
```

## Code

```php
function drupal_array_diff_assoc_recursive($array1, $array2) {
  $difference = array();

  foreach ($array1 as $key => $value) {
    if (is_array($value)) {
      if (!array_key_exists($key, $array2) || !is_array($array2[$key])) {
        $difference[$key] = $value;
      }
      else {
        $new_diff = drupal_array_diff_assoc_recursive($value, $array2[$key]);
        if (!empty($new_diff)) {
          $difference[$key] = $new_diff;
        }
      }
    }
    elseif (!array_key_exists($key, $array2) || $array2[$key] !== $value) {
      $difference[$key] = $value;
    }
  }

  return $difference;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
