# hook_load()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 1211–1216 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L1211-L1216)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_load($nodes)
```

## Documentation

```text
Act on nodes being loaded from the database.

This is a node-type-specific hook, which is invoked only for the node type
being affected. See
@link node_api_hooks Node API hooks @endlink for more information.

Use hook_node_load() to respond to node load of all node types.

This hook is invoked during node loading, which is handled by entity_load(),
via classes NodeController and DrupalDefaultEntityController. After the node
information is read from the database or the entity cache, hook_load() is
invoked on the node's content type module, then field_attach_node_revision()
or field_attach_load() is called, then hook_entity_load() is invoked on all
implementing modules, and finally hook_node_load() is invoked on all
implementing modules.

This hook should only be used to add information that is not in the node or
node revisions table, not to replace information that is in these tables
(which could interfere with the entity cache). For performance reasons,
information for all available nodes should be loaded in a single query where
possible.

@param $nodes
  An array of the nodes being loaded, keyed by nid.

For a detailed usage example, see node_example.module.

@ingroup node_api_hooks
```

## Code

```php
function hook_load($nodes) {
  $result = db_query('SELECT nid, foo FROM {mytable} WHERE nid IN (:nids)', array(':nids' => array_keys($nodes)));
  foreach ($result as $record) {
    $nodes[$record->nid]->foo = $record->foo;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_load()".

- [poll_load()](../../poll/poll.module/poll_load.md) — `modules/poll/poll.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
