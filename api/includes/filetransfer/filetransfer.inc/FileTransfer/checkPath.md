# FileTransfer::checkPath()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 159–166 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L159-L166)
- **Class:** [FileTransfer](../FileTransfer.md)

## Signature

```php
protected final function checkPath($path)
```

## Documentation

```text
Checks that the path is inside the jail and throws an exception if not.

@param $path
  A path to check against the jail.
```

## Code

```php
  protected final function checkPath($path) {
    $full_jail = $this->chroot . $this->jail;
    $full_path = drupal_realpath(substr($this->chroot . $path, 0, strlen($full_jail)));
    $full_path = $this->fixRemotePath($full_path, FALSE);
    if ($full_jail !== $full_path) {
      throw new FileTransferException('@directory is outside of the @jail', NULL, array('@directory' => $path, '@jail' => $this->jail));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
