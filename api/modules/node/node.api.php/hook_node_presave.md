# hook_node_presave()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 687–694 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L687-L694)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_node_presave($node)
```

## Documentation

```text
Act on a node being inserted or updated.

This hook is invoked from node_save() before the node is saved to the
database.

@param $node
  The node that is being inserted or updated.

@ingroup node_api_hooks
```

## Code

```php
function hook_node_presave($node) {
  if ($node->nid && $node->moderate) {
    // Reset votes when node is updated:
    $node->score = 0;
    $node->users = '';
    $node->votes = 0;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_presave()".

- [entity_crud_hook_test_node_presave()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_node_presave.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [book_node_presave()](../../book/book.module/book_node_presave.md) — `modules/book/book.module`
- [forum_node_presave()](../../forum/forum.module/forum_node_presave.md) — `modules/forum/forum.module`
- [node_test_node_presave()](../tests/node_test.module/node_test_node_presave.md) — `modules/node/tests/node_test.module`
- [trigger_node_presave()](../../trigger/trigger.module/trigger_node_presave.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
