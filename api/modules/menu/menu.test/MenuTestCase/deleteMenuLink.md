# MenuTestCase::deleteMenuLink()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 473–485 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L473-L485)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function deleteMenuLink($item)
```

## Documentation

```text
Delete a menu link using the menu module UI.

@param array $item Menu link.
```

## Code

```php
  function deleteMenuLink($item) {
    $mlid = $item['mlid'];
    $title = $item['link_title'];

    // Delete menu link.
    $this->drupalPost("admin/structure/menu/item/$mlid/delete", array(), t('Confirm'));
    $this->assertResponse(200);
    $this->assertRaw(t('The menu link %title has been deleted.', array('%title' => $title)), 'Menu link was deleted');

    // Verify deletion.
    $this->drupalGet('');
    $this->assertNoText($title, 'Menu link was deleted');
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
