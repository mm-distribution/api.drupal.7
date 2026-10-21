# DatabaseConnection

- **Type:** Class
- **File:** [`includes/database/database.inc`](_file.md), lines 187–1419 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L187-L1419)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
abstract class DatabaseConnection
```

## Documentation

```text
Base Database API class.

This class provides a Drupal-specific extension of the PDO database
abstraction class in PHP. Every database driver implementation must provide a
concrete implementation of it to support special handling required by that
database.

@see http://php.net/manual/book.pdo.php
```

## Properties

### $target

```php
protected $target = NULL;
```

```text
The database target this connection is for.

We need this information for later auditing and logging.

@var string
```

### $key

```php
protected $key = NULL;
```

```text
The key representing this connection.

The key is a unique string which identifies a database connection. A
connection can be a single server or a cluster of master and slaves (use
target to pick between master and slave).

@var string
```

### $logger

```php
protected $logger = NULL;
```

```text
The current database logging object for this connection.

@var DatabaseLog
```

### $transactionLayers

```php
protected $transactionLayers = array();
```

```text
Tracks the number of "layers" of transactions currently active.

On many databases transactions cannot nest.  Instead, we track
nested calls to transactions and collapse them into a single
transaction.

@var array
```

### $driverClasses

```php
protected $driverClasses = array();
```

```text
Index of what driver-specific class to use for various operations.

@var array
```

### $statementClass

```php
protected $statementClass = 'DatabaseStatementBase';
```

```text
The name of the Statement class for this connection.

@var string
```

### $transactionSupport

```php
protected $transactionSupport = TRUE;
```

```text
Whether this database connection supports transactions.

@var bool
```

### $transactionalDDLSupport

```php
protected $transactionalDDLSupport = FALSE;
```

```text
Whether this database connection supports transactional DDL.

Set to FALSE by default because few databases support this feature.

@var bool
```

### $temporaryNameIndex

```php
protected $temporaryNameIndex = 0;
```

```text
An index used to generate unique temporary table names.

@var integer
```

### $connection

```php
protected $connection;
```

```text
The actual PDO connection.

@var \PDO
```

### $connectionOptions

```php
protected $connectionOptions = array();
```

```text
The connection information for this connection object.

@var array
```

### $schema

```php
protected $schema = NULL;
```

```text
The schema object for this connection.

@var object
```

### $prefixes

```php
protected $prefixes = array();
```

```text
The prefixes used by this database connection.

@var array
```

### $prefixSearch

```php
protected $prefixSearch = array();
```

```text
List of search values for use in prefixTables().

@var array
```

### $prefixReplace

```php
protected $prefixReplace = array();
```

```text
List of replacement values for use in prefixTables().

@var array
```

### $escapedNames

```php
protected $escapedNames = array();
```

```text
List of escaped database, table, and field names, keyed by unescaped names.

@var array
```

### $escapedAliases

```php
protected $escapedAliases = array();
```

```text
List of escaped aliases names, keyed by unescaped aliases.

@var array
```

### $unprefixedTablesMap

```php
protected $unprefixedTablesMap = array();
```

```text
List of un-prefixed table names, keyed by prefixed table names.

