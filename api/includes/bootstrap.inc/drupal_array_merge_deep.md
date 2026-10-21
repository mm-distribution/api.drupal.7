# drupal_array_merge_deep()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2461–2464 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2461-L2464)

## Signature

```php
function drupal_array_merge_deep()
```

## Documentation

```text
Merges multiple arrays, recursively, and returns the merged array.

This function is similar to PHP's array_merge_recursive() function, but it
handles non-array values differently. When merging values that are not both
arrays, the latter value replaces the former rather than merging with it.

Example:
@code
$link_options_1 = array('fragment' => 'x', 'attributes' => array('title' => t('X'), 'class' => array('a', 'b')));
$link_options_2 = array('fragment' => 'y', 'attributes' => array('title' => t('Y'), 'class' => array('c', 'd')));

// This results in array('fragment' => array('x', 'y'), 'attributes' => array('title' => array(t('X'), t('Y')), 'class' => array('a', 'b', 'c', 'd'))).
$incorrect = array_merge_recursive($link_options_1, $link_options_2);

// This results in array('fragment' => 'y', 'attributes' => array('title' => t('Y'), 'class' => array('a', 'b', 'c', 'd'))).
$correct = drupal_array_merge_deep($link_options_1, $link_options_2);
@endcode

@param ...
  Arrays to merge.

@return
  The merged array.

@see drupal_array_merge_deep_array()
```

## Code

```php
function drupal_array_merge_deep() {
  $args = func_get_args();
  return drupal_array_merge_deep_array($args);
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
