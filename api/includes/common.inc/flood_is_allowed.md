# flood_is_allowed()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1406–1416 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1406-L1416)

## Signature

```php
function flood_is_allowed($name, $threshold, $window = 3600, $identifier = NULL)
```

## Documentation

```text
Checks whether a user is allowed to proceed with the specified event.

Events can have thresholds saying that each user can only do that event
a certain number of times in a time window. This function verifies that the
current user has not exceeded this threshold.

@param $name
  The unique name of the event.
@param $threshold
  The maximum number of times each user can do this event per time window.
@param $window
  Number of seconds in the time window for this event (default is 3600
  seconds, or 1 hour).
@param $identifier
  Unique identifier of the current user. Defaults to their IP address.

@return
  TRUE if the user is allowed to proceed. FALSE if they have exceeded the
  threshold and should not be allowed to proceed.
```

## Code

```php
function flood_is_allowed($name, $threshold, $window = 3600, $identifier = NULL) {
  if (!isset($identifier)) {
    $identifier = ip_address();
  }
  $number = db_query("SELECT COUNT(*) FROM {flood} WHERE event = :event AND identifier = :identifier AND timestamp > :timestamp", array(
    ':event' => $name,
    ':identifier' => $identifier,
    ':timestamp' => REQUEST_TIME - $window))
    ->fetchField();
  return ($number < $threshold);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
