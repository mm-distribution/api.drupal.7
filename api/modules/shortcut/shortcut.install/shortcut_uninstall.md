# shortcut_uninstall()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.install`](_file.md), lines 41–47 · [local source](../../../../source/modules/shortcut/shortcut.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.install#L41-L47)
- **Module/theme:** shortcut
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function shortcut_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function shortcut_uninstall() {
  drupal_load('module', 'shortcut');
  // Delete the menu links associated with each shortcut set.
  foreach (shortcut_sets() as $shortcut_set) {
    menu_delete_links($shortcut_set->set_name);
  }
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.install](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.install) · Licensed GPL-2.0-or-later (see LICENSE)._
