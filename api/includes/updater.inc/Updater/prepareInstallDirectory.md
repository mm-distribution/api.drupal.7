# Updater::prepareInstallDirectory()

- **Type:** Method
- **File:** [`includes/updater.inc`](../_file.md), lines 315–348 · [local source](../../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L315-L348)
- **Class:** [Updater](../Updater.md)

## Signature

```php
public function prepareInstallDirectory(&$filetransfer, $directory)
```

## Documentation

```text
Make sure the installation parent directory exists and is writable.

@param FileTransfer $filetransfer
  Object which is a child of FileTransfer.
@param string $directory
  The installation directory to prepare.
```

## Code

```php
  public function prepareInstallDirectory(&$filetransfer, $directory) {
    // Make the parent dir writable if need be and create the dir.
    if (!is_dir($directory)) {
      $parent_dir = dirname($directory);
      if (!is_writable($parent_dir)) {
        @chmod($parent_dir, 0755);
        // It is expected that this will fail if the directory is owned by the
        // FTP user. If the FTP user == web server, it will succeed.
        try {
          $filetransfer->createDirectory($directory);
          $this->makeWorldReadable($filetransfer, $directory);
        }
        catch (FileTransferException $e) {
          // Probably still not writable. Try to chmod and do it again.
          // @todo: Make a new exception class so we can catch it differently.
          try {
            $old_perms = substr(sprintf('%o', fileperms($parent_dir)), -4);
            $filetransfer->chmod($parent_dir, 0755);
            $filetransfer->createDirectory($directory);
            $this->makeWorldReadable($filetransfer, $directory);
            // Put the permissions back.
            $filetransfer->chmod($parent_dir, intval($old_perms, 8));
          }
          catch (FileTransferException $e) {
            $message = t($e->getMessage(), $e->arguments);
            $throw_message = t('Unable to create %directory due to the following: %reason', array('%directory' => $directory, '%reason' => $message));
            throw new UpdaterException($throw_message);
          }
        }
        // Put the parent directory back.
        @chmod($parent_dir, 0555);
      }
    }
  }
```

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
