# drupal_render_cache_get()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6402–6418 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6402-L6418)

## Signature

```php
function drupal_render_cache_get($elements)
```

## Documentation

```text
Gets the rendered output of a renderable element from the cache.

@param $elements
  A renderable array.

@return
  A markup string containing the rendered content of the element, or FALSE
  if no cached copy of the element is available.

@see drupal_render()
@see drupal_render_cache_set()
```

## Code

```php
function drupal_render_cache_get($elements) {
  if (!in_array($_SERVER['REQUEST_METHOD'], array('GET', 'HEAD')) || !$cid = drupal_render_cid_create($elements)) {
    return FALSE;
  }
  $bin = isset($elements['#cache']['bin']) ? $elements['#cache']['bin'] : 'cache';

  if (!empty($cid) && $cache = cache_get($cid, $bin)) {
    // Add additional libraries, JavaScript, CSS and other data attached
    // to this element.
    if (isset($cache->data['#attached'])) {
      drupal_process_attached($cache->data);
    }
    // Return the rendered output.
    return $cache->data['#markup'];
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
