# FileTransfer::setChroot()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 320–323 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L320-L323)
- **Class:** [FileTransfer](../FileTransfer.md)

## Signature

```php
function setChroot()
```

## Documentation

```text
Sets the chroot and changes the jail to match the correct path scheme
```

## Code

```php
  function setChroot() {
    $this->chroot = $this->findChroot();
    $this->jail = $this->fixRemotePath($this->jail);
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
