# hook_menu_link_insert()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1365–1372 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1365-L1372)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_menu_link_insert($link)
```

## Documentation

```text
Inform modules that a menu link has been created.

This hook is used to notify modules that menu items have been
created. Contributed modules may use the information to perform
actions based on the information entered into the menu system.

@param $link
  Associative array defining a menu link as passed into menu_link_save().

@see hook_menu_link_update()
@see hook_menu_link_delete()
```

## Code

```php
function hook_menu_link_insert($link) {
  // In our sample case, we track menu items as editing sections
  // of the site. These are stored in our table as 'disabled' items.
  $record['mlid'] = $link['mlid'];
  $record['menu_name'] = $link['menu_name'];
  $record['status'] = 0;
  drupal_write_record('menu_example', $record);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_menu_link_insert()".

- [menu_test_menu_link_insert()](../../simpletest/tests/menu_test.module/menu_test_menu_link_insert.md) — `modules/simpletest/tests/menu_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
