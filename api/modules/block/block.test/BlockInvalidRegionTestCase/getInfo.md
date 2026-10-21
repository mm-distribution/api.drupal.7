# BlockInvalidRegionTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 842–848 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L842-L848)
- **Class:** [BlockInvalidRegionTestCase](../BlockInvalidRegionTestCase.md)
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
      'name' => 'Blocks in invalid regions',
      'description' => 'Checks that an active block assigned to a non-existing region triggers the warning message and is disabled.',
      'group' => 'Block',
    );
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
