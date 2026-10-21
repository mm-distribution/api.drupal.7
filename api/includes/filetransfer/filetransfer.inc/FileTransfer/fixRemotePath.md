# FileTransfer::fixRemotePath()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 179–188 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L179-L188)
- **Class:** [FileTransfer](../FileTransfer.md)

## Signature

```php
protected final function fixRemotePath($path, $strip_chroot = TRUE)
```

## Documentation

```text
Returns a modified path suitable for passing to the server.
If a path is a windows path, makes it POSIX compliant by removing the drive letter.
If $this->chroot has a value, it is stripped from the path to allow for
chroot'd filetransfer systems.

@param $path
@param $strip_chroot

@return string
```

## Code

```php
  protected final function fixRemotePath($path, $strip_chroot = TRUE) {
    $path = $this->sanitizePath($path);
    $path = preg_replace('|^([a-z]{1}):|i', '', $path); // Strip out windows driveletter if its there.
    if ($strip_chroot) {
      if ($this->chroot && strpos($path, $this->chroot) === 0) {
        $path = ($path == $this->chroot) ? '' : substr($path, strlen($this->chroot));
      }
    }
    return $path;
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
