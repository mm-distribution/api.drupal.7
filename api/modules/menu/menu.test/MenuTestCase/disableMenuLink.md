# MenuTestCase::disableMenuLink()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 512–520 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L512-L520)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function disableMenuLink($item)
```

## Documentation

```text
Disable a menu link.

@param $item
  Menu link.
```

## Code

```php
  function disableMenuLink($item) {
    $mlid = $item['mlid'];
    $edit['enabled'] = FALSE;
    $this->drupalPost("admin/structure/menu/item/$mlid/edit", $edit, t('Save'));

    // Unlike most other modules, there is no confirmation message displayed.
    // Verify in the database.
    $this->assertMenuLink($mlid, array('hidden' => 1));
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
