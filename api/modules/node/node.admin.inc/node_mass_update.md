# node_mass_update()

- **Type:** Function
- **File:** [`modules/node/node.admin.inc`](_file.md), lines 274–300 · [local source](../../../../source/modules/node/node.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc#L274-L300)
- **Module/theme:** node

## Signature

```php
function node_mass_update($nodes, $updates)
```

## Documentation

```text
Make mass update of nodes, changing all nodes in the $nodes array
to update them with the field values in $updates.

IMPORTANT NOTE: This function is intended to work when called from a form
submission handler. Calling it outside of the form submission process may not
work correctly.

@param array $nodes
  Array of node nids to update.
@param array $updates
  Array of key/value pairs with node field names and the value to update that
  field to.
```

## Code

```php
function node_mass_update($nodes, $updates) {
  // We use batch processing to prevent timeout when updating a large number
  // of nodes.
  if (count($nodes) > 10) {
    $batch = array(
      'operations' => array(
        array('_node_mass_update_batch_process', array($nodes, $updates))
      ),
      'finished' => '_node_mass_update_batch_finished',
      'title' => t('Processing'),
      // We use a single multi-pass operation, so the default
      // 'Remaining x of y operations' message will be confusing here.
      'progress_message' => '',
      'error_message' => t('The update has encountered an error.'),
      // The operations do not live in the .module file, so we need to
      // tell the batch engine which file to load before calling them.
      'file' => drupal_get_path('module', 'node') . '/node.admin.inc',
    );
    batch_set($batch);
  }
  else {
    foreach ($nodes as $nid) {
      _node_mass_update_helper($nid, $updates);
    }
    drupal_set_message(t('The update has been performed.'));
  }
}
```

---
_Drupal 7.103 · [modules/node/node.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
