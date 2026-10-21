# hook_node_load()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 557–567 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L557-L567)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_node_load($nodes, $types)
```

## Documentation

```text
Act on arbitrary nodes being loaded from the database.

This hook should be used to add information that is not in the node or node
revisions table, not to replace information that is in these tables (which
could interfere with the entity cache). For performance reasons, information
for all available nodes should be loaded in a single query where possible.

This hook is invoked during node loading, which is handled by entity_load(),
via classes NodeController and DrupalDefaultEntityController. After the node
information is read from the database or the entity cache, hook_load() is
invoked on the node's content type module, then field_attach_load_revision()
or field_attach_load() is called, then hook_entity_load() is invoked on all
implementing modules, and finally hook_node_load() is invoked on all
implementing modules.

@param $nodes
  An array of the nodes being loaded, keyed by nid.
@param $types
  An array containing the node types present in $nodes. Allows for an early
  return for modules that only support certain node types. However, if your
  module defines a content type, you can use hook_load() to respond to
  loading of just that content type.

For a detailed usage example, see nodeapi_example.module.

@ingroup node_api_hooks
```

## Code

```php
function hook_node_load($nodes, $types) {
  // Decide whether any of $types are relevant to our purposes.
  if (count(array_intersect($types_we_want_to_process, $types))) {
    // Gather our extra data for each of these nodes.
    $result = db_query('SELECT nid, foo FROM {mytable} WHERE nid IN(:nids)', array(':nids' => array_keys($nodes)));
    // Add our extra data to the node objects.
    foreach ($result as $record) {
      $nodes[$record->nid]->foo = $record->foo;
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_load()".

- [entity_crud_hook_test_node_load()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_node_load.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [book_node_load()](../../book/book.module/book_node_load.md) — `modules/book/book.module`
- [comment_node_load()](../../comment/comment.module/comment_node_load.md) — `modules/comment/comment.module`
- [forum_node_load()](../../forum/forum.module/forum_node_load.md) — `modules/forum/forum.module`
- [node_access_test_node_load()](../tests/node_access_test.module/node_access_test_node_load.md) — `modules/node/tests/node_access_test.module`
- [node_test_node_load()](../tests/node_test.module/node_test_node_load.md) — `modules/node/tests/node_test.module`
- [user_node_load()](../../user/user.module/user_node_load.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
