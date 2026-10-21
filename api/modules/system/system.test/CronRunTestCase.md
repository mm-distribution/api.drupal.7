# CronRunTestCase

- **Type:** Class
- **File:** [`modules/system/system.test`](_file.md), lines 794–966 · [local source](../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L794-L966)
- **Module/theme:** system

## Signature

```php
class CronRunTestCase extends DrupalWebTestCase
```

## Documentation

_No docblock in source._

## Methods (derived index)

- [getInfo()](CronRunTestCase/getInfo.md) — Implement getInfo().
- [setUp()](CronRunTestCase/setUp.md)
- [testCronRun()](CronRunTestCase/testCronRun.md) — Test cron runs.
- [testAutomaticCron()](CronRunTestCase/testAutomaticCron.md) — Ensure that the automatic cron run feature is working.
- [testTempFileCleanup()](CronRunTestCase/testTempFileCleanup.md) — Ensure that temporary files are removed.
- [testCronExceptions()](CronRunTestCase/testCronExceptions.md) — Make sure exceptions thrown on hook_cron() don't affect other modules.
- [testManualCron()](CronRunTestCase/testManualCron.md) — Ensure that the manual cron run is working.
- [testCronCacheExpiration()](CronRunTestCase/testCronCacheExpiration.md) — Tests that hook_flush_caches() is not invoked on every single cron run.

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
