# DatabaseAlterTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/database_test.test`](_file.md), lines 2922–3072 · [local source](../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2922-L3072)
- **Module/theme:** batch_test

## Signature

```php
class DatabaseAlterTestCase extends DatabaseTestCase
```

## Documentation

```text
Select alter tests.

@see database_test_query_alter()
```

## Methods (derived index)

- [getInfo()](DatabaseAlterTestCase/getInfo.md)
- [testSimpleAlter()](DatabaseAlterTestCase/testSimpleAlter.md) — Test that we can do basic alters.
- [testAlterWithJoin()](DatabaseAlterTestCase/testAlterWithJoin.md) — Test that we can alter the joins on a query.
- [testAlterChangeConditional()](DatabaseAlterTestCase/testAlterChangeConditional.md) — Test that we can alter a query's conditionals.
- [testAlterChangeFields()](DatabaseAlterTestCase/testAlterChangeFields.md) — Test that we can alter the fields of a query.
- [testAlterExpression()](DatabaseAlterTestCase/testAlterExpression.md) — Test that we can alter expressions in the query.
- [testAlterRemoveRange()](DatabaseAlterTestCase/testAlterRemoveRange.md) — Test that we can remove a range() value from a query. This also tests hook_query_TAG_alter().
- [testSimpleAlterSubquery()](DatabaseAlterTestCase/testSimpleAlterSubquery.md) — Test that we can do basic alters on subqueries.

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
