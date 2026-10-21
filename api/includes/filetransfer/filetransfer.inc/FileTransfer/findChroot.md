# FileTransfer::findChroot()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 293–314 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L293-L314)
- **Class:** [FileTransfer](../FileTransfer.md)

## Signature

```php
function findChroot()
```

## Documentation

```text
Return the chroot property for this connection.

It does this by moving up the tree until it finds itself. If successful,
it will return the chroot, otherwise FALSE.

@return
  The chroot path for this connection or FALSE.
```

## Code

```php
  function findChroot() {
    // If the file exists as is, there is no chroot.
    $path = __FILE__;
    $path = $this->fixRemotePath($path, FALSE);
    if ($this->isFile($path)) {
      return FALSE;
    }

    $path = dirname(__FILE__);
    $path = $this->fixRemotePath($path, FALSE);
    $parts = explode('/', $path);
    $chroot = '';
    while (count($parts)) {
      $check = implode('/', $parts);
      if ($this->isFile($check . '/' . drupal_basename(__FILE__))) {
        // Remove the trailing slash.
        return substr($chroot, 0, -1);
      }
      $chroot .= array_shift($parts) . '/';
    }
    return FALSE;
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
