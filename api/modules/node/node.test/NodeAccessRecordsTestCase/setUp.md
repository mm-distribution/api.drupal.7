# NodeAccessRecordsTestCase::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1085–1090 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1085-L1090)
- **Class:** [NodeAccessRecordsTestCase](../NodeAccessRecordsTestCase.md)
- **Module/theme:** node

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    // Enable dummy module that implements hook_node_grants(),
    // hook_node_access_records(), hook_node_grants_alter() and
    // hook_node_access_records_alter().
    parent::setUp('node_test');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
