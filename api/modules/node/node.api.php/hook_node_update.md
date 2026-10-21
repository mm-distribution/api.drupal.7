# hook_node_update()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 717–722 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L717-L722)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_node_update($node)
```

## Documentation

```text
Respond to updates to a node.

This hook is invoked from node_save() after the database query that will
update node in the node table is scheduled for execution, after the
type-specific hook_update() is invoked, and after field_attach_update() is
called.

Note that when this hook is invoked, the changes have not yet been written to
the database, because a database transaction is still in progress. The
transaction is not finalized until the save operation is entirely completed
and node_save() goes out of scope. You should not rely on data in the
database at this time as it is not updated yet. You should also note that any
write/update database queries executed from this hook are also not committed
immediately. Check node_save() and db_transaction() for more info.

@param $node
  The node that is being updated.

@ingroup node_api_hooks
```

## Code

```php
function hook_node_update($node) {
  db_update('mytable')
    ->fields(array('extra' => $node->extra))
    ->condition('nid', $node->nid)
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_update()".

- [entity_crud_hook_test_node_update()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_node_update.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [book_node_update()](../../book/book.module/book_node_update.md) — `modules/book/book.module`
- [forum_node_update()](../../forum/forum.module/forum_node_update.md) — `modules/forum/forum.module`
- [menu_node_update()](../../menu/menu.module/menu_node_update.md) — `modules/menu/menu.module`
- [node_access_test_node_update()](../tests/node_access_test.module/node_access_test_node_update.md) — `modules/node/tests/node_access_test.module`
- [node_test_node_update()](../tests/node_test.module/node_test_node_update.md) — `modules/node/tests/node_test.module`
- [path_node_update()](../../path/path.module/path_node_update.md) — `modules/path/path.module`
- [search_node_update()](../../search/search.module/search_node_update.md) — `modules/search/search.module`
- [taxonomy_node_update()](../../taxonomy/taxonomy.module/taxonomy_node_update.md) — `modules/taxonomy/taxonomy.module`
- [tracker_node_update()](../../tracker/tracker.module/tracker_node_update.md) — `modules/tracker/tracker.module`
- [translation_node_update()](../../translation/translation.module/translation_node_update.md) — `modules/translation/translation.module`
- [trigger_node_update()](../../trigger/trigger.module/trigger_node_update.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
