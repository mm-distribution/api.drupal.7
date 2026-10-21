# FileTransfer::copyDirectoryJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 214–228 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L214-L228)
- **Class:** [FileTransfer](../FileTransfer.md)

## Signature

```php
protected function copyDirectoryJailed($source, $destination)
```

## Documentation

```text
Copies a directory.

We need a separate method to make the $destination is in the jail.

@param $source
  The source path.
@param $destination
  The destination path.
```

## Code

```php
  protected function copyDirectoryJailed($source, $destination) {
    if ($this->isDirectory($destination)) {
      $destination = $destination . '/' . drupal_basename($source);
    }
    $this->createDirectory($destination);
    foreach (new RecursiveIteratorIterator(new SkipDotsRecursiveDirectoryIterator($source), RecursiveIteratorIterator::SELF_FIRST) as $filename => $file) {
      $relative_path = substr($filename, strlen($source));
      if ($file->isDir()) {
        $this->createDirectory($destination . $relative_path);
      }
      else {
        $this->copyFile($file->getPathName(), $destination . $relative_path);
      }
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
