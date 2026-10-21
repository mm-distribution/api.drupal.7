# Database

- **Type:** Class
- **File:** [`includes/database/database.inc`](_file.md), lines 1428–1889 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1428-L1889)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
abstract class Database
```

## Documentation

```text
Primary front-controller for the database system.

This class is uninstantiatable and un-extendable. It acts to encapsulate
all control and shepherding of database connections into a single location
without the use of globals.
```

## Constants

### RETURN_NULL

```php
const RETURN_NULL = 0;
```

```text
Flag to indicate a query call should simply return NULL.

This is used for queries that have no reasonable return value anyway, such
as INSERT statements to a table without a serial primary key.
```

### RETURN_STATEMENT

```php
const RETURN_STATEMENT = 1;
```

```text
Flag to indicate a query call should return the prepared statement.
```

### RETURN_AFFECTED

```php
const RETURN_AFFECTED = 2;
```

```text
Flag to indicate a query call should return the number of affected rows.
```

### RETURN_INSERT_ID

```php
const RETURN_INSERT_ID = 3;
```

```text
Flag to indicate a query call should return the "last insert id".
```

## Properties

### $connections

```php
static protected $connections = array();
```

```text
An nested array of all active connections. It is keyed by database name
and target.

@var array
```

### $databaseInfo

```php
static protected $databaseInfo = NULL;
```

```text
A processed copy of the database connection information from settings.php.

@var array
```

### $ignoreTargets

```php
static protected $ignoreTargets = array();
```

```text
A list of key/target credentials to simply ignore.

@var array
```

### $activeKey

```php
static protected $activeKey = 'default';
```

```text
The key of the currently active database connection.

@var string
```

### $logs

```php
static protected $logs = array();
```

```text
An array of active query log objects.

Every connection has one and only one logger object for all targets and
logging keys.

array(
  '$db_key' => DatabaseLog object.
);

@var array
```

## Methods (derived index)

- [startLog()](Database/startLog.md) — Starts logging a given logging key on the specified connection.
- [getLog()](Database/getLog.md) — Retrieves the queries logged on for given logging key.
- [getConnection()](Database/getConnection.md) — Gets the connection object for the specified database key and target.
- [isActiveConnection()](Database/isActiveConnection.md) — Determines if there is an active connection.
- [setActiveConnection()](Database/setActiveConnection.md) — Sets the active connection to the specified key.
- [parseConnectionInfo()](Database/parseConnectionInfo.md) — Process the configuration file for database information.
- [addConnectionInfo()](Database/addConnectionInfo.md) — Adds database connection information for a given key/target.
- [getConnectionInfo()](Database/getConnectionInfo.md) — Gets information on the specified database connection.
- [renameConnection()](Database/renameConnection.md) — Rename a connection and its corresponding connection information.
- [removeConnection()](Database/removeConnection.md) — Remove a connection and its corresponding connection information.
- [openConnection()](Database/openConnection.md) — Opens a connection to the server specified by the given key and target.
- [closeConnection()](Database/closeConnection.md) — Closes a connection to the server specified by the given key and target.
- [ignoreTarget()](Database/ignoreTarget.md) — Instructs the system to temporarily ignore a given key/target.
- [loadDriverFile()](Database/loadDriverFile.md) — Load a file for the database that might hold a class.

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
