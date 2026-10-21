# drupal_render_children()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6292–6303 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6292-L6303)

## Signature

```php
function drupal_render_children(&$element, $children_keys = NULL)
```

## Documentation

```text
Renders children of an element and concatenates them.

@param array $element
  The structured array whose children shall be rendered.
@param array $children_keys
  (optional) If the keys of the element's children are already known, they
  can be passed in to save another run of element_children().

@return string
  The rendered HTML of all children of the element.

@see drupal_render()
```

## Code

```php
function drupal_render_children(&$element, $children_keys = NULL) {
  if ($children_keys === NULL) {
    $children_keys = element_children($element);
  }
  $output = '';
  foreach ($children_keys as $key) {
    if (!empty($element[$key])) {
      $output .= drupal_render($element[$key]);
    }
  }
  return $output;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
