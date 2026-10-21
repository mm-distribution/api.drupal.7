# NodeAccessBaseTableTestCase::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1174–1178 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1174-L1178)
- **Class:** [NodeAccessBaseTableTestCase](../NodeAccessBaseTableTestCase.md)
- **Module/theme:** node

## Signature

```php
public function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  public function setUp() {
    parent::setUp('node_access_test');
    node_access_rebuild();
    variable_set('node_access_test_private', TRUE);
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
