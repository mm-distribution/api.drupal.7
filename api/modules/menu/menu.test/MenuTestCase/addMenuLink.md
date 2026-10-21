# MenuTestCase::addMenuLink()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 327–355 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L327-L355)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function addMenuLink($plid = 0, $link = '<front>', $menu_name = 'navigation', $expanded = TRUE, $weight = '0')
```

## Documentation

```text
Add a menu link using the menu module UI.

@param integer $plid Parent menu link id.
@param string $link Link path.
@param string $menu_name Menu name.
@param string $weight Menu link weight
@return array Menu link created.
```

## Code

```php
  function addMenuLink($plid = 0, $link = '<front>', $menu_name = 'navigation', $expanded = TRUE, $weight = '0') {
    // View add menu link page.
    $this->drupalGet("admin/structure/menu/manage/$menu_name/add");
    $this->assertResponse(200);
    $this->assertNoOption('edit-parent', 'management:0');

    $title = '!link_' . $this->randomName(16);
    $edit = array(
      'link_path' => $link,
      'link_title' => $title,
      'description' => '',
      'enabled' => TRUE, // Use this to disable the menu and test.
      'expanded' => $expanded, // Setting this to true should test whether it works when we do the std_user tests.
      'parent' =>  $menu_name . ':' . $plid,
      'weight' => $weight,
    );

    // Add menu link.
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertResponse(200);
    // Unlike most other modules, there is no confirmation message displayed.
    $this->assertText($title, 'Menu link was added');

    $item = db_query('SELECT * FROM {menu_links} WHERE link_title = :title', array(':title' => $title))->fetchAssoc();
    $this->assertTrue(t('Menu link was found in database.'));
    $this->assertMenuLink($item['mlid'], array('menu_name' => $menu_name, 'link_path' => $link, 'has_children' => 0, 'plid' => $plid));

    return $item;
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
