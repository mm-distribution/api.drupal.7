# PollUpgradePathTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/upgrade/upgrade.node.test`](_file.md), lines 100–157 · [local source](../../../../../../source/modules/simpletest/tests/upgrade/upgrade.node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.node.test#L100-L157)
- **Module/theme:** batch_test

## Signature

```php
class PollUpgradePathTestCase extends UpgradePathTestCase
```

## Documentation

```text
Upgrade test for node type poll.

Load a bare installation of Drupal 6 and run the upgrade process on it.

The install only contains dblog (although it's optional, it's only so that
another hook_watchdog module can take its place, the site is not functional
without watchdog) and update.
```

## Methods (derived index)

- [getInfo()](PollUpgradePathTestCase/getInfo.md)
- [setUp()](PollUpgradePathTestCase/setUp.md)
- [testPollUpgrade()](PollUpgradePathTestCase/testPollUpgrade.md) — Test a successful upgrade.

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.node.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
