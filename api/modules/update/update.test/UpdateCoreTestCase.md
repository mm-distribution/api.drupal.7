# UpdateCoreTestCase

- **Type:** Class
- **File:** [`modules/update/update.test`](_file.md), lines 63–277 · [local source](../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L63-L277)
- **Module/theme:** update

## Signature

```php
class UpdateCoreTestCase extends UpdateTestHelper
```

## Documentation

```text
Tests behavior related to discovering and listing updates to Drupal core.
```

## Methods (derived index)

- [getInfo()](UpdateCoreTestCase/getInfo.md)
- [setUp()](UpdateCoreTestCase/setUp.md)
- [testNoUpdatesAvailable()](UpdateCoreTestCase/testNoUpdatesAvailable.md) — Tests the Update Manager module when no updates are available.
- [testNormalUpdateAvailable()](UpdateCoreTestCase/testNormalUpdateAvailable.md) — Tests the Update Manager module when one normal update is available.
- [testSecurityUpdateAvailable()](UpdateCoreTestCase/testSecurityUpdateAvailable.md) — Tests the Update Manager module when a security update is available.
- [testDatestampMismatch()](UpdateCoreTestCase/testDatestampMismatch.md) — Ensures proper results where there are date mismatches among modules.
- [testModulePageRunCron()](UpdateCoreTestCase/testModulePageRunCron.md) — Checks that running cron updates the list of available updates.
- [testModulePageUpToDate()](UpdateCoreTestCase/testModulePageUpToDate.md) — Checks the messages at admin/modules when the site is up to date.
- [testModulePageRegularUpdate()](UpdateCoreTestCase/testModulePageRegularUpdate.md) — Checks the messages at admin/modules when an update is missing.
- [testModulePageSecurityUpdate()](UpdateCoreTestCase/testModulePageSecurityUpdate.md) — Checks the messages at admin/modules when a security update is missing.
- [testServiceUnavailable()](UpdateCoreTestCase/testServiceUnavailable.md) — Tests the Update Manager module when the update server returns 503 errors.
- [testFetchTasks()](UpdateCoreTestCase/testFetchTasks.md) — Tests that exactly one fetch task per project is created and not more.
- [setSystemInfo7_0()](UpdateCoreTestCase/setSystemInfo7_0.md) — Sets the version to 7.0 when no project-specific mapping is defined.

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
