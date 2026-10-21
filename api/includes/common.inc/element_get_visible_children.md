# element_get_visible_children()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6806–6826 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6806-L6826)

## Signature

```php
function element_get_visible_children(array $elements)
```

## Documentation

```text
Returns the visible children of an element.

@param $elements
  The parent element.

@return
  The array keys of the element's visible children.
```

## Code

```php
function element_get_visible_children(array $elements) {
  $visible_children = array();

  foreach (element_children($elements) as $key) {
    $child = $elements[$key];

    // Skip un-accessible children.
    if (isset($child['#access']) && !$child['#access']) {
      continue;
    }

    // Skip value and hidden elements, since they are not rendered.
    if (isset($child['#type']) && in_array($child['#type'], array('value', 'hidden'))) {
      continue;
    }

    $visible_children[$key] = $child;
  }

  return array_keys($visible_children);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
