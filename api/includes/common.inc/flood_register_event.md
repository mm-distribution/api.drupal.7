# flood_register_event()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1353–1365 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1353-L1365)

## Signature

```php
function flood_register_event($name, $window = 3600, $identifier = NULL)
```

## Documentation

```text
Registers an event for the current visitor to the flood control mechanism.

@param $name
  The name of an event.
@param $window
  Optional number of seconds before this event expires. Defaults to 3600 (1
  hour). Typically uses the same value as the flood_is_allowed() $window
  parameter. Expired events are purged on cron run to prevent the flood table
  from growing indefinitely.
@param $identifier
  Optional identifier (defaults to the current user's IP address).
```

## Code

```php
function flood_register_event($name, $window = 3600, $identifier = NULL) {
  if (!isset($identifier)) {
    $identifier = ip_address();
  }
  db_insert('flood')
    ->fields(array(
      'event' => $name,
      'identifier' => $identifier,
      'timestamp' => REQUEST_TIME,
      'expiration' => REQUEST_TIME + $window,
    ))
    ->execute();
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
