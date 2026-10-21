# ConnectionUnitTest

- **Type:** Class
- **File:** [`modules/simpletest/tests/database_test.test`](_file.md), lines 4279–4495 · [local source](../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4279-L4495)
- **Module/theme:** batch_test

## Signature

```php
class ConnectionUnitTest extends DrupalUnitTestCase
```

## Documentation

```text
Tests management of database connections.
```

## Properties

### $key

```php
protected $key;
```

### $target

```php
protected $target;
```

### $originalTarget

```php
protected $originalTarget;
```

### $monitor

```php
protected $monitor;
```

### $originalCount

```php
protected $originalCount;
```

### $skipTest

```php
protected $skipTest;
```

## Methods (derived index)

- [getInfo()](ConnectionUnitTest/getInfo.md)
- [setUp()](ConnectionUnitTest/setUp.md)
- [addConnection()](ConnectionUnitTest/addConnection.md) — Adds a new database connection info to Database.
- [getConnectionID()](ConnectionUnitTest/getConnectionID.md) — Returns the connection ID of the current test connection.
- [assertConnection()](ConnectionUnitTest/assertConnection.md) — Asserts that a connection ID exists.
- [assertNoConnection()](ConnectionUnitTest/assertNoConnection.md) — Asserts that a connection ID does not exist.
- [testOpenClose()](ConnectionUnitTest/testOpenClose.md) — Tests Database::closeConnection() without query.
- [testOpenQueryClose()](ConnectionUnitTest/testOpenQueryClose.md) — Tests Database::closeConnection() with a query.
- [testOpenQueryPrefetchClose()](ConnectionUnitTest/testOpenQueryPrefetchClose.md) — Tests Database::closeConnection() with a query and custom prefetch method.
- [testOpenSelectQueryClose()](ConnectionUnitTest/testOpenSelectQueryClose.md) — Tests Database::closeConnection() with a select query.

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
