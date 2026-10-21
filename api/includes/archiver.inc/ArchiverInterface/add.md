# ArchiverInterface::add()

- **Type:** Method
- **File:** [`includes/archiver.inc`](../_file.md), lines 33–33 · [local source](../../../../source/includes/archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/archiver.inc#L33)
- **Class:** [ArchiverInterface](../ArchiverInterface.md)

## Signature

```php
public function add($file_path);
```

## Documentation

```text
Adds the specified file or directory to the archive.

@param $file_path
  The full system path of the file or directory to add. Only local files
  and directories are supported.

@return ArchiverInterface
  The called object.
```

## Code

```php
  public function add($file_path);
```

---
_Drupal 7.103 · [includes/archiver.inc](https://github.com/drupal/drupal/blob/7.103/includes/archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
