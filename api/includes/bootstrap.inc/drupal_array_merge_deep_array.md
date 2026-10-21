# drupal_array_merge_deep_array()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2483–2506 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2483-L2506)

## Signature

```php
function drupal_array_merge_deep_array($arrays)
```

## Documentation

```text
Merges multiple arrays, recursively, and returns the merged array.

This function is equivalent to drupal_array_merge_deep(), except the
input arrays are passed as a single array parameter rather than a variable
parameter list.

The following are equivalent:
- drupal_array_merge_deep($a, $b);
- drupal_array_merge_deep_array(array($a, $b));

The following are also equivalent:
- call_user_func_array('drupal_array_merge_deep', $arrays_to_merge);
- drupal_array_merge_deep_array($arrays_to_merge);

@see drupal_array_merge_deep()
```

## Code

```php
function drupal_array_merge_deep_array($arrays) {
  $result = array();

  foreach ($arrays as $array) {
    foreach ($array as $key => $value) {
      // Renumber integer keys as array_merge_recursive() does. Note that PHP
      // automatically converts array keys that are integer strings (e.g., '1')
      // to integers.
      if (is_integer($key)) {
        $result[] = $value;
      }
      // Recurse when both values are arrays.
      elseif (isset($result[$key]) && is_array($result[$key]) && is_array($value)) {
        $result[$key] = drupal_array_merge_deep_array(array($result[$key], $value));
      }
      // Otherwise, use the latter value, overriding any previous value.
      else {
        $result[$key] = $value;
      }
    }
  }

  return $result;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
