# options_array_transpose()

- **Type:** Function
- **File:** [`modules/field/modules/options/options.module`](_file.md), lines 351–366 · [local source](../../../../../../source/modules/field/modules/options/options.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module#L351-L366)
- **Module/theme:** options

## Signature

```php
function options_array_transpose($array)
```

## Documentation

```text
Manipulates a 2D array to reverse rows and columns.

The default data storage for fields is delta first, column names second.
This is sometimes inconvenient for field modules, so this function can be
used to present the data in an alternate format.

@param $array
  The array to be transposed. It must be at least two-dimensional, and
  the subarrays must all have the same keys or behavior is undefined.
@return
  The transposed array.
```

## Code

```php
function options_array_transpose($array) {
  $result = array();
  if (is_array($array)) {
    foreach ($array as $key1 => $value1) {
      if (is_array($value1)) {
        foreach ($value1 as $key2 => $value2) {
          if (!isset($result[$key2])) {
            $result[$key2] = array();
          }
          $result[$key2][$key1] = $value2;
        }
      }
    }
  }
  return $result;
}
```

---
_Drupal 7.103 · [modules/field/modules/options/options.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module) · Licensed GPL-2.0-or-later (see LICENSE)._
