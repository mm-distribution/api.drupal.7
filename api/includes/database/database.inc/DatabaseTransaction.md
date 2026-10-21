# DatabaseTransaction

- **Type:** Class
- **File:** [`includes/database/database.inc`](_file.md), lines 1975–2047 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1975-L2047)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
class DatabaseTransaction
```

## Documentation

```text
A wrapper class for creating and managing database transactions.

Not all databases or database configurations support transactions. For
example, MySQL MyISAM tables do not. It is also easy to begin a transaction
and then forget to commit it, which can lead to connection errors when
another transaction is started.

This class acts as a wrapper for transactions. To begin a transaction,
simply instantiate it. When the object goes out of scope and is destroyed
it will automatically commit. It also will check to see if the specified
connection supports transactions. If not, it will simply skip any transaction
commands, allowing user-space code to proceed normally. The only difference
is that rollbacks won't actually do anything.

In the vast majority of cases, you should not instantiate this class
directly. Instead, call ->startTransaction(), from the appropriate connection
object.
```

## Properties

### $connection

```php
protected $connection;
```

```text
The connection object for this transaction.

@var DatabaseConnection
```

### $rolledBack

```php
protected $rolledBack = FALSE;
```

```text
A boolean value to indicate whether this transaction has been rolled back.

@var Boolean
```

### $name

```php
protected $name;
```

```text
The name of the transaction.

This is used to label the transaction savepoint. It will be overridden to
'drupal_transaction' if there is no transaction depth.
```

## Methods (derived index)

- [__construct()](DatabaseTransaction/__construct.md)
- [__destruct()](DatabaseTransaction/__destruct.md)
- [name()](DatabaseTransaction/name.md) — Retrieves the name of the transaction or savepoint.
- [rollback()](DatabaseTransaction/rollback.md) — Rolls back the current transaction.

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
