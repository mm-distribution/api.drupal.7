# ModuleUpdater

- **Type:** Class
- **File:** [`modules/system/system.updater.inc`](_file.md), lines 12–67 · [local source](../../../../source/modules/system/system.updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc#L12-L67)
- **Module/theme:** system

## Signature

```php
class ModuleUpdater extends Updater implements DrupalUpdaterInterface
```

## Documentation

```text
Class for updating modules using FileTransfer classes via authorize.php.
```

## Methods (derived index)

- [getInstallDirectory()](ModuleUpdater/getInstallDirectory.md) — Return the directory where a module should be installed.
- [isInstalled()](ModuleUpdater/isInstalled.md)
- [canUpdateDirectory()](ModuleUpdater/canUpdateDirectory.md)
- [canUpdate()](ModuleUpdater/canUpdate.md)
- [postInstallTasks()](ModuleUpdater/postInstallTasks.md) — Returns a list of post install actions.
- [postUpdateTasks()](ModuleUpdater/postUpdateTasks.md)

---
_Drupal 7.103 · [modules/system/system.updater.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
