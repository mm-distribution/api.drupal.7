# overlay_store_rendered_content()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 952–958 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L952-L958)
- **Module/theme:** overlay

## Signature

```php
function overlay_store_rendered_content($id = NULL, $content = NULL)
```

## Documentation

```text
Stores strings representing rendered HTML content.

This function is used to keep a static cache of rendered content that can be
referred to later in the page request.

@param $id
  (Optional) An identifier for the content which is being stored, which will
  be used as an array key in the returned array. If omitted, no change will
  be made to the current stored data.
@param $content
  (Optional) A string representing the rendered data to store. This only has
  an effect if $id is also provided.

@return
  An array representing all data that is currently being stored, or an empty
  array if there is none.

@see overlay_get_rendered_content()
```

## Code

```php
function overlay_store_rendered_content($id = NULL, $content = NULL) {
  $rendered_content = &drupal_static(__FUNCTION__, array());
  if (isset($id)) {
    $rendered_content[$id] = $content;
  }
  return $rendered_content;
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
