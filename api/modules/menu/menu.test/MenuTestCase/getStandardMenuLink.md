# MenuTestCase::getStandardMenuLink()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 581–590 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L581-L590)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
private function getStandardMenuLink()
```

## Documentation

```text
Get standard menu link.
```

## Code

```php
  private function getStandardMenuLink() {
    // Retrieve menu link id of the Log out menu link, which will always be on the front page.
    $mlid = db_query("SELECT mlid FROM {menu_links} WHERE module = 'system' AND router_path = 'user/logout'")->fetchField();
    $this->assertTrue($mlid > 0, 'Standard menu link id was found');
    // Load menu link.
    // Use api function so that link is translated for rendering.
    $item = menu_link_load($mlid);
    $this->assertTrue((bool) $item, 'Standard menu link was loaded');
    return $item;
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
