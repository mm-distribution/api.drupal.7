# drupal_render_collect_attached()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6472–6497 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6472-L6497)

## Signature

```php
function drupal_render_collect_attached($elements, $return = FALSE)
```

## Documentation

```text
Collects #attached for an element and its children into a single array.

When caching elements, it is necessary to collect all libraries, JavaScript
and CSS into a single array, from both the element itself and all child
elements. This allows drupal_render() to add these back to the page when the
element is returned from cache.

@param $elements
  The element to collect #attached from.
@param $return
  Whether to return the attached elements and reset the internal static.

@return
  The #attached array for this element and its descendants.
```

## Code

```php
function drupal_render_collect_attached($elements, $return = FALSE) {
  $attached = &drupal_static(__FUNCTION__, array());

  // Collect all #attached for this element.
  if (isset($elements['#attached'])) {
    foreach ($elements['#attached'] as $key => $value) {
      if (!isset($attached[$key])) {
        $attached[$key] = array();
      }
      $attached[$key] = array_merge($attached[$key], $value);
    }
  }
  if ($children = element_children($elements)) {
    foreach ($children as $child) {
      drupal_render_collect_attached($elements[$child]);
    }
  }

  // If this was the first call to the function, return all attached elements
  // and reset the static cache.
  if ($return) {
    $return = $attached;
    $attached = array();
    return $return;
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
