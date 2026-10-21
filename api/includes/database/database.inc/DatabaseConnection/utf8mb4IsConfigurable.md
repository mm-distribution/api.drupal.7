# DatabaseConnection::utf8mb4IsConfigurable()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1392–1396 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1392-L1396)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function utf8mb4IsConfigurable()
```

## Documentation

```text
Checks whether utf8mb4 support is configurable in settings.php.

@return bool
```

## Code

```php
  public function utf8mb4IsConfigurable() {
    // Since 4 byte UTF-8 is not supported by default, there is nothing to
    // configure.
    return FALSE;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
