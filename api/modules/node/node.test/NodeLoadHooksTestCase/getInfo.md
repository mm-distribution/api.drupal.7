# NodeLoadHooksTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 112–118 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L112-L118)
- **Class:** [NodeLoadHooksTestCase](../NodeLoadHooksTestCase.md)
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
      'name' => 'Node load hooks',
      'description' => 'Test the hooks invoked when a node is being loaded.',
      'group' => 'Node',
    );
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
