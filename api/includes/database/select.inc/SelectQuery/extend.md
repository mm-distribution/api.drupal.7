# SelectQuery::extend()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1170–1176 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1170-L1176)
- **Class:** [SelectQuery](../SelectQuery.md)
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
    $override_class = $extender_name . '_' . $this->connection->driver();
    if (class_exists($override_class)) {
      $extender_name = $override_class;
    }
    return new $extender_name($this, $this->connection);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
