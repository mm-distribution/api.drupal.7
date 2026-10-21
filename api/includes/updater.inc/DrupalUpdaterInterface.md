# DrupalUpdaterInterface

- **Type:** Interface
- **File:** [`includes/updater.inc`](_file.md), lines 21–65 · [local source](../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L21-L65)

## Signature

```php
interface DrupalUpdaterInterface
```

## Documentation

```text
Interface for a class which can update a Drupal project.

An Updater currently serves the following purposes:
  - It can take a given directory, and determine if it can operate on it.
  - It can move the contents of that directory into the appropriate place
    on the system using FileTransfer classes.
  - It can return a list of "next steps" after an update or install.
  - In the future, it will most likely perform some of those steps as well.
```

## Methods (derived index)

- [isInstalled()](DrupalUpdaterInterface/isInstalled.md) — Checks if the project is installed.
- [getProjectName()](DrupalUpdaterInterface/getProjectName.md) — Returns the system name of the project.
- [getInstallDirectory()](DrupalUpdaterInterface/getInstallDirectory.md)
- [canUpdateDirectory()](DrupalUpdaterInterface/canUpdateDirectory.md) — Determine if the Updater can handle the project provided in $directory.
- [postInstall()](DrupalUpdaterInterface/postInstall.md) — Actions to run after an install has occurred.
- [postUpdate()](DrupalUpdaterInterface/postUpdate.md) — Actions to run after an update has occurred.

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
