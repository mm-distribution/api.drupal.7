# StatisticsLoggingTestCase

- **Type:** Class
- **File:** [`modules/statistics/statistics.test`](_file.md), lines 55–166 · [local source](../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L55-L166)
- **Module/theme:** statistics

## Signature

```php
class StatisticsLoggingTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests that logging via statistics_exit() works for all pages.

We subclass DrupalWebTestCase rather than StatisticsTestCase, because we
want to test requests from an anonymous user.
```

## Properties

### $auth_user

```php
protected $auth_user;
```

### $node

```php
protected $node;
```

## Methods (derived index)

- [getInfo()](StatisticsLoggingTestCase/getInfo.md)
- [setUp()](StatisticsLoggingTestCase/setUp.md)
- [testLogging()](StatisticsLoggingTestCase/testLogging.md) — Verifies request logging for cached and uncached pages.

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
