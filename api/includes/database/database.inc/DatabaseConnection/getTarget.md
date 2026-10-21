# DatabaseConnection::getTarget()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 571–573 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L571-L573)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function getTarget()
```

## Documentation

```text
Returns the target this connection is associated with.

@return
  The target string of this connection.
```

## Code

```php
  public function getTarget() {
    return $this->target;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
