# Updater::install()

- **Type:** Method
- **File:** [`includes/updater.inc`](../_file.md), lines 282–305 · [local source](../../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L282-L305)
- **Class:** [Updater](../Updater.md)

## Signature

```php
public function install(&$filetransfer, $overrides = array())
```

## Documentation

```text
Installs a Drupal project, returns a list of next actions.

@param FileTransfer $filetransfer
  Object that is a child of FileTransfer.
@param array $overrides
  An array of settings to override defaults; see self::getInstallArgs().

@return array
  An array of links which the user may need to complete the install.
```

## Code

```php
  public function install(&$filetransfer, $overrides = array()) {
    try {
      // Establish arguments with possible overrides.
      $args = $this->getInstallArgs($overrides);

      // Make sure the installation parent directory exists and is writable.
      $this->prepareInstallDirectory($filetransfer, $args['install_dir']);

      // Copy the directory in place.
      $filetransfer->copyDirectory($this->source, $args['install_dir']);

      // Make sure what we just installed is readable by the web server.
      $this->makeWorldReadable($filetransfer, $args['install_dir'] . '/' . $this->name);

      // Potentially enable something?
      // @TODO: decide if we want to implement this.
      $this->postInstall();
      // For now, just return a list of links of things to do.
      return $this->postInstallTasks();
    }
    catch (FileTransferException $e) {
      throw new UpdaterFileTransferException(t('File Transfer failed, reason: !reason', array('!reason' => strtr($e->getMessage(), $e->arguments))));
    }
  }
```

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
