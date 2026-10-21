# DatabaseDeleteTruncateTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/database_test.test`](_file.md), lines 1153–1210 · [local source](../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1153-L1210)
- **Module/theme:** batch_test

## Signature

```php
class DatabaseDeleteTruncateTestCase extends DatabaseTestCase
```

## Documentation

```text
Delete/Truncate tests.

The DELETE tests are not as extensive, as all of the interesting code for
DELETE queries is in the conditional which is identical to the UPDATE and
SELECT conditional handling.

The TRUNCATE tests are not extensive either, because the behavior of
TRUNCATE queries is not consistent across database engines. We only test
that a TRUNCATE query actually deletes all rows from the target table.
```

## Methods (derived index)

- [getInfo()](DatabaseDeleteTruncateTestCase/getInfo.md)
- [testSubselectDelete()](DatabaseDeleteTruncateTestCase/testSubselectDelete.md) — Confirm that we can use a subselect in a delete successfully.
- [testSimpleDelete()](DatabaseDeleteTruncateTestCase/testSimpleDelete.md) — Confirm that we can delete a single record successfully.
- [testTruncate()](DatabaseDeleteTruncateTestCase/testTruncate.md) — Confirm that we can truncate a whole table successfully.

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
