# DatabaseUpdateTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/database_test.test`](_file.md), lines 828–959 · [local source](../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L828-L959)
- **Module/theme:** batch_test

## Signature

```php
class DatabaseUpdateTestCase extends DatabaseTestCase
```

## Documentation

```text
Update builder tests.
```

## Methods (derived index)

- [getInfo()](DatabaseUpdateTestCase/getInfo.md)
- [testSimpleUpdate()](DatabaseUpdateTestCase/testSimpleUpdate.md) — Confirm that we can update a single record successfully.
- [testSimpleNullUpdate()](DatabaseUpdateTestCase/testSimpleNullUpdate.md) — Confirm updating to NULL.
- [testMultiUpdate()](DatabaseUpdateTestCase/testMultiUpdate.md) — Confirm that we can update a multiple records successfully.
- [testMultiGTUpdate()](DatabaseUpdateTestCase/testMultiGTUpdate.md) — Confirm that we can update a multiple records with a non-equality condition.
- [testWhereUpdate()](DatabaseUpdateTestCase/testWhereUpdate.md) — Confirm that we can update a multiple records with a where call.
- [testWhereAndConditionUpdate()](DatabaseUpdateTestCase/testWhereAndConditionUpdate.md) — Confirm that we can stack condition and where calls.
- [testExpressionUpdate()](DatabaseUpdateTestCase/testExpressionUpdate.md) — Test updating with expressions.

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
