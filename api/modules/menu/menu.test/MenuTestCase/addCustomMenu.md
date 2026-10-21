# MenuTestCase::addCustomMenu()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 138–184 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L138-L184)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function addCustomMenu()
```

## Documentation

```text
Add custom menu.
```

## Code

```php
  function addCustomMenu() {
    // Add custom menu.

    // Try adding a menu using a menu_name that is too long.
    $this->drupalGet('admin/structure/menu/add');
    $menu_name = substr(hash('sha256', $this->randomName(16)), 0, MENU_MAX_MENU_NAME_LENGTH_UI + 1);
    $title = $this->randomName(16);
    $edit = array(
      'menu_name' => $menu_name,
      'description' => '',
      'title' =>  $title,
    );
    $this->drupalPost('admin/structure/menu/add', $edit, t('Save'));

    // Verify that using a menu_name that is too long results in a validation message.
    $this->assertRaw(t('!name cannot be longer than %max characters but is currently %length characters long.', array(
      '!name' => t('Menu name'),
      '%max' => MENU_MAX_MENU_NAME_LENGTH_UI,
      '%length' => drupal_strlen($menu_name),
    )));

    // Change the menu_name so it no longer exceeds the maximum length.
    $menu_name = substr(hash('sha256', $this->randomName(16)), 0, MENU_MAX_MENU_NAME_LENGTH_UI);
    $edit['menu_name'] = $menu_name;
    $this->drupalPost('admin/structure/menu/add', $edit, t('Save'));

    // Verify that no validation error is given for menu_name length.
    $this->assertNoRaw(t('!name cannot be longer than %max characters but is currently %length characters long.', array(
      '!name' => t('Menu name'),
      '%max' => MENU_MAX_MENU_NAME_LENGTH_UI,
      '%length' => drupal_strlen($menu_name),
    )));
    // Unlike most other modules, there is no confirmation message displayed.

    $this->drupalGet('admin/structure/menu');
    $this->assertText($title, 'Menu created');

    // Enable the custom menu block.
    $menu_name = 'menu-' . $menu_name; // Drupal prepends the name with 'menu-'.
    $edit = array();
    $edit['blocks[menu_' . $menu_name . '][region]'] = 'sidebar_first';
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));
    $this->assertResponse(200);
    $this->assertText(t('The block settings have been updated.'), 'Custom menu block was enabled');

    return menu_load($menu_name);
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
