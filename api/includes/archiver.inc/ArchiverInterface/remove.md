# ArchiverInterface::remove()

- **Type:** Method
- **File:** [`includes/archiver.inc`](../_file.md), lines 44–44 · [local source](../../../../source/includes/archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/archiver.inc#L44)
- **Class:** [ArchiverInterface](../ArchiverInterface.md)

## Signature

```php
public function remove($path);
```

## Documentation

```text
Removes the specified file from the archive.

@param $path
  The file name relative to the root of the archive to remove.

@return ArchiverInterface
  The called object.
```

## Code

```php
  public function remove($path);
```

---
_Drupal 7.103 · [includes/archiver.inc](https://github.com/drupal/drupal/blob/7.103/includes/archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
