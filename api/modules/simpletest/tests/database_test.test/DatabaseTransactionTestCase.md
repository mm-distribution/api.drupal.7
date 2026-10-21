# DatabaseTransactionTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/database_test.test`](_file.md), lines 3719–4200 · [local source](../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3719-L4200)
- **Module/theme:** batch_test

## Signature

```php
class DatabaseTransactionTestCase extends DatabaseTestCase
```

## Documentation

```text
Test transaction support, particularly nesting.

We test nesting by having two transaction layers, an outer and inner. The
outer layer encapsulates the inner layer. Our transaction nesting abstraction
should allow the outer layer function to call any function it wants,
especially the inner layer that starts its own transaction, and be
confident that, when the function it calls returns, its own transaction
is still "alive."

Call structure:
  transactionOuterLayer()
    Start transaction
    transactionInnerLayer()
      Start transaction (does nothing in database)
      [Maybe decide to roll back]
    Do more stuff
    Should still be in transaction A
```

## Methods (derived index)

- [getInfo()](DatabaseTransactionTestCase/getInfo.md)
- [transactionOuterLayer()](DatabaseTransactionTestCase/transactionOuterLayer.md) — Helper method for transaction unit test.
- [transactionInnerLayer()](DatabaseTransactionTestCase/transactionInnerLayer.md) — Helper method for transaction unit tests. This "inner layer" transaction is either used alone or nested inside of the "outer layer" transaction.
- [testTransactionRollBackSupported()](DatabaseTransactionTestCase/testTransactionRollBackSupported.md) — Test transaction rollback on a database that supports transactions.
- [testTransactionRollBackNotSupported()](DatabaseTransactionTestCase/testTransactionRollBackNotSupported.md) — Test transaction rollback on a database that does not support transactions.
- [testCommittedTransaction()](DatabaseTransactionTestCase/testCommittedTransaction.md) — Test committed transaction.
- [testTransactionWithDdlStatement()](DatabaseTransactionTestCase/testTransactionWithDdlStatement.md) — Test the compatibility of transactions with DDL statements.
- [rollBackWithoutTransactionErrorHandler()](DatabaseTransactionTestCase/rollBackWithoutTransactionErrorHandler.md) — Special handling of "rollback without transaction" errors.
- [insertRow()](DatabaseTransactionTestCase/insertRow.md) — Insert a single row into the testing table.
- [executeDDLStatement()](DatabaseTransactionTestCase/executeDDLStatement.md) — Execute a DDL statement.
- [cleanUp()](DatabaseTransactionTestCase/cleanUp.md) — Start over for a new test.
- [assertRowPresent()](DatabaseTransactionTestCase/assertRowPresent.md) — Assert that a given row is present in the test table.
- [assertRowAbsent()](DatabaseTransactionTestCase/assertRowAbsent.md) — Assert that a given row is absent from the test table.
- [testTransactionStacking()](DatabaseTransactionTestCase/testTransactionStacking.md) — Test transaction stacking and commit / rollback.

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
