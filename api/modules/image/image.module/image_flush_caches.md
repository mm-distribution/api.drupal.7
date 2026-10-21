# image_flush_caches()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 271–273 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L271-L273)
- **Module/theme:** image
- **Implements:** [hook_flush_caches()](../../system/system.api.php/hook_flush_caches.md)

## Signature

```php
function image_flush_caches()
```

## Documentation

```text
Implements hook_flush_caches().
```

## Code

```php
function image_flush_caches() {
  return array('cache_image');
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
