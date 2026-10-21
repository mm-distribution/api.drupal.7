# node_test_node_load()

- **Type:** Function
- **File:** [`modules/node/tests/node_test.module`](_file.md), lines 14–25 · [local source](../../../../../source/modules/node/tests/node_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module#L14-L25)
- **Module/theme:** node_test
- **Implements:** [hook_node_load()](../../node.api.php/hook_node_load.md)

## Signature

```php
function node_test_node_load($nodes, $types)
```

## Documentation

```text
Implements hook_node_load().
```

## Code

```php
function node_test_node_load($nodes, $types) {
  // Add properties to each loaded node which record the parameters that were
  // passed in to this function, so the tests can check that (a) this hook was
  // called, and (b) the parameters were what we expected them to be.
  $nids = array_keys($nodes);
  ksort($nids);
  sort($types);
  foreach ($nodes as $node) {
    $node->node_test_loaded_nids = $nids;
    $node->node_test_loaded_types = $types;
  }
}
```

---
_Drupal 7.103 · [modules/node/tests/node_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
