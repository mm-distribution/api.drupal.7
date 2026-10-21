# hook_node_delete()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 475–479 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L475-L479)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_node_delete($node)
```

## Documentation

```text
Respond to node deletion.

This hook is invoked from node_delete_multiple() after the type-specific
hook_delete() has been invoked, but before hook_entity_delete and
field_attach_delete() are called, and before the node is removed from the
node table in the database.

@param $node
  The node that is being deleted.

@ingroup node_api_hooks
```

## Code

```php
function hook_node_delete($node) {
  db_delete('mytable')
    ->condition('nid', $node->nid)
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_delete()".

- [entity_crud_hook_test_node_delete()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_node_delete.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [book_node_delete()](../../book/book.module/book_node_delete.md) — `modules/book/book.module`
- [comment_node_delete()](../../comment/comment.module/comment_node_delete.md) — `modules/comment/comment.module`
- [forum_node_delete()](../../forum/forum.module/forum_node_delete.md) — `modules/forum/forum.module`
- [menu_node_delete()](../../menu/menu.module/menu_node_delete.md) — `modules/menu/menu.module`
- [node_access_test_node_delete()](../tests/node_access_test.module/node_access_test_node_delete.md) — `modules/node/tests/node_access_test.module`
- [path_node_delete()](../../path/path.module/path_node_delete.md) — `modules/path/path.module`
- [statistics_node_delete()](../../statistics/statistics.module/statistics_node_delete.md) — `modules/statistics/statistics.module`
- [taxonomy_node_delete()](../../taxonomy/taxonomy.module/taxonomy_node_delete.md) — `modules/taxonomy/taxonomy.module`
- [tracker_node_delete()](../../tracker/tracker.module/tracker_node_delete.md) — `modules/tracker/tracker.module`
- [translation_node_delete()](../../translation/translation.module/translation_node_delete.md) — `modules/translation/translation.module`
- [trigger_node_delete()](../../trigger/trigger.module/trigger_node_delete.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
