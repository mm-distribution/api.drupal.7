# FileTransfer::chmod()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 92–100 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L92-L100)
- **Class:** [FileTransfer](../FileTransfer.md)

## Signature

```php
public final function chmod($path, $mode, $recursive = FALSE)
```

## Documentation

```text
@see http://php.net/chmod

@param string $path
@param long $mode
@param bool $recursive
```

## Code

```php
  public final function chmod($path, $mode, $recursive = FALSE) {
    if (!in_array('FileTransferChmodInterface', class_implements(get_class($this)))) {
      throw new FileTransferException('Unable to change file permissions');
    }
    $path = $this->sanitizePath($path);
    $path = $this->fixRemotePath($path);
    $this->checkPath($path);
    $this->chmodJailed($path, $mode, $recursive);
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
