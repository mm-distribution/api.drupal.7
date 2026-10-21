# hook_menu_link_update()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1387–1396 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1387-L1396)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_menu_link_update($link)
```

## Documentation

```text
Inform modules that a menu link has been updated.

This hook is used to notify modules that menu items have been
updated. Contributed modules may use the information to perform
actions based on the information entered into the menu system.

@param $link
  Associative array defining a menu link as passed into menu_link_save().

@see hook_menu_link_insert()
@see hook_menu_link_delete()
```

## Code

```php
function hook_menu_link_update($link) {
  // If the parent menu has changed, update our record.
  $menu_name = db_query("SELECT menu_name FROM {menu_example} WHERE mlid = :mlid", array(':mlid' => $link['mlid']))->fetchField();
  if ($menu_name != $link['menu_name']) {
    db_update('menu_example')
      ->fields(array('menu_name' => $link['menu_name']))
      ->condition('mlid', $link['mlid'])
      ->execute();
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_menu_link_update()".

- [menu_test_menu_link_update()](../../simpletest/tests/menu_test.module/menu_test_menu_link_update.md) — `modules/simpletest/tests/menu_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
