# Updater

- **Type:** Class
- **File:** [`includes/updater.inc`](_file.md), lines 70–414 · [local source](../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L70-L414)

## Signature

```php
class Updater
```

## Documentation

```text
Base class for Updaters used in Drupal.
```

## Properties

### $source

```php
public $source;
```

```text
@var string $source Directory to install from.
```

### $name

```php
protected $name;
```

```text
@var string $name The name of the project.
```

### $title

```php
protected $title;
```

```text
@var string $title The title of the project.
```

## Methods (derived index)

- [__construct()](Updater/__construct.md)
- [factory()](Updater/factory.md) — Return an Updater of the appropriate type depending on the source.
- [getUpdaterFromDirectory()](Updater/getUpdaterFromDirectory.md) — Determine which Updater class can operate on the given directory.
- [findInfoFile()](Updater/findInfoFile.md) — Figure out what the most important (or only) info file is in a directory.
- [getProjectName()](Updater/getProjectName.md) — Get the name of the project directory (basename).
- [getProjectTitle()](Updater/getProjectTitle.md) — Return the project name from a Drupal info file.
- [getInstallArgs()](Updater/getInstallArgs.md) — Store the default parameters for the Updater.
- [update()](Updater/update.md) — Updates a Drupal project, returns a list of next actions.
- [install()](Updater/install.md) — Installs a Drupal project, returns a list of next actions.
- [prepareInstallDirectory()](Updater/prepareInstallDirectory.md) — Make sure the installation parent directory exists and is writable.
- [makeWorldReadable()](Updater/makeWorldReadable.md) — Ensure that a given directory is world readable.
- [makeBackup()](Updater/makeBackup.md) — Perform a backup.
- [getBackupDir()](Updater/getBackupDir.md) — Return the full path to a directory where backups should be written.
- [postUpdate()](Updater/postUpdate.md) — Perform actions after new code is updated.
- [postInstall()](Updater/postInstall.md) — Perform actions after installation.
- [postInstallTasks()](Updater/postInstallTasks.md) — Return an array of links to pages that should be visited post operation.
- [postUpdateTasks()](Updater/postUpdateTasks.md) — Return an array of links to pages that should be visited post operation.

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
