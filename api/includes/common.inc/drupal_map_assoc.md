# drupal_map_assoc()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 2910–2918 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L2910-L2918)

## Signature

```php
function drupal_map_assoc($array, $function = NULL)
```

## Documentation

```text
Forms an associative array from a linear array.

This function walks through the provided array and constructs an associative
array out of it. The keys of the resulting array will be the values of the
input array. The values will be the same as the keys unless a function is
specified, in which case the output of the function is used for the values
instead.

@param $array
  A linear array.
@param $function
  A name of a function to apply to all values before output.

@return
  An associative array.
```

## Code

```php
function drupal_map_assoc($array, $function = NULL) {
  // array_combine() fails with empty arrays:
  // http://bugs.php.net/bug.php?id=34857.
  $array = !empty($array) ? array_combine($array, $array) : array();
  if (is_callable($function)) {
    $array = array_map($function, $array);
  }
  return $array;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
