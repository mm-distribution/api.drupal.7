# DatabaseConnection::getConnectionOptions()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 440–442 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L440-L442)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function getConnectionOptions()
```

## Documentation

```text
Returns the connection information for this connection object.

Note that Database::getConnectionInfo() is for requesting information
about an arbitrary database connection that is defined. This method
is for requesting the connection information of this specific
open connection object.

@return
  An array of the connection information. The exact list of
  properties is driver-dependent.
```

## Code

```php
  public function getConnectionOptions() {
    return $this->connectionOptions;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
