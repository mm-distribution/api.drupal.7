# SelectQueryExtender::extend()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 666–671 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L666-L671)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function extend($extender_name)
```

## Documentation

_No docblock in source._

## Code

```php
  public function extend($extender_name) {
    // The extender can be anywhere so this needs to go to the registry, which
    // is surely loaded by now.
    $class = $this->connection->getDriverClass($extender_name, array(), TRUE);
    return new $class($this, $this->connection);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
