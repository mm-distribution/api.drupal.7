# MenuTestCase::enableMenuLink()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 528–535 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L528-L535)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function enableMenuLink($item)
```

## Documentation

```text
Enable a menu link.

@param $item
  Menu link.
```

## Code

```php
  function enableMenuLink($item) {
    $mlid = $item['mlid'];
    $edit['enabled'] = TRUE;
    $this->drupalPost("admin/structure/menu/item/$mlid/edit", $edit, t('Save'));

    // Verify in the database.
    $this->assertMenuLink($mlid, array('hidden' => 0));
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
