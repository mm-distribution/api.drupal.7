# node_access_rebuild()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3625–3674 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3625-L3674)
- **Module/theme:** node
- **Topics:** [node_access](../../../topics/node_access.md)

## Signature

```php
function node_access_rebuild($batch_mode = FALSE)
```

## Documentation

```text
Rebuilds the node access database.

This is occasionally needed by modules that make system-wide changes to
access levels. When the rebuild is required by an admin-triggered action (e.g
module settings form), calling node_access_needs_rebuild(TRUE) instead of
node_access_rebuild() lets the user perform his changes and actually
rebuild only once he is done.

Note: As of Drupal 6, node access modules are not required to (and actually
should not) call node_access_rebuild() in hook_enable/disable anymore.

@see node_access_needs_rebuild()

@param $batch_mode
  Set to TRUE to process in 'batch' mode, spawning processing over several
  HTTP requests (thus avoiding the risk of PHP timeout if the site has a
  large number of nodes).
  hook_update_N and any form submit handler are safe contexts to use the
  'batch mode'. Less decidable cases (such as calls from hook_user,
  hook_taxonomy, etc...) might consider using the non-batch mode.
```

## Code

```php
function node_access_rebuild($batch_mode = FALSE) {
  db_delete('node_access')->execute();
  // Only recalculate if the site is using a node_access module.
  if (count(module_implements('node_grants'))) {
    if ($batch_mode) {
      $batch = array(
        'title' => t('Rebuilding content access permissions'),
        'operations' => array(
          array('_node_access_rebuild_batch_operation', array()),
        ),
        'finished' => '_node_access_rebuild_batch_finished'
      );
      batch_set($batch);
    }
    else {
      // Try to allocate enough time to rebuild node grants
      drupal_set_time_limit(240);

      // Rebuild newest nodes first so that recent content becomes available quickly.
      $nids = db_query("SELECT nid FROM {node} ORDER BY nid DESC")->fetchCol();
      foreach ($nids as $nid) {
        $node = node_load($nid, NULL, TRUE);
        // To preserve database integrity, only acquire grants if the node
        // loads successfully.
        if (!empty($node)) {
          node_access_acquire_grants($node);
        }
      }
    }
  }
  else {
    // Not using any node_access modules. Add the default grant.
    db_insert('node_access')
      ->fields(array(
        'nid' => 0,
        'realm' => 'all',
        'gid' => 0,
        'grant_view' => 1,
        'grant_update' => 0,
        'grant_delete' => 0,
      ))
      ->execute();
  }

  if (!isset($batch)) {
    drupal_set_message(t('Content permissions have been rebuilt.'));
    node_access_needs_rebuild(FALSE);
    cache_clear_all();
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
