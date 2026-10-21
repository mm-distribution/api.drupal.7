# DatabaseSelectTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/database_test.test`](_file.md), lines 1426–1850 · [local source](../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1426-L1850)
- **Module/theme:** batch_test

## Signature

```php
class DatabaseSelectTestCase extends DatabaseTestCase
```

## Documentation

```text
Test the SELECT builder.
```

## Methods (derived index)

- [getInfo()](DatabaseSelectTestCase/getInfo.md)
- [testSimpleSelect()](DatabaseSelectTestCase/testSimpleSelect.md) — Test rudimentary SELECT statements.
- [testSimpleComment()](DatabaseSelectTestCase/testSimpleComment.md) — Test rudimentary SELECT statement with a COMMENT.
- [testVulnerableComment()](DatabaseSelectTestCase/testVulnerableComment.md) — Test query COMMENT system against vulnerabilities.
- [makeCommentsProvider()](DatabaseSelectTestCase/makeCommentsProvider.md) — Provides expected and input values for testVulnerableComment().
- [testSimpleSelectConditional()](DatabaseSelectTestCase/testSimpleSelectConditional.md) — Test basic conditionals on SELECT statements.
- [testSimpleSelectExpression()](DatabaseSelectTestCase/testSimpleSelectExpression.md) — Test SELECT statements with expressions.
- [testSimpleSelectExpressionMultiple()](DatabaseSelectTestCase/testSimpleSelectExpressionMultiple.md) — Test SELECT statements with multiple expressions.
- [testSimpleSelectMultipleFields()](DatabaseSelectTestCase/testSimpleSelectMultipleFields.md) — Test adding multiple fields to a select statement at the same time.
- [testSimpleSelectAllFields()](DatabaseSelectTestCase/testSimpleSelectAllFields.md) — Test adding all fields from a given table to a select statement.
- [testNullCondition()](DatabaseSelectTestCase/testNullCondition.md) — Test that we can find a record with a NULL value.
- [testNotNullCondition()](DatabaseSelectTestCase/testNotNullCondition.md) — Test that we can find a record without a NULL value.
- [testUnion()](DatabaseSelectTestCase/testUnion.md) — Test that we can UNION multiple Select queries together. This is semantically equal to UNION DISTINCT, so we don't explicitly test that.
- [testUnionAll()](DatabaseSelectTestCase/testUnionAll.md) — Test that we can UNION ALL multiple Select queries together.
- [testUnionOrder()](DatabaseSelectTestCase/testUnionOrder.md) — Tests that we can UNION multiple Select queries together and set the ORDER.
- [testUnionOrderLimit()](DatabaseSelectTestCase/testUnionOrderLimit.md) — Tests that we can UNION multiple Select queries together with a LIMIT.
- [testRandomOrder()](DatabaseSelectTestCase/testRandomOrder.md) — Test that random ordering of queries works.
- [testSelectDuplicateAlias()](DatabaseSelectTestCase/testSelectDuplicateAlias.md) — Test that aliases are renamed when duplicates.

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
