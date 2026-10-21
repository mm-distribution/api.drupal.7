# Query::__wakeup()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 352–354 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L352-L354)
- **Class:** [Query](../Query.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __wakeup()
```

## Documentation

```text
Implements the magic __wakeup function to reconnect to the database.
```

## Code

```php
  public function __wakeup() {
    $this->connection = Database::getConnection($this->connectionTarget, $this->connectionKey);
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
