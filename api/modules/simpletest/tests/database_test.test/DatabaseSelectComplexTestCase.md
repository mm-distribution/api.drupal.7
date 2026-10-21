# DatabaseSelectComplexTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/database_test.test`](_file.md), lines 2132–2489 · [local source](../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2132-L2489)
- **Module/theme:** batch_test

## Signature

```php
class DatabaseSelectComplexTestCase extends DatabaseTestCase
```

## Documentation

```text
Test more complex select statements.
```

## Methods (derived index)

- [getInfo()](DatabaseSelectComplexTestCase/getInfo.md)
- [testDefaultJoin()](DatabaseSelectComplexTestCase/testDefaultJoin.md) — Test simple JOIN statements.
- [testLeftOuterJoin()](DatabaseSelectComplexTestCase/testLeftOuterJoin.md) — Test LEFT OUTER joins.
- [testGroupBy()](DatabaseSelectComplexTestCase/testGroupBy.md) — Test GROUP BY clauses.
- [testGroupByAndHaving()](DatabaseSelectComplexTestCase/testGroupByAndHaving.md) — Test GROUP BY and HAVING clauses together.
- [testRange()](DatabaseSelectComplexTestCase/testRange.md) — Test range queries. The SQL clause varies with the database.
- [testDistinct()](DatabaseSelectComplexTestCase/testDistinct.md) — Test distinct queries.
- [testCountQuery()](DatabaseSelectComplexTestCase/testCountQuery.md) — Test that we can generate a count query from a built query.
- [testHavingCountQuery()](DatabaseSelectComplexTestCase/testHavingCountQuery.md)
- [testCountQueryRemovals()](DatabaseSelectComplexTestCase/testCountQueryRemovals.md) — Test that countQuery properly removes 'all_fields' statements and ordering clauses.
- [testCountQueryFieldRemovals()](DatabaseSelectComplexTestCase/testCountQueryFieldRemovals.md) — Test that countQuery properly removes fields and expressions.
- [testCountQueryDistinct()](DatabaseSelectComplexTestCase/testCountQueryDistinct.md) — Test that we can generate a count query from a query with distinct.
- [testCountQueryGroupBy()](DatabaseSelectComplexTestCase/testCountQueryGroupBy.md) — Test that we can generate a count query from a query with GROUP BY.
- [testNestedConditions()](DatabaseSelectComplexTestCase/testNestedConditions.md) — Confirm that we can properly nest conditional clauses.
- [testJoinTwice()](DatabaseSelectComplexTestCase/testJoinTwice.md) — Confirm we can join on a single table twice with a dynamic alias.
- [testJoinConditionObject()](DatabaseSelectComplexTestCase/testJoinConditionObject.md) — Test that join conditions can use Condition objects.

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
