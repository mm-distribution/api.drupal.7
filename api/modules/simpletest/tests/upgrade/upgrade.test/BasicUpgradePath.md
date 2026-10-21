# BasicUpgradePath

- **Type:** Class
- **File:** [`modules/simpletest/tests/upgrade/upgrade.test`](_file.md), lines 344–430 · [local source](../../../../../../source/modules/simpletest/tests/upgrade/upgrade.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test#L344-L430)
- **Module/theme:** batch_test

## Signature

```php
class BasicUpgradePath extends UpgradePathTestCase
```

## Documentation

```text
Perform basic upgrade tests.

Load a bare installation of Drupal 6 and run the upgrade process on it.

The install only contains dblog (although it's optional, it's only so that
another hook_watchdog module can take its place, the site is not functional
without watchdog) and update.
```

## Methods (derived index)

- [getInfo()](BasicUpgradePath/getInfo.md)
- [setUp()](BasicUpgradePath/setUp.md)
- [testFailedUpgrade()](BasicUpgradePath/testFailedUpgrade.md) — Test a failed upgrade, and verify that the failure is reported.
- [testBasicUpgrade()](BasicUpgradePath/testBasicUpgrade.md) — Test a successful upgrade.

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test) · Licensed GPL-2.0-or-later (see LICENSE)._
