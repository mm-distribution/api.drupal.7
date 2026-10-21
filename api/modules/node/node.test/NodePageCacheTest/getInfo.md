# NodePageCacheTest::getInfo()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 3031–3037 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L3031-L3037)
- **Class:** [NodePageCacheTest](../NodePageCacheTest.md)
- **Module/theme:** node

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
        'name' => 'Node page cache test',
        'description' => 'Test cache invalidation of node operations.',
        'group' => 'Node',
    );
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
