# overlay_get_rendered_content()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 928–930 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L928-L930)
- **Module/theme:** overlay

## Signature

```php
function overlay_get_rendered_content()
```

## Documentation

```text
Returns any rendered content that was stored earlier in the page request.

@return
  An array of all rendered HTML that was stored earlier in the page request,
  keyed by the identifier with which it was stored. If no content was
  stored, an empty array is returned.

@see overlay_store_rendered_content()
```

## Code

```php
function overlay_get_rendered_content() {
  return overlay_store_rendered_content();
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
