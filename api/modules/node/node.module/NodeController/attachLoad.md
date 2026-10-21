# NodeController::attachLoad()

- **Type:** Method
- **File:** [`modules/node/node.module`](../_file.md), lines 4159–4179 · [local source](../../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L4159-L4179)
- **Class:** [NodeController](../NodeController.md)
- **Module/theme:** node

## Signature

```php
protected function attachLoad(&$nodes, $revision_id = FALSE)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function attachLoad(&$nodes, $revision_id = FALSE) {
    // Create an array of nodes for each content type and pass this to the
    // object type specific callback.
    $typed_nodes = array();
    foreach ($nodes as $id => $entity) {
      $typed_nodes[$entity->type][$id] = $entity;
    }

    // Call object type specific callbacks on each typed array of nodes.
    foreach ($typed_nodes as $node_type => $nodes_of_type) {
      if (node_hook($node_type, 'load')) {
        $function = node_type_get_base($node_type) . '_load';
        $function($nodes_of_type);
      }
    }
    // Besides the list of nodes, pass one additional argument to
    // hook_node_load(), containing a list of node types that were loaded.
    $argument = array_keys($typed_nodes);
    $this->hookLoadArguments = array($argument);
    parent::attachLoad($nodes, $revision_id);
  }
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
