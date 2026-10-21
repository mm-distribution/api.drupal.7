# NodeTypePersistenceTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1686–1692 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1686-L1692)
- **Class:** [NodeTypePersistenceTestCase](../NodeTypePersistenceTestCase.md)
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
      'name' => 'Node type persist',
      'description' => 'Ensures that node type customization survives module enabling and disabling.',
      'group' => 'Node',
    );
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
