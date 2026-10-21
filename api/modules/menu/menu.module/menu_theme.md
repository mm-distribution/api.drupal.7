# menu_theme()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 162–173 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L162-L173)
- **Module/theme:** menu
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function menu_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function menu_theme() {
  return array(
    'menu_overview_form' => array(
      'file' => 'menu.admin.inc',
      'render element' => 'form',
    ),
    'menu_admin_overview' => array(
      'file' => 'menu.admin.inc',
      'variables' => array('title' => NULL, 'name' => NULL, 'description' => NULL),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
