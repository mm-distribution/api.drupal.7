# NodeAccessTestCase::assertNodeAccess()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1021–1026 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1021-L1026)
- **Class:** [NodeAccessTestCase](../NodeAccessTestCase.md)
- **Module/theme:** node

## Signature

```php
function assertNodeAccess($ops, $node, $account)
```

## Documentation

```text
Asserts node_access() correctly grants or denies access.
```

## Code

```php
  function assertNodeAccess($ops, $node, $account) {
    foreach ($ops as $op => $result) {
      $msg = format_string("node_access returns @result with operation '@op'.", array('@result' => $result ? 'true' : 'false', '@op' => $op));
      $this->assertEqual($result, node_access($op, $node, $account), $msg);
    }
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
