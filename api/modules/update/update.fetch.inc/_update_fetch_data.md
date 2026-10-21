# _update_fetch_data()

- **Type:** Function
- **File:** [`modules/update/update.fetch.inc`](_file.md), lines 112–119 · [local source](../../../../source/modules/update/update.fetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc#L112-L119)
- **Module/theme:** update

## Signature

```php
function _update_fetch_data()
```

## Documentation

```text
Attempts to drain the queue of tasks for release history data to fetch.
```

## Code

```php
function _update_fetch_data() {
  $queue = DrupalQueue::get('update_fetch_tasks');
  $end = time() + variable_get('update_max_fetch_time', UPDATE_MAX_FETCH_TIME);
  while (time() < $end && ($item = $queue->claimItem())) {
    _update_process_fetch_task($item->data);
    $queue->deleteItem($item);
  }
}
```

---
_Drupal 7.103 · [modules/update/update.fetch.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
