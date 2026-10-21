# hook_node_insert()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 520–527 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L520-L527)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_node_insert($node)
```

## Documentation

```text
Respond to creation of a new node.

This hook is invoked from node_save() after the database query that will
insert the node into the node table is scheduled for execution, after the
type-specific hook_insert() is invoked, and after field_attach_insert() is
called.

Note that when this hook is invoked, the changes have not yet been written to
the database, because a database transaction is still in progress. The
transaction is not finalized until the save operation is entirely completed
and node_save() goes out of scope. You should not rely on data in the
database at this time as it is not updated yet. You should also note that any
write/update database queries executed from this hook are also not committed
immediately. Check node_save() and db_transaction() for more info.

@param $node
  The node that is being created.

@ingroup node_api_hooks
```

## Code

```php
function hook_node_insert($node) {
  db_insert('mytable')
    ->fields(array(
      'nid' => $node->nid,
      'extra' => $node->extra,
    ))
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_insert()".

- [entity_crud_hook_test_node_insert()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_node_insert.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [book_node_insert()](../../book/book.module/book_node_insert.md) — `modules/book/book.module`
- [comment_node_insert()](../../comment/comment.module/comment_node_insert.md) — `modules/comment/comment.module`
- [forum_node_insert()](../../forum/forum.module/forum_node_insert.md) — `modules/forum/forum.module`
- [menu_node_insert()](../../menu/menu.module/menu_node_insert.md) — `modules/menu/menu.module`
- [node_access_test_node_insert()](../tests/node_access_test.module/node_access_test_node_insert.md) — `modules/node/tests/node_access_test.module`
- [node_test_exception_node_insert()](../tests/node_test_exception.module/node_test_exception_node_insert.md) — `modules/node/tests/node_test_exception.module`
- [node_test_node_insert()](../tests/node_test.module/node_test_node_insert.md) — `modules/node/tests/node_test.module`
- [path_node_insert()](../../path/path.module/path_node_insert.md) — `modules/path/path.module`
- [taxonomy_node_insert()](../../taxonomy/taxonomy.module/taxonomy_node_insert.md) — `modules/taxonomy/taxonomy.module`
- [tracker_node_insert()](../../tracker/tracker.module/tracker_node_insert.md) — `modules/tracker/tracker.module`
- [translation_node_insert()](../../translation/translation.module/translation_node_insert.md) — `modules/translation/translation.module`
- [translation_test_node_insert()](../../translation/tests/translation_test.module/translation_test_node_insert.md) — `modules/translation/tests/translation_test.module`
- [trigger_node_insert()](../../trigger/trigger.module/trigger_node_insert.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
