# DatabaseConnection::getKey()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 593–595 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L593-L595)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function getKey()
```

## Documentation

```text
Returns the key this connection is associated with.

@return
  The key of this connection.
```

## Code

```php
  public function getKey() {
    return $this->key;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
