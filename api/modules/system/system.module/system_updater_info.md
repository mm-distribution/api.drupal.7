# system_updater_info()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 1879–1892 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1879-L1892)
- **Module/theme:** system
- **Implements:** [hook_updater_info()](../system.api.php/hook_updater_info.md)

## Signature

```php
function system_updater_info()
```

## Documentation

```text
Implements hook_updater_info().
```

## Code

```php
function system_updater_info() {
  return array(
    'module' => array(
      'class' => 'ModuleUpdater',
      'name' => t('Update modules'),
      'weight' => 0,
    ),
    'theme' => array(
      'class' => 'ThemeUpdater',
      'name' => t('Update themes'),
      'weight' => 0,
    ),
  );
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
