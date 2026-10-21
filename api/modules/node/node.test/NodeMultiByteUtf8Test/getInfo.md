# NodeMultiByteUtf8Test::getInfo()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 3101–3107 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L3101-L3107)
- **Class:** [NodeMultiByteUtf8Test](../NodeMultiByteUtf8Test.md)
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
      'name' => 'Multi-byte UTF-8',
      'description' => 'Test that multi-byte UTF-8 characters are stored and retrieved correctly.',
      'group' => 'Node',
    );
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
