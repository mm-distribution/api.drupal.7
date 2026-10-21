# node_save()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1077–1201 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1077-L1201)
- **Module/theme:** node

## Signature

```php
function node_save($node)
```

## Documentation

```text
Saves changes to a node or adds a new node.

@param $node
  The $node object to be saved. If $node->nid is
  omitted (or $node->is_new is TRUE), a new node will be added.
```

## Code

```php
function node_save($node) {
  $transaction = db_transaction();

  try {
    // Load the stored entity, if any.
    if (!empty($node->nid) && !isset($node->original)) {
      $node->original = entity_load_unchanged('node', $node->nid);
    }

    field_attach_presave('node', $node);
    global $user;

    // Determine if we will be inserting a new node.
    if (!isset($node->is_new)) {
      $node->is_new = empty($node->nid);
    }

    // Set the timestamp fields.
    if (empty($node->created)) {
      $node->created = REQUEST_TIME;
    }
    // The changed timestamp is always updated for bookkeeping purposes,
    // for example: revisions, searching, etc.
    $node->changed = REQUEST_TIME;

    $node->timestamp = REQUEST_TIME;
    $update_node = TRUE;

    // Let modules modify the node before it is saved to the database.
    module_invoke_all('node_presave', $node);
    module_invoke_all('entity_presave', $node, 'node');

    if ($node->is_new || !empty($node->revision)) {
      // When inserting either a new node or a new node revision, $node->log
      // must be set because {node_revision}.log is a text column and therefore
      // cannot have a default value. However, it might not be set at this
      // point (for example, if the user submitting a node form does not have
      // permission to create revisions), so we ensure that it is at least an
      // empty string in that case.
      // @todo: Make the {node_revision}.log column nullable so that we can
      // remove this check.
      if (!isset($node->log)) {
        $node->log = '';
      }
    }
    elseif (!isset($node->log) || $node->log === '') {
      // If we are updating an existing node without adding a new revision, we
      // need to make sure $node->log is unset whenever it is empty. As long as
      // $node->log is unset, drupal_write_record() will not attempt to update
      // the existing database column when re-saving the revision; therefore,
      // this code allows us to avoid clobbering an existing log entry with an
      // empty one.
      unset($node->log);
    }

    // When saving a new node revision, unset any existing $node->vid so as to
    // ensure that a new revision will actually be created, then store the old
    // revision ID in a separate property for use by node hook implementations.
    if (!$node->is_new && !empty($node->revision) && $node->vid) {
      $node->old_vid = $node->vid;
      unset($node->vid);
    }

    // Save the node and node revision.
    if ($node->is_new) {
      // For new nodes, save new records for both the node itself and the node
      // revision.
      drupal_write_record('node', $node);
      _node_save_revision($node, $user->uid);
      $op = 'insert';
    }
    else {
      // For existing nodes, update the node record which matches the value of
      // $node->nid.
      drupal_write_record('node', $node, 'nid');
      // Then, if a new node revision was requested, save a new record for
      // that; otherwise, update the node revision record which matches the
      // value of $node->vid.
      if (!empty($node->revision)) {
        _node_save_revision($node, $user->uid);
      }
      else {
        _node_save_revision($node, $user->uid, 'vid');
        $update_node = FALSE;
      }
      $op = 'update';
    }
    if ($update_node) {
      db_update('node')
        ->fields(array('vid' => $node->vid))
        ->condition('nid', $node->nid)
        ->execute();
    }

    // Call the node specific callback (if any). This can be
    // node_invoke($node, 'insert') or
    // node_invoke($node, 'update').
    node_invoke($node, $op);

    // Save fields.
    $function = "field_attach_$op";
    $function('node', $node);

    module_invoke_all('node_' . $op, $node);
    module_invoke_all('entity_' . $op, $node, 'node');

    // Update the node access table for this node.
    node_access_acquire_grants($node);

    // Clear internal properties.
    unset($node->is_new);
    unset($node->original);
    // Clear the static loading cache.
    entity_get_controller('node')->resetCache(array($node->nid));

    // Ignore slave server temporarily to give time for the
    // saved node to be propagated to the slave.
    db_ignore_slave();
  }
  catch (Exception $e) {
    $transaction->rollback();
    watchdog_exception('node', $e);
    throw $e;
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
