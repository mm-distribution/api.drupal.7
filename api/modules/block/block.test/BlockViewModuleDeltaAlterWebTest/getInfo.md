# BlockViewModuleDeltaAlterWebTest::getInfo()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 761–767 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L761-L767)
- **Class:** [BlockViewModuleDeltaAlterWebTest](../BlockViewModuleDeltaAlterWebTest.md)
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
      'name' => 'Block view module delta alter',
      'description' => 'Test the hook_block_view_MODULE_DELTA_alter() hook.',
      'group' => 'Block',
    );
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
