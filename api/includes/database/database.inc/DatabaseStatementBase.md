# DatabaseStatementBase

- **Type:** Class
- **File:** [`includes/database/database.inc`](_file.md), lines 2249–2339 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2249-L2339)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
class DatabaseStatementBase extends PDOStatement implements DatabaseStatementInterface
```

## Documentation

```text
Default implementation of DatabaseStatementInterface.

PDO allows us to extend the PDOStatement class to provide additional
functionality beyond that offered by default. We do need extra
functionality. By default, this class is not driver-specific. If a given
driver needs to set a custom statement class, it may do so in its
constructor.

@see http://us.php.net/pdostatement
```

## Properties

### $dbh

```php
public $dbh;
```

```text
Reference to the database connection object for this statement.

The name $dbh is inherited from PDOStatement.

@var DatabaseConnection
```

## Methods (derived index)

- [__construct()](DatabaseStatementBase/__construct.md)
- [execute()](DatabaseStatementBase/execute.md)
- [getQueryString()](DatabaseStatementBase/getQueryString.md)
- [fetchCol()](DatabaseStatementBase/fetchCol.md)
- [fetchAllAssoc()](DatabaseStatementBase/fetchAllAssoc.md)
- [fetchAllKeyed()](DatabaseStatementBase/fetchAllKeyed.md)
- [fetchField()](DatabaseStatementBase/fetchField.md)
- [fetchAssoc()](DatabaseStatementBase/fetchAssoc.md)

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
