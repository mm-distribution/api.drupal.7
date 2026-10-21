# MenuNodeTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 732–738 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L732-L738)
- **Class:** [MenuNodeTestCase](../MenuNodeTestCase.md)
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
      'name' => 'Menu settings for nodes',
      'description' => 'Add, edit, and delete a node with menu link.',
      'group' => 'Menu',
    );
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
