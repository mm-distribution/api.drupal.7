# db_ignore_slave()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 3163–3175 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L3163-L3175)

## Signature

```php
function db_ignore_slave()
```

## Documentation

```text
Sets a session variable specifying the lag time for ignoring a slave server.
```

## Code

```php
function db_ignore_slave() {
  $connection_info = Database::getConnectionInfo();
  // Only set ignore_slave_server if there are slave servers being used, which
  // is assumed if there are more than one.
  if (count($connection_info) > 1) {
    // Five minutes is long enough to allow the slave to break and resume
    // interrupted replication without causing problems on the Drupal site from
    // the old data.
    $duration = variable_get('maximum_replication_lag', 300);
    // Set session variable with amount of time to delay before using slave.
    $_SESSION['ignore_slave_server'] = REQUEST_TIME + $duration;
  }
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
