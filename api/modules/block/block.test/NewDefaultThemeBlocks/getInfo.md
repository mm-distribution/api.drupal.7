# NewDefaultThemeBlocks::getInfo()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 407–413 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L407-L413)
- **Class:** [NewDefaultThemeBlocks](../NewDefaultThemeBlocks.md)
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
      'name' => 'New default theme blocks',
      'description' => 'Checks that the new default theme gets blocks.',
      'group' => 'Block',
    );
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
