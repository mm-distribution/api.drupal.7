# FileTransferFTPExtension::removeDirectoryJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/ftp.inc`](../_file.md), lines 76–101 · [local source](../../../../../source/includes/filetransfer/ftp.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc#L76-L101)
- **Class:** [FileTransferFTPExtension](../FileTransferFTPExtension.md)

## Signature

```php
protected function removeDirectoryJailed($directory)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function removeDirectoryJailed($directory) {
    $pwd = ftp_pwd($this->connection);
    if (!ftp_chdir($this->connection, $directory)) {
      throw new FileTransferException("Unable to change to directory @directory", NULL, array('@directory' => $directory));
    }
    $list = @ftp_nlist($this->connection, '.');
    if (!$list) {
      $list = array();
    }
    foreach ($list as $item) {
      if ($item == '.' || $item == '..') {
        continue;
      }
      if (@ftp_chdir($this->connection, $item)) {
        ftp_cdup($this->connection);
        $this->removeDirectory(ftp_pwd($this->connection) . '/' . $item);
      }
      else {
        $this->removeFile(ftp_pwd($this->connection) . '/' . $item);
      }
    }
    ftp_chdir($this->connection, $pwd);
    if (!ftp_rmdir($this->connection, $directory)) {
      throw new FileTransferException("Unable to remove to directory @directory", NULL, array('@directory' => $directory));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ftp.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
