# system_image_toolkits()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3494–3502 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3494-L3502)
- **Module/theme:** system
- **Implements:** [hook_image_toolkits()](../system.api.php/hook_image_toolkits.md)

## Signature

```php
function system_image_toolkits()
```

## Documentation

```text
Implements hook_image_toolkits().
```

## Code

```php
function system_image_toolkits() {
  include_once DRUPAL_ROOT . '/' . drupal_get_path('module', 'system') . '/' . 'image.gd.inc';
  return array(
    'gd' => array(
      'title' => t('GD2 image manipulation toolkit'),
      'available' => function_exists('image_gd_check_settings') && image_gd_check_settings(),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
