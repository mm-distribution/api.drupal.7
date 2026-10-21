# hook_image_style_flush()

- **Type:** Hook (documentation function)
- **File:** [`modules/image/image.api.php`](_file.md), lines 117–120 · [local source](../../../../source/modules/image/image.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.api.php#L117-L120)
- **Module/theme:** image
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_image_style_flush($style)
```

## Documentation

```text
Respond to image style flushing.

This hook enables modules to take effect when a style is being flushed (all
images are being deleted from the server and regenerated). Any
module-specific caches that contain information related to the style should
be cleared using this hook. This hook is called whenever a style is updated,
deleted, or any effect associated with the style is update or deleted.

@param $style
  The image style array that is being flushed.
```

## Code

```php
function hook_image_style_flush($style) {
  // Empty cached data that contains information about the style.
  cache_clear_all('*', 'cache_mymodule', TRUE);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_image_style_flush()".

_None found._

---
_Drupal 7.103 · [modules/image/image.api.php](https://github.com/drupal/drupal/blob/7.103/modules/image/image.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
