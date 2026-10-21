# poll_cron()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 174–182 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L174-L182)
- **Module/theme:** poll
- **Implements:** [hook_cron()](../../system/system.api.php/hook_cron.md)

## Signature

```php
function poll_cron()
```

## Documentation

```text
Implements hook_cron().

Closes polls that have exceeded their allowed runtime.
```

## Code

```php
function poll_cron() {
  $nids = db_query('SELECT p.nid FROM {poll} p INNER JOIN {node} n ON p.nid = n.nid WHERE (n.created + p.runtime) < :request_time AND p.active = :active AND p.runtime <> :runtime', array(':request_time' => REQUEST_TIME, ':active' => 1, ':runtime' => 0))->fetchCol();
  if (!empty($nids)) {
    db_update('poll')
      ->fields(array('active' => 0))
      ->condition('nid', $nids, 'IN')
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
