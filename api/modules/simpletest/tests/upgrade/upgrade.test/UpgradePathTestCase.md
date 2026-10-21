# UpgradePathTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/upgrade/upgrade.test`](_file.md), lines 6–313 · [local source](../../../../../../source/modules/simpletest/tests/upgrade/upgrade.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test#L6-L313)
- **Module/theme:** batch_test

## Signature

```php
abstract class UpgradePathTestCase extends DrupalWebTestCase
```

## Documentation

```text
Perform end-to-end tests of the upgrade path.
```

## Properties

### $databaseDumpFiles

```php
var $databaseDumpFiles = array();
```

```text
The file path(s) to the dumped database(s) to load into the child site.

@var array
```

### $upgradedSite

```php
var $upgradedSite = FALSE;
```

```text
Flag that indicates whether the child site has been upgraded.
```

### $upgradeErrors

```php
var $upgradeErrors = array();
```

```text
Array of errors triggered during the upgrade process.
```

### $loadedModules

```php
var $loadedModules = array();
```

```text
Array of modules loaded when the test starts.
```

### $zlibInstalled

```php
var $zlibInstalled = TRUE;
```

```text
Flag to indicate whether zlib is installed or not.
```

### $pendingUpdates

```php
var $pendingUpdates = TRUE;
```

```text
Flag to indicate whether there are pending updates or not.
```

### $skipUpgradeTest

```php
var $skipUpgradeTest = FALSE;
```

```text
Flag to indicate whether to skip upgrade tests.
```

## Methods (derived index)

- [__construct()](UpgradePathTestCase/__construct.md) — Constructs an UpgradePathTestCase object.
- [prepareD7Session()](UpgradePathTestCase/prepareD7Session.md) — Prepares the appropriate session for the release of Drupal being upgraded.
- [setUp()](UpgradePathTestCase/setUp.md) — Overrides DrupalWebTestCase::setUp() for upgrade testing.
- [variable_set()](UpgradePathTestCase/variable_set.md) — Specialized variable_set() that works even if the child site is not upgraded.
- [refreshVariables()](UpgradePathTestCase/refreshVariables.md) — Specialized refreshVariables().
- [performUpgrade()](UpgradePathTestCase/performUpgrade.md) — Perform the upgrade.
- [uninstallModulesExcept()](UpgradePathTestCase/uninstallModulesExcept.md) — Force uninstall all modules from a test database, except those listed.

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test) · Licensed GPL-2.0-or-later (see LICENSE)._
