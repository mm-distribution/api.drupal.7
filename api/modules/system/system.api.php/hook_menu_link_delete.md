# hook_menu_link_delete()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1411–1416 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1411-L1416)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_menu_link_delete($link)
```

## Documentation

```text
Inform modules that a menu link has been deleted.

This hook is used to notify modules that menu items have been
deleted. Contributed modules may use the information to perform
actions based on the information entered into the menu system.

@param $link
  Associative array defining a menu link as passed into menu_link_save().

@see hook_menu_link_insert()
@see hook_menu_link_update()
```

## Code

```php
function hook_menu_link_delete($link) {
  // Delete the record from our table.
  db_delete('menu_example')
    ->condition('mlid', $link['mlid'])
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_menu_link_delete()".

- [menu_test_menu_link_delete()](../../simpletest/tests/menu_test.module/menu_test_menu_link_delete.md) — `modules/simpletest/tests/menu_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
