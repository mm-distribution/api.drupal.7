# DatabaseStatementPrefetch::throwPDOException()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 204–210 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L204-L210)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
protected function throwPDOException()
```

## Documentation

```text
Throw a PDO Exception based on the last PDO error.
```

## Code

```php
  protected function throwPDOException() {
    $error_info = $this->dbh->errorInfo();
    // We rebuild a message formatted in the same way as PDO.
    $exception = new PDOException("SQLSTATE[" . $error_info[0] . "]: General error " . $error_info[1] . ": " . $error_info[2]);
    $exception->errorInfo = $error_info;
    throw $exception;
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
