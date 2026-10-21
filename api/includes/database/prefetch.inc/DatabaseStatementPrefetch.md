# DatabaseStatementPrefetch

- **Type:** Class
- **File:** [`includes/database/prefetch.inc`](_file.md), lines 22–516 · [local source](../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L22-L516)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
class DatabaseStatementPrefetch implements Iterator, DatabaseStatementInterface
```

## Documentation

```text
An implementation of DatabaseStatementInterface that prefetches all data.

This class behaves very similar to a PDOStatement but as it always fetches
every row it is possible to manipulate those results.
```

## Properties

### $queryString

```php
protected $queryString;
```

```text
The query string.

@var string
```

### $driverOptions

```php
protected $driverOptions;
```

```text
Driver-specific options. Can be used by child classes.

@var Array
```

### $dbh

```php
public $dbh;
```

```text
Reference to the database connection object for this statement.

The name $dbh is inherited from PDOStatement.

@var DatabaseConnection
```

### $data

```php
protected $data = array();
```

```text
Main data store.

@var Array
```

### $currentRow

```php
protected $currentRow = NULL;
```

```text
The current row, retrieved in PDO::FETCH_ASSOC format.

@var Array
```

### $currentKey

```php
protected $currentKey = NULL;
```

```text
The key of the current row.

@var int
```

### $columnNames

```php
protected $columnNames = NULL;
```

```text
The list of column names in this result set.

@var Array
```

### $rowCount

```php
protected $rowCount = NULL;
```

```text
The number of rows affected by the last query.

@var int
```

### $resultRowCount

```php
protected $resultRowCount = 0;
```

```text
The number of rows in this result set.

@var int
```

### $fetchStyle

```php
protected $fetchStyle = PDO::FETCH_OBJ;
```

```text
Holds the current fetch style (which will be used by the next fetch).
@see PDOStatement::fetch()

@var int
```

### $fetchOptions

```php
protected $fetchOptions = array(
    'class' => 'stdClass',
    'constructor_args' => array(),
    'object' => NULL,
    'column' => 0,
  );
```

```text
Holds supplementary current fetch options (which will be used by the next fetch).

@var Array
```

### $defaultFetchStyle

```php
protected $defaultFetchStyle = PDO::FETCH_OBJ;
```

```text
Holds the default fetch style.

@var int
```

### $defaultFetchOptions

```php
protected $defaultFetchOptions = array(
    'class' => 'stdClass',
    'constructor_args' => array(),
    'object' => NULL,
    'column' => 0,
  );
```

```text
Holds supplementary default fetch options.

@var Array
```

## Methods (derived index)

- [__construct()](DatabaseStatementPrefetch/__construct.md)
- [execute()](DatabaseStatementPrefetch/execute.md) — Executes a prepared statement.
- [throwPDOException()](DatabaseStatementPrefetch/throwPDOException.md) — Throw a PDO Exception based on the last PDO error.
- [getStatement()](DatabaseStatementPrefetch/getStatement.md) — Grab a PDOStatement object from a given query and its arguments.
- [getQueryString()](DatabaseStatementPrefetch/getQueryString.md) — Return the object's SQL query string.
- [setFetchMode()](DatabaseStatementPrefetch/setFetchMode.md)
- [current()](DatabaseStatementPrefetch/current.md)
- [key()](DatabaseStatementPrefetch/key.md)
- [rewind()](DatabaseStatementPrefetch/rewind.md)
- [next()](DatabaseStatementPrefetch/next.md)
- [valid()](DatabaseStatementPrefetch/valid.md)
- [rowCount()](DatabaseStatementPrefetch/rowCount.md)
- [fetch()](DatabaseStatementPrefetch/fetch.md)
- [fetchColumn()](DatabaseStatementPrefetch/fetchColumn.md)
- [fetchField()](DatabaseStatementPrefetch/fetchField.md)
- [fetchObject()](DatabaseStatementPrefetch/fetchObject.md)
- [fetchAssoc()](DatabaseStatementPrefetch/fetchAssoc.md)
- [fetchAll()](DatabaseStatementPrefetch/fetchAll.md)
- [fetchCol()](DatabaseStatementPrefetch/fetchCol.md)
- [fetchAllKeyed()](DatabaseStatementPrefetch/fetchAllKeyed.md)
- [fetchAllAssoc()](DatabaseStatementPrefetch/fetchAllAssoc.md)

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
