# UpdateTestContribCase

- **Type:** Class
- **File:** [`modules/update/update.test`](_file.md), lines 282–693 · [local source](../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L282-L693)
- **Module/theme:** update

## Signature

```php
class UpdateTestContribCase extends UpdateTestHelper
```

## Documentation

```text
Tests behavior related to handling updates to contributed modules and themes.
```

## Methods (derived index)

- [getInfo()](UpdateTestContribCase/getInfo.md)
- [setUp()](UpdateTestContribCase/setUp.md)
- [testNoReleasesAvailable()](UpdateTestContribCase/testNoReleasesAvailable.md) — Tests when there is no available release data for a contrib module.
- [testUpdateContribBasic()](UpdateTestContribCase/testUpdateContribBasic.md) — Tests the basic functionality of a contrib module on the status report.
- [testUpdateContribOrder()](UpdateTestContribCase/testUpdateContribOrder.md) — Tests that contrib projects are ordered by project name.
- [testUpdateBaseThemeSecurityUpdate()](UpdateTestContribCase/testUpdateBaseThemeSecurityUpdate.md) — Tests that subthemes are notified about security updates for base themes.
- [testUpdateAdminThemeSecurityUpdate()](UpdateTestContribCase/testUpdateAdminThemeSecurityUpdate.md) — Tests that the admin theme is always notified about security updates.
- [testUpdateShowDisabledThemes()](UpdateTestContribCase/testUpdateShowDisabledThemes.md) — Tests that disabled themes are only shown when desired.
- [testUpdateBrokenFetchURL()](UpdateTestContribCase/testUpdateBrokenFetchURL.md) — Makes sure that if we fetch from a broken URL, sane things happen.
- [testHookUpdateStatusAlter()](UpdateTestContribCase/testHookUpdateStatusAlter.md) — Checks that hook_update_status_alter() works to change a status.

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