@var array
```

## Methods (derived index)

- [__construct()](DatabaseConnection/__construct.md)
- [__call()](DatabaseConnection/__call.md) — Proxy possible direct calls to the \PDO methods.
- [destroy()](DatabaseConnection/destroy.md) — Destroys this Connection object.
- [defaultOptions()](DatabaseConnection/defaultOptions.md) — Returns the default query options for any given query.
- [getConnectionOptions()](DatabaseConnection/getConnectionOptions.md) — Returns the connection information for this connection object.
- [setPrefix()](DatabaseConnection/setPrefix.md) — Set the list of prefixes used by this database connection.
- [prefixTables()](DatabaseConnection/prefixTables.md) — Appends a database prefix to all tables in a query.
- [tablePrefix()](DatabaseConnection/tablePrefix.md) — Find the prefix for a table.
- [getUnprefixedTablesMap()](DatabaseConnection/getUnprefixedTablesMap.md) — Gets a list of individually prefixed table names.
- [prepareQuery()](DatabaseConnection/prepareQuery.md) — Prepares a query string and returns the prepared statement.
- [setTarget()](DatabaseConnection/setTarget.md) — Tells this connection object what its target value is.
- [getTarget()](DatabaseConnection/getTarget.md) — Returns the target this connection is associated with.
- [setKey()](DatabaseConnection/setKey.md) — Tells this connection object what its key is.
- [getKey()](DatabaseConnection/getKey.md) — Returns the key this connection is associated with.
- [setLogger()](DatabaseConnection/setLogger.md) — Associates a logging object with this connection.
- [getLogger()](DatabaseConnection/getLogger.md) — Gets the current logging object for this connection.
- [makeSequenceName()](DatabaseConnection/makeSequenceName.md) — Creates the appropriate sequence name for a given table and serial field.
- [makeComment()](DatabaseConnection/makeComment.md) — Flatten an array of query comments into a single comment string.
- [filterComment()](DatabaseConnection/filterComment.md) — Sanitize a query comment string.
- [query()](DatabaseConnection/query.md) — Executes a query string against the database.
- [expandArguments()](DatabaseConnection/expandArguments.md) — Expands out shorthand placeholders.
- [getDriverClass()](DatabaseConnection/getDriverClass.md) — Gets the driver-specific override class if any for the specified class.
- [select()](DatabaseConnection/select.md) — Prepares and returns a SELECT query object.
- [insert()](DatabaseConnection/insert.md) — Prepares and returns an INSERT query object.
- [merge()](DatabaseConnection/merge.md) — Prepares and returns a MERGE query object.
- [update()](DatabaseConnection/update.md) — Prepares and returns an UPDATE query object.
- [delete()](DatabaseConnection/delete.md) — Prepares and returns a DELETE query object.
- [truncate()](DatabaseConnection/truncate.md) — Prepares and returns a TRUNCATE query object.
- [schema()](DatabaseConnection/schema.md) — Returns a DatabaseSchema object for manipulating the schema.
- [escapeTable()](DatabaseConnection/escapeTable.md) — Escapes a table name string.
- [escapeField()](DatabaseConnection/escapeField.md) — Escapes a field name string.
- [escapeAlias()](DatabaseConnection/escapeAlias.md) — Escapes an alias name string.
- [escapeLike()](DatabaseConnection/escapeLike.md) — Escapes characters that work as wildcard characters in a LIKE pattern.
- [inTransaction()](DatabaseConnection/inTransaction.md) — Determines if there is an active transaction open.
- [transactionDepth()](DatabaseConnection/transactionDepth.md) — Determines current transaction depth.
- [startTransaction()](DatabaseConnection/startTransaction.md) — Returns a new DatabaseTransaction object on this connection.
- [rollback()](DatabaseConnection/rollback.md) — Rolls back the transaction entirely or to a named savepoint.
- [pushTransaction()](DatabaseConnection/pushTransaction.md) — Increases the depth of transaction nesting.
- [popTransaction()](DatabaseConnection/popTransaction.md) — Decreases the depth of transaction nesting.
- [popCommittableTransactions()](DatabaseConnection/popCommittableTransactions.md) — Internal function: commit all the transaction layers that can commit.
- [queryRange()](DatabaseConnection/queryRange.md) — Runs a limited-range query on this database object.
- [generateTemporaryTableName()](DatabaseConnection/generateTemporaryTableName.md) — Generates a temporary table name.
- [queryTemporary()](DatabaseConnection/queryTemporary.md) — Runs a SELECT query and stores its results in a temporary table.
- [driver()](DatabaseConnection/driver.md) — Returns the type of database driver.
- [version()](DatabaseConnection/version.md) — Returns the version of the database server.
- [supportsTransactions()](DatabaseConnection/supportsTransactions.md) — Determines if this driver supports transactions.
- [supportsTransactionalDDL()](DatabaseConnection/supportsTransactionalDDL.md) — Determines if this driver supports transactional DDL.
- [databaseType()](DatabaseConnection/databaseType.md) — Returns the name of the PDO driver for this connection.
- [mapConditionOperator()](DatabaseConnection/mapConditionOperator.md) — Gets any special processing requirements for the condition operator.
- [commit()](DatabaseConnection/commit.md) — Throws an exception to deny direct access to transaction commits.
- [nextId()](DatabaseConnection/nextId.md) — Retrieves an unique id from a given sequence.
- [utf8mb4IsConfigurable()](DatabaseConnection/utf8mb4IsConfigurable.md) — Checks whether utf8mb4 support is configurable in settings.php.
- [utf8mb4IsActive()](DatabaseConnection/utf8mb4IsActive.md) — Checks whether utf8mb4 support is currently active.
- [utf8mb4IsSupported()](DatabaseConnection/utf8mb4IsSupported.md) — Checks whether utf8mb4 support is available on the current database system.

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
