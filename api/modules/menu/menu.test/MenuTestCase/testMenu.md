# MenuTestCase::testMenu()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 32–86 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L32-L86)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function testMenu()
```

## Documentation

```text
Login users, add menus and menu links, and test menu functionality through the admin and user interfaces.
```

## Code

```php
  function testMenu() {
    // Login the user.
    $this->drupalLogin($this->big_user);
    $this->items = array();

    // Do standard menu tests.
    $this->doStandardMenuTests();

    // Do custom menu tests.
    $this->doCustomMenuTests();

    // Do standard user tests.
    // Login the user.
    $this->drupalLogin($this->std_user);
    $this->verifyAccess(403);
    foreach ($this->items as $item) {
      $node = node_load(substr($item['link_path'], 5)); // Paths were set as 'node/$nid'.
      $this->verifyMenuLink($item, $node);
    }

    // Login the user.
    $this->drupalLogin($this->big_user);

    // Delete menu links.
    foreach ($this->items as $item) {
      $this->deleteMenuLink($item);
    }

    // Delete custom menu.
    $this->deleteCustomMenu($this->menu);

    // Modify and reset a standard menu link.
    $item = $this->getStandardMenuLink();
    $old_title = $item['link_title'];
    $this->modifyMenuLink($item);
    $item = menu_link_load($item['mlid']);
    // Verify that a change to the description is saved.
    $description = $this->randomName(16);
    $item['options']['attributes']['title']  = $description;
    menu_link_save($item);
    $saved_item = menu_link_load($item['mlid']);
    $this->assertEqual($description, $saved_item['options']['attributes']['title'], 'Saving an existing link updates the description (title attribute)');
    $this->resetMenuLink($item, $old_title);

    // Test that the page title is correct when a local task appears in a
    // top-level menu item. See https://www.drupal.org/node/1973262.
    $item = $this->addMenuLink(0, 'user/register', 'user-menu');
    $this->drupalGet('user/password');
    $this->assertNoTitle('Home | Drupal');
    $this->drupalLogout();
    $this->drupalGet('user/register');
    $this->assertTitle($item['link_title'] . ' | Drupal');
    $this->drupalGet('user');
    $this->assertNoTitle('Home | Drupal');
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
