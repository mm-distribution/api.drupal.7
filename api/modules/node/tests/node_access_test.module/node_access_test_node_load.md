# node_access_test_node_load()

- **Type:** Function
- **File:** [`modules/node/tests/node_access_test.module`](_file.md), lines 191–196 · [local source](../../../../../source/modules/node/tests/node_access_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module#L191-L196)
- **Module/theme:** node_test
- **Implements:** [hook_node_load()](../../node.api.php/hook_node_load.md)

## Signature

```php
function node_access_test_node_load($nodes, $types)
```

## Documentation

```text
Implements hook_node_load().
```

## Code

```php
function node_access_test_node_load($nodes, $types) {
  $result = db_query('SELECT nid, private FROM {node_access_test} WHERE nid IN(:nids)', array(':nids' => array_keys($nodes)));
  foreach ($result as $record) {
    $nodes[$record->nid]->private = $record->private;
  }
}
```

---
_Drupal 7.103 · [modules/node/tests/node_access_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
