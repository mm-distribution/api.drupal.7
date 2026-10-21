# system_add_module_assets()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 1970–1985 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1970-L1985)
- **Module/theme:** system

## Signature

```php
function system_add_module_assets()
```

## Documentation

```text
Adds CSS and JavaScript files declared in module .info files.
```

## Code

```php
function system_add_module_assets() {
  foreach (system_get_info('module') as $module => $info) {
    if (!empty($info['stylesheets'])) {
      foreach ($info['stylesheets'] as $media => $stylesheets) {
        foreach ($stylesheets as $stylesheet) {
          drupal_add_css($stylesheet, array('every_page' => TRUE, 'media' => $media));
        }
      }
    }
    if (!empty($info['scripts'])) {
      foreach ($info['scripts'] as $script) {
        drupal_add_js($script, array('every_page' => TRUE));
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
