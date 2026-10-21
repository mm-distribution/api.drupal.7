# DatabaseInsertTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/database_test.test`](_file.md), lines 545–722 · [local source](../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L545-L722)
- **Module/theme:** batch_test

## Signature

```php
class DatabaseInsertTestCase extends DatabaseTestCase
```

## Documentation

```text
Test the insert builder.
```

## Methods (derived index)

- [getInfo()](DatabaseInsertTestCase/getInfo.md)
- [testSimpleInsert()](DatabaseInsertTestCase/testSimpleInsert.md) — Test the very basic insert functionality.
- [testMultiInsert()](DatabaseInsertTestCase/testMultiInsert.md) — Test that we can insert multiple records in one query object.
- [testRepeatedInsert()](DatabaseInsertTestCase/testRepeatedInsert.md) — Test that an insert object can be reused with new data after it executes.
- [testInsertFieldOnlyDefinintion()](DatabaseInsertTestCase/testInsertFieldOnlyDefinintion.md) — Test that we can specify fields without values and specify values later.
- [testInsertLastInsertID()](DatabaseInsertTestCase/testInsertLastInsertID.md) — Test that inserts return the proper auto-increment ID.
- [testInsertSelectFields()](DatabaseInsertTestCase/testInsertSelectFields.md) — Test that the INSERT INTO ... SELECT (fields) ... syntax works.
- [testInsertSelectAll()](DatabaseInsertTestCase/testInsertSelectAll.md) — Tests that the INSERT INTO ... SELECT * ... syntax works.

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
