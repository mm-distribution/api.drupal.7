# StatisticsAdminTestCase

- **Type:** Class
- **File:** [`modules/statistics/statistics.test`](_file.md), lines 311–460 · [local source](../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L311-L460)
- **Module/theme:** statistics

## Signature

```php
class StatisticsAdminTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests the statistics administration screen.
```

## Properties

### $privileged_user

```php
protected $privileged_user;
```

```text
A user that has permission to administer and access statistics.

@var object|FALSE

A fully loaded user object, or FALSE if user creation failed.
```

### $test_node

```php
protected $test_node;
```

```text
A page node for which to check access statistics.

@var object
```

## Methods (derived index)

- [getInfo()](StatisticsAdminTestCase/getInfo.md)
- [setUp()](StatisticsAdminTestCase/setUp.md)
- [testStatisticsSettings()](StatisticsAdminTestCase/testStatisticsSettings.md) — Verifies that the statistics settings page works.
- [testDeleteNode()](StatisticsAdminTestCase/testDeleteNode.md) — Tests that when a node is deleted, the node counter is deleted too.
- [testDeleteUser()](StatisticsAdminTestCase/testDeleteUser.md) — Tests that accesslog reflects when a user is deleted.
- [testExpiredLogs()](StatisticsAdminTestCase/testExpiredLogs.md) — Tests that cron clears day counts and expired access logs.

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
