# update_fix_d7_block_deltas()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 355–467 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L355-L467)

## Signature

```php
function update_fix_d7_block_deltas(&$sandbox, $renamed_deltas, $moved_deltas)
```

## Documentation

```text
A helper function that modules can use to assist with the transformation
from numeric block deltas to string block deltas during the 6.x -> 7.x
upgrade.

@todo This function should be removed in 8.x.

@param $sandbox
  An array holding data for the batch process.
@param $renamed_deltas
  An associative array.  Keys are module names, values an associative array
  mapping the old block deltas to the new block deltas for the module.
  Example:
  @code
    $renamed_deltas = array(
      'mymodule' =>
        array(
          0 => 'mymodule-block-1',
          1 => 'mymodule-block-2',
        ),
    );
  @endcode
@param $moved_deltas
  An associative array. Keys are source module names, values an associative
  array mapping the (possibly renamed) block name to the new module name.
  Example:
  @code
    $moved_deltas = array(
      'user' =>
        array(
          'navigation' => 'system',
        ),
    );
  @endcode
```

## Code

```php
function update_fix_d7_block_deltas(&$sandbox, $renamed_deltas, $moved_deltas) {
  // Loop through each block and make changes to the block tables.
  // Only run this the first time through the batch update.
  if (!isset($sandbox['progress'])) {
    // Determine whether to use the old or new block table names.
    $block_tables = db_table_exists('blocks') ? array('blocks', 'blocks_roles') : array('block', 'block_role');
    foreach ($block_tables as $table) {
      foreach ($renamed_deltas as $module => $deltas) {
        foreach ($deltas as $old_delta => $new_delta) {
          // Only do the update if the old block actually exists.
          $block_exists = db_query("SELECT COUNT(*) FROM {" . $table . "} WHERE module = :module AND delta = :delta", array(
              ':module' => $module,
              ':delta' => $old_delta,
            ))
            ->fetchField();
          if ($block_exists) {
            // Delete any existing blocks with the new module+delta.
            db_delete($table)
              ->condition('module', $module)
              ->condition('delta', $new_delta)
              ->execute();
            // Rename the old block to the new module+delta.
            db_update($table)
              ->fields(array('delta' => $new_delta))
              ->condition('module', $module)
              ->condition('delta', $old_delta)
              ->execute();
          }
        }
      }
      foreach ($moved_deltas as $old_module => $deltas) {
        foreach ($deltas as $delta => $new_module) {
          // Only do the update if the old block actually exists.
          $block_exists = db_query("SELECT COUNT(*) FROM {" . $table . "} WHERE module = :module AND delta = :delta", array(
              ':module' => $old_module,
              ':delta' => $delta,
            ))
            ->fetchField();
          if ($block_exists) {
            // Delete any existing blocks with the new module+delta.
            db_delete($table)
              ->condition('module', $new_module)
              ->condition('delta', $delta)
              ->execute();
            // Rename the old block to the new module+delta.
            db_update($table)
              ->fields(array('module' => $new_module))
              ->condition('module', $old_module)
              ->condition('delta', $delta)
              ->execute();
          }
        }
      }
    }

    // Initialize batch update information.
    $sandbox['progress'] = 0;
    $sandbox['last_user_processed'] = -1;
    $sandbox['max'] = db_query("SELECT COUNT(*) FROM {users} WHERE data LIKE :block", array(
        ':block' => '%' . db_like(serialize('block')) . '%',
      ))
      ->fetchField();
  }
  // Now do the batch update of the user-specific block visibility settings.
  $limit = 100;
  $result = db_select('users', 'u')
    ->fields('u', array('uid', 'data'))
    ->condition('uid', $sandbox['last_user_processed'], '>')
    ->condition('data', '%' . db_like(serialize('block')) . '%', 'LIKE')
    ->orderBy('uid', 'ASC')
    ->range(0, $limit)
    ->execute();
  foreach ($result as $row) {
    $data = unserialize($row->data);
    $user_needs_update = FALSE;
    foreach ($renamed_deltas as $module => $deltas) {
      foreach ($deltas as $old_delta => $new_delta) {
        if (isset($data['block'][$module][$old_delta])) {
          // Transfer the old block visibility settings to the newly-renamed
          // block, and mark this user for a database update.
          $data['block'][$module][$new_delta] = $data['block'][$module][$old_delta];
          unset($data['block'][$module][$old_delta]);
          $user_needs_update = TRUE;
        }
      }
    }
    foreach ($moved_deltas as $old_module => $deltas) {
      foreach ($deltas as $delta => $new_module) {
        if (isset($data['block'][$old_module][$delta])) {
          // Transfer the old block visibility settings to the moved
          // block, and mark this user for a database update.
          $data['block'][$new_module][$delta] = $data['block'][$old_module][$delta];
          unset($data['block'][$old_module][$delta]);
          $user_needs_update = TRUE;
        }
      }
    }
    // Update the current user.
    if ($user_needs_update) {
      db_update('users')
        ->fields(array('data' => serialize($data)))
        ->condition('uid', $row->uid)
        ->execute();
    }
    // Update our progress information for the batch update.
    $sandbox['progress']++;
    $sandbox['last_user_processed'] = $row->uid;
  }
  // Indicate our current progress to the batch update system.
  if ($sandbox['progress'] < $sandbox['max']) {
    $sandbox['#finished'] = $sandbox['progress'] / $sandbox['max'];
  }
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
