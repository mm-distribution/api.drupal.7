# DatabaseMergeTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/database_test.test`](_file.md), lines 1215–1421 · [local source](../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1215-L1421)
- **Module/theme:** batch_test

## Signature

```php
class DatabaseMergeTestCase extends DatabaseTestCase
```

## Documentation

```text
Test the MERGE query builder.
```

## Methods (derived index)

- [getInfo()](DatabaseMergeTestCase/getInfo.md)
- [testMergeInsert()](DatabaseMergeTestCase/testMergeInsert.md) — Confirm that we can merge-insert a record successfully.
- [testMergeUpdate()](DatabaseMergeTestCase/testMergeUpdate.md) — Confirm that we can merge-update a record successfully.
- [testMergeUpdateExcept()](DatabaseMergeTestCase/testMergeUpdateExcept.md) — Confirm that we can merge-update a record successfully, with different insert and update.
- [testMergeUpdateExplicit()](DatabaseMergeTestCase/testMergeUpdateExplicit.md) — Confirm that we can merge-update a record successfully, with alternate replacement.
- [testMergeUpdateExpression()](DatabaseMergeTestCase/testMergeUpdateExpression.md) — Confirm that we can merge-update a record successfully, with expressions.
- [testMergeInsertWithoutUpdate()](DatabaseMergeTestCase/testMergeInsertWithoutUpdate.md) — Test that we can merge-insert without any update fields.
- [testMergeUpdateWithoutUpdate()](DatabaseMergeTestCase/testMergeUpdateWithoutUpdate.md) — Confirm that we can merge-update without any update fields.
- [testInvalidMerge()](DatabaseMergeTestCase/testInvalidMerge.md) — Test that an invalid merge query throws an exception like it is supposed to.

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
