# FileTransferFTPExtension::chmodJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/ftp.inc`](../_file.md), lines 123–137 · [local source](../../../../../source/includes/filetransfer/ftp.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc#L123-L137)
- **Class:** [FileTransferFTPExtension](../FileTransferFTPExtension.md)

## Signature

```php
function chmodJailed($path, $mode, $recursive)
```

## Documentation

_No docblock in source._

## Code

```php
  function chmodJailed($path, $mode, $recursive) {
    if (!ftp_chmod($this->connection, $mode, $path)) {
      throw new FileTransferException("Unable to set permissions on %file", NULL, array('%file' => $path));
    }
    if ($this->isDirectory($path) && $recursive) {
      $filelist = @ftp_nlist($this->connection, $path);
      if (!$filelist) {
        //empty directory - returns false
        return;
      }
      foreach ($filelist as $file) {
        $this->chmodJailed($file, $mode, $recursive);
      }
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ftp.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
