# EnableDisableTestCase

- **Type:** Class
- **File:** [`modules/system/system.test`](_file.md), lines 132–349 · [local source](../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L132-L349)
- **Module/theme:** system

## Signature

```php
class EnableDisableTestCase extends ModuleTestCase
```

## Documentation

```text
Test module enabling/disabling functionality.
```

## Properties

### $profile

```php
protected $profile = 'testing';
```

## Methods (derived index)

- [getInfo()](EnableDisableTestCase/getInfo.md)
- [testEnableDisable()](EnableDisableTestCase/testEnableDisable.md) — Test that all core modules can be enabled, disabled and uninstalled.
- [testEntityInfoChanges()](EnableDisableTestCase/testEntityInfoChanges.md) — Ensures entity info cache is updated after changes.
- [testEntityInfoCacheWatchdog()](EnableDisableTestCase/testEntityInfoCacheWatchdog.md) — Tests entity info cache after enabling a module with a dependency on an entity providing module.
- [assertSuccessfulDisableAndUninstall()](EnableDisableTestCase/assertSuccessfulDisableAndUninstall.md) — Disables and uninstalls a module and asserts that it was done correctly.

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
