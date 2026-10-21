# Updater::update()

- **Type:** Method
- **File:** [`includes/updater.inc`](../_file.md), lines 230–269 · [local source](../../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L230-L269)
- **Class:** [Updater](../Updater.md)

## Signature

```php
public function update(&$filetransfer, $overrides = array())
```

## Documentation

```text
Updates a Drupal project, returns a list of next actions.

@param FileTransfer $filetransfer
  Object that is a child of FileTransfer. Used for moving files
  to the server.
@param array $overrides
  An array of settings to override defaults; see self::getInstallArgs().

@return array
  An array of links which the user may need to complete the update
```

## Code

```php
  public function update(&$filetransfer, $overrides = array()) {
    try {
      // Establish arguments with possible overrides.
      $args = $this->getInstallArgs($overrides);

      // Take a Backup.
      if ($args['make_backup']) {
        $this->makeBackup($args['install_dir'], $args['backup_dir']);
      }

      if (!$this->name) {
        // This is bad, don't want to delete the install directory.
        throw new UpdaterException(t('Fatal error in update, cowardly refusing to wipe out the install directory.'));
      }

      // Make sure the installation parent directory exists and is writable.
      $this->prepareInstallDirectory($filetransfer, $args['install_dir']);

      if (is_dir($args['install_dir'] . '/' . $this->name)) {
        // Remove the existing installed file.
        $filetransfer->removeDirectory($args['install_dir'] . '/' . $this->name);
      }

      // Copy the directory in place.
      $filetransfer->copyDirectory($this->source, $args['install_dir']);

      // Make sure what we just installed is readable by the web server.
      $this->makeWorldReadable($filetransfer, $args['install_dir'] . '/' . $this->name);

      // Run the updates.
      // @TODO: decide if we want to implement this.
      $this->postUpdate();

      // For now, just return a list of links of things to do.
      return $this->postUpdateTasks();
    }
    catch (FileTransferException $e) {
      throw new UpdaterFileTransferException(t('File Transfer failed, reason: !reason', array('!reason' => strtr($e->getMessage(), $e->arguments))));
    }
  }
```

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
