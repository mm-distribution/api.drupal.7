# FileTransferChmodInterface::chmodJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 390–390 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L390)
- **Class:** [FileTransferChmodInterface](../FileTransferChmodInterface.md)

## Signature

```php
function chmodJailed($path, $mode, $recursive);
```

## Documentation

```text
Changes the permissions of the file / directory specified in $path

@param string $path
  Path to change permissions of.
@param long $mode
  The new file permission mode to be passed to chmod().
@param boolean $recursive
  Pass TRUE to recursively chmod the entire directory specified in $path.
```

## Code

```php
  function chmodJailed($path, $mode, $recursive);
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
