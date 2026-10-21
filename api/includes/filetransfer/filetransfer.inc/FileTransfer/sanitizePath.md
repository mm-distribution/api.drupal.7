# FileTransfer::sanitizePath()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 196–202 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L196-L202)
- **Class:** [FileTransfer](../FileTransfer.md)

## Signature

```php
function sanitizePath($path)
```

## Documentation

```text
Changes backslashes to slashes, also removes a trailing slash.

@param string $path
@return string
```

## Code

```php
  function sanitizePath($path) {
    $path = str_replace('\\', '/', $path); // Windows path sanitization.
    if (substr($path, -1) == '/') {
      $path = substr($path, 0, -1);
    }
    return $path;
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
