# MenuTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 14–20 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L14-L20)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Menu link creation/deletion',
      'description' => 'Add a custom menu, add menu links to the custom menu and Navigation menu, check their data, and delete them using the menu module UI.',
      'group' => 'Menu'
    );
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
