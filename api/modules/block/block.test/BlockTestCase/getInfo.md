# BlockTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 12–18 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L12-L18)
- **Class:** [BlockTestCase](../BlockTestCase.md)
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
      'name' => 'Block functionality',
      'description' => 'Add, edit and delete custom block. Configure and move a module-defined block.',
      'group' => 'Block',
    );
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
