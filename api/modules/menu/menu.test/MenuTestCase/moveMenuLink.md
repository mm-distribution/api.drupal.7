# MenuTestCase::moveMenuLink()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 411–422 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L411-L422)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function moveMenuLink($item, $plid, $menu_name)
```

## Documentation

```text
Change the parent of a menu link using the menu module UI.
```

## Code

```php
  function moveMenuLink($item, $plid, $menu_name) {
    $mlid = $item['mlid'];

    $this->drupalGet("admin/structure/menu/item/$mlid/edit");
    $this->assertOption('edit-parent', 'management:0');

    $edit = array(
      'parent' => $menu_name . ':' . $plid,
    );
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertResponse(200);
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
