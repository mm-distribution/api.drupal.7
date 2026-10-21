# _node_mass_update_batch_process()

- **Type:** Function
- **File:** [`modules/node/node.admin.inc`](_file.md), lines 338–364 · [local source](../../../../source/modules/node/node.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc#L338-L364)
- **Module/theme:** node

## Signature

```php
function _node_mass_update_batch_process($nodes, $updates, &$context)
```

## Documentation

```text
Implements callback_batch_operation().

Executes a batch operation for node_mass_update().

@param array $nodes
  An array of node IDs.
@param array $updates
  Associative array of updates.
@param array $context
  An array of contextual key/values.
```

## Code

```php
function _node_mass_update_batch_process($nodes, $updates, &$context) {
  if (!isset($context['sandbox']['progress'])) {
    $context['sandbox']['progress'] = 0;
    $context['sandbox']['max'] = count($nodes);
    $context['sandbox']['nodes'] = $nodes;
  }

  // Process nodes by groups of 5.
  $count = min(5, count($context['sandbox']['nodes']));
  for ($i = 1; $i <= $count; $i++) {
    // For each nid, load the node, reset the values, and save it.
    $nid = array_shift($context['sandbox']['nodes']);
    $node = _node_mass_update_helper($nid, $updates);

    // Store result for post-processing in the finished callback.
    $context['results'][] = l($node->title, 'node/' . $node->nid);

    // Update our progress information.
    $context['sandbox']['progress']++;
  }

  // Inform the batch engine that we are not finished,
  // and provide an estimation of the completion level we reached.
  if ($context['sandbox']['progress'] != $context['sandbox']['max']) {
    $context['finished'] = $context['sandbox']['progress'] / $context['sandbox']['max'];
  }
}
```

---
_Drupal 7.103 · [modules/node/node.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
