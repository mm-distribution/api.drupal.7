# flood_clear_event()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1375–1383 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1375-L1383)

## Signature

```php
function flood_clear_event($name, $identifier = NULL)
```

## Documentation

```text
Makes the flood control mechanism forget an event for the current visitor.

@param $name
  The name of an event.
@param $identifier
  Optional identifier (defaults to the current user's IP address).
```

## Code

```php
function flood_clear_event($name, $identifier = NULL) {
  if (!isset($identifier)) {
    $identifier = ip_address();
  }
  db_delete('flood')
    ->condition('event', $name)
    ->condition('identifier', $identifier)
    ->execute();
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
