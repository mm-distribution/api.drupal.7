# taxonomy_update_7011()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.install`](_file.md), lines 907–935 · [local source](../../../../source/modules/taxonomy/taxonomy.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install#L907-L935)
- **Module/theme:** taxonomy
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function taxonomy_update_7011(&$sandbox)
```

## Documentation

```text
Drop unpublished nodes from the index.
```

## Code

```php
function taxonomy_update_7011(&$sandbox) {
  // Initialize information needed by the batch update system.
  if (!isset($sandbox['progress'])) {
    $sandbox['progress'] = 0;
    $sandbox['max'] = db_query('SELECT COUNT(DISTINCT n.nid) FROM {node} n INNER JOIN {taxonomy_index} t ON n.nid = t.nid WHERE n.status = :status', array(':status' => NODE_NOT_PUBLISHED))->fetchField();
    // If there's no data, don't bother with the extra work.
    if (empty($sandbox['max'])) {
      return;
    }
  }

  // Process records in groups of 5000.
  $limit = 5000;
  $nids = db_query_range('SELECT DISTINCT n.nid FROM {node} n INNER JOIN {taxonomy_index} t ON n.nid = t.nid WHERE n.status = :status', 0, $limit, array(':status' => NODE_NOT_PUBLISHED))->fetchCol();
  if (!empty($nids)) {
    db_delete('taxonomy_index')
      ->condition('nid', $nids)
      ->execute();
  }

  // Update our progress information for the batch update.
  $sandbox['progress'] += $limit;

  // Indicate our current progress to the batch update system, if the update is
  // not yet complete.
  if ($sandbox['progress'] < $sandbox['max']) {
    $sandbox['#finished'] = $sandbox['progress'] / $sandbox['max'];
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.install](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install) · Licensed GPL-2.0-or-later (see LICENSE)._
