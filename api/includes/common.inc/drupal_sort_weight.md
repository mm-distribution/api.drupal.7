# drupal_sort_weight()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6698–6705 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6698-L6705)

## Signature

```php
function drupal_sort_weight($a, $b)
```

## Documentation

```text
Sorts a structured array by the 'weight' element.

Note that the sorting is by the 'weight' array element, not by the render
element property '#weight'.

Callback for uasort() used in various functions.

@param $a
  First item for comparison. The compared items should be associative arrays
  that optionally include a 'weight' element. For items without a 'weight'
  element, a default value of 0 will be used.
@param $b
  Second item for comparison.
```

## Code

```php
function drupal_sort_weight($a, $b) {
  $a_weight = (is_array($a) && isset($a['weight'])) ? $a['weight'] : 0;
  $b_weight = (is_array($b) && isset($b['weight'])) ? $b['weight'] : 0;
  if ($a_weight == $b_weight) {
    return 0;
  }
  return ($a_weight < $b_weight) ? -1 : 1;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
