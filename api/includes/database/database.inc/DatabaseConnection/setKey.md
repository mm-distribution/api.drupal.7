# DatabaseConnection::setKey()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 581–585 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L581-L585)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function setKey($key)
```

## Documentation

```text
Tells this connection object what its key is.

@param $target
  The key this connection is for.
```

## Code

```php
  public function setKey($key) {
    if (!isset($this->key)) {
      $this->key = $key;
    }
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
