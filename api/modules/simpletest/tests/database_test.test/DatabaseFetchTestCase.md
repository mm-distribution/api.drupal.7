# DatabaseFetchTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/database_test.test`](_file.md), lines 378–473 · [local source](../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L378-L473)
- **Module/theme:** batch_test

## Signature

```php
class DatabaseFetchTestCase extends DatabaseTestCase
```

## Documentation

```text
Test fetch actions, part 1.

We get timeout errors if we try to run too many tests at once.
```

## Methods (derived index)

- [getInfo()](DatabaseFetchTestCase/getInfo.md)
- [testQueryFetchDefault()](DatabaseFetchTestCase/testQueryFetchDefault.md) — Confirm that we can fetch a record properly in default object mode.
- [testQueryFetchObject()](DatabaseFetchTestCase/testQueryFetchObject.md) — Confirm that we can fetch a record to an object explicitly.
- [testQueryFetchArray()](DatabaseFetchTestCase/testQueryFetchArray.md) — Confirm that we can fetch a record to an array associative explicitly.
- [testQueryFetchClass()](DatabaseFetchTestCase/testQueryFetchClass.md) — Confirm that we can fetch a record into a new instance of a custom class.
- [testQueryFetchClasstype()](DatabaseFetchTestCase/testQueryFetchClasstype.md) — Confirms that we can fetch a record into a new instance of a custom class. The name of the class is determined from a value of the first column.

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
