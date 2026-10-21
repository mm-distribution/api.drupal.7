# BlockCacheTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 493–499 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L493-L499)
- **Class:** [BlockCacheTestCase](../BlockCacheTestCase.md)
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
      'name' => 'Block caching',
      'description' => 'Test block caching.',
      'group' => 'Block',
    );
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
