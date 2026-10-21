# drupal_render_cache_set()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6433–6454 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6433-L6454)

## Signature

```php
function drupal_render_cache_set(&$markup, $elements)
```

## Documentation

```text
Caches the rendered output of a renderable element.

This is called by drupal_render() if the #cache property is set on an
element.

@param $markup
  The rendered output string of $elements.
@param $elements
  A renderable array.

@see drupal_render_cache_get()
```

## Code

```php
function drupal_render_cache_set(&$markup, $elements) {
  // Create the cache ID for the element.
  if (!in_array($_SERVER['REQUEST_METHOD'], array('GET', 'HEAD')) || !$cid = drupal_render_cid_create($elements)) {
    return FALSE;
  }

  // Cache implementations are allowed to modify the markup, to support
  // replacing markup with edge-side include commands. The supporting cache
  // backend will store the markup in some other key (like
  // $data['#real-value']) and return an include command instead. When the
  // ESI command is executed by the content accelerator, the real value can
  // be retrieved and used.
  $data['#markup'] = &$markup;
  // Persist attached data associated with this element.
  $attached = drupal_render_collect_attached($elements, TRUE);
  if ($attached) {
    $data['#attached'] = $attached;
  }
  $bin = isset($elements['#cache']['bin']) ? $elements['#cache']['bin'] : 'cache';
  $expire = isset($elements['#cache']['expire']) ? $elements['#cache']['expire'] : CACHE_PERMANENT;
  cache_set($cid, $data, $bin, $expire);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
