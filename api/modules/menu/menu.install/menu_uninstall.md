# menu_uninstall()

- **Type:** Function
- **File:** [`modules/menu/menu.install`](_file.md), lines 68–70 · [local source](../../../../source/modules/menu/menu.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.install#L68-L70)
- **Module/theme:** menu
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function menu_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function menu_uninstall() {
  menu_rebuild();
}
```

---
_Drupal 7.103 · [modules/menu/menu.install](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.install) · Licensed GPL-2.0-or-later (see LICENSE)._
