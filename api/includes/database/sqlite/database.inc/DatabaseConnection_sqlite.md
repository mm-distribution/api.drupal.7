# DatabaseConnection_sqlite

- **Type:** Class
- **File:** [`includes/database/sqlite/database.inc`](_file.md), lines 18–416 · [local source](../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L18-L416)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
class DatabaseConnection_sqlite extends DatabaseConnection
```

## Documentation

```text
Specific SQLite implementation of DatabaseConnection.
```

## Properties

### $savepointSupport

```php
protected $savepointSupport = FALSE;
```

```text
Whether this database connection supports savepoints.

Version of sqlite lower then 3.6.8 can't use savepoints.
See http://www.sqlite.org/releaselog/3_6_8.html

@var boolean
```

### $willRollback

```php
protected $willRollback;
```

```text
Whether or not the active transaction (if any) will be rolled back.

@var boolean
```

### $attachedDatabases

```php
protected $attachedDatabases = array();
```

```text
All databases attached to the current database. This is used to allow
prefixes to be safely handled without locking the table

@var array
```

### $tableDropped

```php
var $tableDropped = FALSE;
```

```text
Whether or not a table has been dropped this request: the destructor will
only try to get rid of unnecessary databases if there is potential of them
being empty.

This variable is set to public because DatabaseSchema_sqlite needs to
access it. However, it should not be manually set.

@var boolean
```

## Methods (derived index)

- [__construct()](DatabaseConnection_sqlite/__construct.md)
- [__destruct()](DatabaseConnection_sqlite/__destruct.md) — Destructor for the SQLite connection.
- [getAttachedDatabases()](DatabaseConnection_sqlite/getAttachedDatabases.md) — Gets all the attached databases.
- [sqlFunctionIf()](DatabaseConnection_sqlite/sqlFunctionIf.md) — SQLite compatibility implementation for the IF() SQL function.
- [sqlFunctionGreatest()](DatabaseConnection_sqlite/sqlFunctionGreatest.md) — SQLite compatibility implementation for the GREATEST() SQL function.
- [sqlFunctionConcat()](DatabaseConnection_sqlite/sqlFunctionConcat.md) — SQLite compatibility implementation for the CONCAT() SQL function.
- [sqlFunctionSubstring()](DatabaseConnection_sqlite/sqlFunctionSubstring.md) — SQLite compatibility implementation for the SUBSTRING() SQL function.
- [sqlFunctionSubstringIndex()](DatabaseConnection_sqlite/sqlFunctionSubstringIndex.md) — SQLite compatibility implementation for the SUBSTRING_INDEX() SQL function.
- [sqlFunctionRand()](DatabaseConnection_sqlite/sqlFunctionRand.md) — SQLite compatibility implementation for the RAND() SQL function.
- [prepare()](DatabaseConnection_sqlite/prepare.md) — SQLite-specific implementation of DatabaseConnection::prepare().
- [PDOPrepare()](DatabaseConnection_sqlite/PDOPrepare.md) — NEVER CALL THIS FUNCTION: YOU MIGHT DEADLOCK YOUR PHP PROCESS.
- [queryRange()](DatabaseConnection_sqlite/queryRange.md)
- [queryTemporary()](DatabaseConnection_sqlite/queryTemporary.md)
- [driver()](DatabaseConnection_sqlite/driver.md)
- [databaseType()](DatabaseConnection_sqlite/databaseType.md)
- [mapConditionOperator()](DatabaseConnection_sqlite/mapConditionOperator.md)
- [prepareQuery()](DatabaseConnection_sqlite/prepareQuery.md)
- [nextId()](DatabaseConnection_sqlite/nextId.md)
- [rollback()](DatabaseConnection_sqlite/rollback.md)
- [pushTransaction()](DatabaseConnection_sqlite/pushTransaction.md)
- [popTransaction()](DatabaseConnection_sqlite/popTransaction.md)
- [utf8mb4IsActive()](DatabaseConnection_sqlite/utf8mb4IsActive.md)
- [utf8mb4IsSupported()](DatabaseConnection_sqlite/utf8mb4IsSupported.md)

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
