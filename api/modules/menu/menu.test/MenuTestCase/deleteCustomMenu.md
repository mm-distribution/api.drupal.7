# MenuTestCase::deleteCustomMenu()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 191–203 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L191-L203)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function deleteCustomMenu($menu)
```

## Documentation

```text
Delete custom menu.

@param string $menu_name Custom menu name.
```

## Code

```php
  function deleteCustomMenu($menu) {
    $menu_name = $this->menu['menu_name'];
    $title = $this->menu['title'];

    // Delete custom menu.
    $this->drupalPost("admin/structure/menu/manage/$menu_name/delete", array(), t('Delete'));
    $this->assertResponse(200);
    $this->assertRaw(t('The custom menu %title has been deleted.', array('%title' => $title)), 'Custom menu was deleted');
    $this->assertFalse(menu_load($menu_name), 'Custom menu was deleted');
    // Test if all menu links associated to the menu were removed from database.
    $result = db_query("SELECT menu_name FROM {menu_links} WHERE menu_name = :menu_name", array(':menu_name' => $menu_name))->fetchField();
    $this->assertFalse($result, 'All menu links associated to the custom menu were deleted.');
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
