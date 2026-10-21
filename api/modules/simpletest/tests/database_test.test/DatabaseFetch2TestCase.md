# DatabaseFetch2TestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/database_test.test`](_file.md), lines 480–540 · [local source](../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L480-L540)
- **Module/theme:** batch_test

## Signature

```php
class DatabaseFetch2TestCase extends DatabaseTestCase
```

## Documentation

```text
Test fetch actions, part 2.

We get timeout errors if we try to run too many tests at once.
```

## Methods (derived index)

- [getInfo()](DatabaseFetch2TestCase/getInfo.md)
- [setUp()](DatabaseFetch2TestCase/setUp.md)
- [testQueryFetchNum()](DatabaseFetch2TestCase/testQueryFetchNum.md)
- [testQueryFetchBoth()](DatabaseFetch2TestCase/testQueryFetchBoth.md) — Confirm that we can fetch a record into a doubly-keyed array explicitly.
- [testQueryFetchCol()](DatabaseFetch2TestCase/testQueryFetchCol.md) — Confirm that we can fetch an entire column of a result set at once.

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
