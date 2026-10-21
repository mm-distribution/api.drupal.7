# DatabaseConnection::prefixTables()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 497–499 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L497-L499)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function prefixTables($sql)
```

## Documentation

```text
Appends a database prefix to all tables in a query.

Queries sent to Drupal should wrap all table names in curly brackets. This
function searches for this syntax and adds Drupal's table prefix to all
tables, allowing Drupal to coexist with other systems in the same database
and/or schema if necessary.

@param $sql
  A string containing a partial or entire SQL query.

@return
  The properly-prefixed string.
```

## Code

```php
  public function prefixTables($sql) {
    return str_replace($this->prefixSearch, $this->prefixReplace, $sql);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
