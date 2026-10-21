# menu_permission()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 48–54 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L48-L54)
- **Module/theme:** menu
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function menu_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function menu_permission() {
  return array(
    'administer menu' => array(
      'title' => t('Administer menus and menu items'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
