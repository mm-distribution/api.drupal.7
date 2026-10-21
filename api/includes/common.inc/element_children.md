# element_children()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6755–6795 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6755-L6795)

## Signature

```php
function element_children(&$elements, $sort = FALSE)
```

## Documentation

```text
Identifies the children of an element array, optionally sorted by weight.

The children of a element array are those key/value pairs whose key does
not start with a '#'. See drupal_render() for details.

@param $elements
  The element array whose children are to be identified.
@param $sort
  Boolean to indicate whether the children should be sorted by weight.

@return
  The array keys of the element's children.
```

## Code

```php
function element_children(&$elements, $sort = FALSE) {
  // Do not attempt to sort elements which have already been sorted.
  $sort = isset($elements['#sorted']) ? !$elements['#sorted'] : $sort;

  // Filter out properties from the element, leaving only children.
  $count = count($elements);
  $child_weights = array();
  $i = 0;
  $sortable = FALSE;
  foreach ($elements as $key => $value) {
    if (is_int($key) || $key === '' || $key[0] !== '#') {
      if (is_array($value) && isset($value['#weight'])) {
        $weight = $value['#weight'];
        $sortable = TRUE;
      }
      else {
        $weight = 0;
      }
      // Support weights with up to three digit precision and conserve the
      // insertion order.
      $child_weights[$key] = floor($weight * 1000) + $i / $count;
    }
    $i++;
  }

  // Sort the children if necessary.
  if ($sort && $sortable) {
    asort($child_weights);
    // Put the sorted children back into $elements in the correct order, to
    // preserve sorting if the same element is passed through
    // element_children() twice.
    foreach ($child_weights as $key => $weight) {
      $value = $elements[$key];
      unset($elements[$key]);
      $elements[$key] = $value;
    }
    $elements['#sorted'] = TRUE;
  }

  return array_keys($child_weights);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
