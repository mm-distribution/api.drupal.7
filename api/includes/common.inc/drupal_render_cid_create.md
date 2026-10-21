# drupal_render_cid_create()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6608–6619 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6608-L6619)

## Signature

```php
function drupal_render_cid_create($elements)
```

## Documentation

```text
Creates the cache ID for a renderable element.

This creates the cache ID string, either by returning the #cache['cid']
property if present or by building the cache ID out of the #cache['keys']
and, optionally, the #cache['granularity'] properties.

@param $elements
  A renderable array.

@return
  The cache ID string, or FALSE if the element may not be cached.
```

## Code

```php
function drupal_render_cid_create($elements) {
  if (isset($elements['#cache']['cid'])) {
    return $elements['#cache']['cid'];
  }
  elseif (isset($elements['#cache']['keys'])) {
    $granularity = isset($elements['#cache']['granularity']) ? $elements['#cache']['granularity'] : NULL;
    // Merge in additional cache ID parts based provided by drupal_render_cid_parts().
    $cid_parts = array_merge($elements['#cache']['keys'], drupal_render_cid_parts($granularity));
    return implode(':', $cid_parts);
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
