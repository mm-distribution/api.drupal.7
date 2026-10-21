# tracker_enable()

- **Type:** Function
- **File:** [`modules/tracker/tracker.install`](_file.md), lines 19–27 · [local source](../../../../source/modules/tracker/tracker.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.install#L19-L27)
- **Module/theme:** tracker
- **Implements:** [hook_enable()](../../system/system.api.php/hook_enable.md)

## Signature

```php
function tracker_enable()
```

## Documentation

```text
Implements hook_enable().
```

## Code

```php
function tracker_enable() {
  $max_nid = db_query('SELECT MAX(nid) FROM {node}')->fetchField();
  if ($max_nid != 0) {
    variable_set('tracker_index_nid', $max_nid);
    // To avoid timing out while attempting to do a complete indexing, we
    // simply call our cron job to remove stale records and begin the process.
    tracker_cron();
  }
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.install](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.install) · Licensed GPL-2.0-or-later (see LICENSE)._
