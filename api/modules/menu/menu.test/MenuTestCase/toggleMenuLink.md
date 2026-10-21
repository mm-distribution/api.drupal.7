# MenuTestCase::toggleMenuLink()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 493–504 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L493-L504)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function toggleMenuLink($item)
```

## Documentation

```text
Alternately disable and enable a menu link.

@param $item
  Menu link.
```

## Code

```php
  function toggleMenuLink($item) {
    $this->disableMenuLink($item);

    // Verify menu link is absent.
    $this->drupalGet('');
    $this->assertNoText($item['link_title'], 'Menu link was not displayed');
    $this->enableMenuLink($item);

    // Verify menu link is displayed.
    $this->drupalGet('');
    $this->assertText($item['link_title'], 'Menu link was displayed');
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
