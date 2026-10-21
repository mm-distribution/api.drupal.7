# _system_default_theme_features()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2712–2724 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2712-L2724)
- **Module/theme:** system

## Signature

```php
function _system_default_theme_features()
```

## Documentation

```text
Returns an array of default theme features.
```

## Code

```php
function _system_default_theme_features() {
  return array(
    'logo',
    'favicon',
    'name',
    'slogan',
    'node_user_picture',
    'comment_user_picture',
    'comment_user_verification',
    'main_menu',
    'secondary_menu',
  );
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
