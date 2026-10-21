# BlockAdminThemeTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 457–463 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L457-L463)
- **Class:** [BlockAdminThemeTestCase](../BlockAdminThemeTestCase.md)
- **Module/theme:** block

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
      'name' => 'Admin theme block admin accessibility',
      'description' => "Check whether the block administer page for a disabled theme accessible if and only if it's the admin theme.",
      'group' => 'Block',
    );
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
