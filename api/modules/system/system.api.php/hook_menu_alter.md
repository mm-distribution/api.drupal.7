# hook_menu_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1292–1295 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1292-L1295)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_menu_alter(&$items)
```

## Documentation

```text
Alter the data being saved to the {menu_router} table after hook_menu is invoked.

This hook is invoked by menu_router_build(). The menu definitions are passed
in by reference. Each element of the $items array is one item returned
by a module from hook_menu. Additional items may be added, or existing items
altered.

@param $items
  Associative array of menu router definitions returned from hook_menu().
```

## Code

```php
function hook_menu_alter(&$items) {
  // Example - disable the page at node/add
  $items['node/add']['access callback'] = FALSE;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_menu_alter()".

- [comment_menu_alter()](../../comment/comment.module/comment_menu_alter.md) — `modules/comment/comment.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
