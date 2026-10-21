# path_permission()

- **Type:** Function
- **File:** [`modules/path/path.module`](_file.md), lines 40–50 · [local source](../../../../source/modules/path/path.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module#L40-L50)
- **Module/theme:** path
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function path_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function path_permission() {
  return array(
    'administer url aliases' => array(
      'title' => t('Administer URL aliases'),
      'restrict access' => TRUE,
    ),
    'create url aliases' => array(
      'title' => t('Create and edit URL aliases'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/path/path.module](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module) · Licensed GPL-2.0-or-later (see LICENSE)._
