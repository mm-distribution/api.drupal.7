# node_test_node_grants()

- **Type:** Function
- **File:** [`modules/node/tests/node_test.module`](_file.md), lines 57–66 · [local source](../../../../../source/modules/node/tests/node_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module#L57-L66)
- **Module/theme:** node_test
- **Implements:** [hook_node_grants()](../../node.api.php/hook_node_grants.md)

## Signature

```php
function node_test_node_grants($account, $op)
```

## Documentation

```text
Implements hook_node_grants().
```

## Code

```php
function node_test_node_grants($account, $op) {
  // Give everyone full grants so we don't break other node tests.
  // Our node access tests asserts three realms of access.
  // See testGrantAlter().
  return array(
    'test_article_realm' => array(1),
    'test_page_realm' => array(1),
    'test_alter_realm' => array(2),
  );
}
```

---
_Drupal 7.103 · [modules/node/tests/node_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
