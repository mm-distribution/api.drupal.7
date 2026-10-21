# image_permission()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 240–247 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L240-L247)
- **Module/theme:** image
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function image_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function image_permission() {
  return array(
    'administer image styles' => array(
      'title' => t('Administer image styles'),
      'description' => t('Create and modify styles for generating image modifications such as thumbnails.'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
