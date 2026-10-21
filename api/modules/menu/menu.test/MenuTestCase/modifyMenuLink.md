# MenuTestCase::modifyMenuLink()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 429–445 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L429-L445)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function modifyMenuLink(&$item)
```

## Documentation

```text
Modify a menu link using the menu module UI.

@param array $item Menu link passed by reference.
```

## Code

```php
  function modifyMenuLink(&$item) {
    $item['link_title'] = $this->randomName(16);

    $mlid = $item['mlid'];
    $title = $item['link_title'];

    // Edit menu link.
    $edit = array();
    $edit['link_title'] = $title;
    $this->drupalPost("admin/structure/menu/item/$mlid/edit", $edit, t('Save'));
    $this->assertResponse(200);
    // Unlike most other modules, there is no confirmation message displayed.

    // Verify menu link.
    $this->drupalGet('admin/structure/menu/manage/' . $item['menu_name']);
    $this->assertText($title, 'Menu link was edited');
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
