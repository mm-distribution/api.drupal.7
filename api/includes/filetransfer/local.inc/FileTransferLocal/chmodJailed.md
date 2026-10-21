# FileTransferLocal::chmodJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/local.inc`](../_file.md), lines 64–75 · [local source](../../../../../source/includes/filetransfer/local.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/local.inc#L64-L75)
- **Class:** [FileTransferLocal](../FileTransferLocal.md)

## Signature

```php
public function chmodJailed($path, $mode, $recursive)
```

## Documentation

_No docblock in source._

## Code

```php
  public function chmodJailed($path, $mode, $recursive) {
    if ($recursive && is_dir($path)) {
      foreach (new RecursiveIteratorIterator(new SkipDotsRecursiveDirectoryIterator($path), RecursiveIteratorIterator::SELF_FIRST) as $filename => $file) {
        if (@!chmod($filename, $mode)) {
          throw new FileTransferException('Cannot chmod %path.', NULL, array('%path' => $filename));
        }
      }
    }
    elseif (@!chmod($path, $mode)) {
      throw new FileTransferException('Cannot chmod %path.', NULL, array('%path' => $path));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/local.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/local.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
