# MenuTestCase::resetMenuLink()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 453–466 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L453-L466)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function resetMenuLink($item, $old_title)
```

## Documentation

```text
Reset a standard menu link using the menu module UI.

@param array $item Menu link.
@param string $old_title Original title for menu link.
```

## Code

```php
  function resetMenuLink($item, $old_title) {
    $mlid = $item['mlid'];
    $title = $item['link_title'];

    // Reset menu link.
    $this->drupalPost("admin/structure/menu/item/$mlid/reset", array(), t('Reset'));
    $this->assertResponse(200);
    $this->assertRaw(t('The menu link was reset to its default settings.'), 'Menu link was reset');

    // Verify menu link.
    $this->drupalGet('');
    $this->assertNoText($title, 'Menu link was reset');
    $this->assertText($old_title, 'Menu link was reset');
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
