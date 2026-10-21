# DatabaseLoggingTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/database_test.test`](_file.md), lines 3135–3259 · [local source](../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3135-L3259)
- **Module/theme:** batch_test

## Signature

```php
class DatabaseLoggingTestCase extends DatabaseTestCase
```

## Documentation

```text
Query logging tests.
```

## Methods (derived index)

- [getInfo()](DatabaseLoggingTestCase/getInfo.md)
- [testEnableLogging()](DatabaseLoggingTestCase/testEnableLogging.md) — Test that we can log the existence of a query.
- [testEnableMultiLogging()](DatabaseLoggingTestCase/testEnableMultiLogging.md) — Test that we can run two logs in parallel.
- [testEnableTargetLogging()](DatabaseLoggingTestCase/testEnableTargetLogging.md) — Test that we can log queries against multiple targets on the same connection.
- [testEnableTargetLoggingNoTarget()](DatabaseLoggingTestCase/testEnableTargetLoggingNoTarget.md) — Test that logs to separate targets collapse to the same connection properly.
- [testEnableMultiConnectionLogging()](DatabaseLoggingTestCase/testEnableMultiConnectionLogging.md) — Test that we can log queries separately on different connections.

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
