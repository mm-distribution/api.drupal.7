# _update_cache_clear()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 850–868 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L850-L868)
- **Module/theme:** update
- **Topics:** [update_status_cache](../../../topics/update_status_cache.md)

## Signature

```php
function _update_cache_clear($cid = NULL, $wildcard = FALSE)
```

## Documentation

```text
Invalidates cached data relating to update status.

@param $cid
  (optional) Cache ID of the record to clear from the private update module
  cache. If empty, all records will be cleared from the table except fetch
  tasks. Defaults to NULL.
@param $wildcard
  (optional) If TRUE, cache IDs starting with $cid are deleted in addition to
  the exact cache ID specified by $cid. Defaults to FALSE.
```

## Code

```php
function _update_cache_clear($cid = NULL, $wildcard = FALSE) {
  if (empty($cid)) {
    db_delete('cache_update')
      // Clear everything except fetch task information because these are used
      // to ensure that the fetch task queue items are not added multiple times.
      ->condition('cid', 'fetch_task::%', 'NOT LIKE')
      ->execute();
  }
  else {
    $query = db_delete('cache_update');
    if ($wildcard) {
      $query->condition('cid', $cid . '%', 'LIKE');
    }
    else {
      $query->condition('cid', $cid);
    }
    $query->execute();
  }
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
