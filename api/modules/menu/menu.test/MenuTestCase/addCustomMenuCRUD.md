# MenuTestCase::addCustomMenuCRUD()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 111–133 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L111-L133)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function addCustomMenuCRUD()
```

## Documentation

```text
Add custom menu using CRUD functions.
```

## Code

```php
  function addCustomMenuCRUD() {
    // Add a new custom menu.
    $menu_name = substr(hash('sha256', $this->randomName(16)), 0, MENU_MAX_MENU_NAME_LENGTH_UI);
    $title = $this->randomName(16);

    $menu = array(
      'menu_name' => $menu_name,
      'title' => $title,
      'description' => 'Description text',
    );
    menu_save($menu);

    // Assert the new menu.
    $this->drupalGet('admin/structure/menu/manage/' . $menu_name . '/edit');
    $this->assertRaw($title, 'Custom menu was added.');

    // Edit the menu.
    $new_title = $this->randomName(16);
    $menu['title'] = $new_title;
    menu_save($menu);
    $this->drupalGet('admin/structure/menu/manage/' . $menu_name . '/edit');
    $this->assertRaw($new_title, 'Custom menu was edited.');
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
