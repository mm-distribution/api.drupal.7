# node_test_node_presave()

- **Type:** Function
- **File:** [`modules/node/tests/node_test.module`](_file.md), lines 128–141 · [local source](../../../../../source/modules/node/tests/node_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module#L128-L141)
- **Module/theme:** node_test
- **Implements:** [hook_node_presave()](../../node.api.php/hook_node_presave.md)

## Signature

```php
function node_test_node_presave($node)
```

## Documentation

```text
Implements hook_node_presave().
```

## Code

```php
function node_test_node_presave($node) {
  if ($node->title == 'testing_node_presave') {
    // Sun, 19 Nov 1978 05:00:00 GMT
    $node->created = 280299600;
    // Drupal 1.0 release.
    $node->changed = 979534800;
  }
  // Determine changes.
  if (!empty($node->original) && $node->original->title == 'test_changes') {
    if ($node->original->title != $node->title) {
      $node->title .= '_presave';
    }
  }
}
```

---
_Drupal 7.103 · [modules/node/tests/node_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
