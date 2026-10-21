# ArchiverInterface::extract()

- **Type:** Method
- **File:** [`includes/archiver.inc`](../_file.md), lines 59–59 · [local source](../../../../source/includes/archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/archiver.inc#L59)
- **Class:** [ArchiverInterface](../ArchiverInterface.md)

## Signature

```php
public function extract($path, array $files = array());
```

## Documentation

```text
Extracts multiple files in the archive to the specified path.

@param $path
  A full system path of the directory to which to extract files.
@param $files
  Optionally specify a list of files to be extracted. Files are
  relative to the root of the archive. If not specified, all files
  in the archive will be extracted.

@return ArchiverInterface
  The called object.
```

## Code

```php
  public function extract($path, array $files = array());
```

---
_Drupal 7.103 · [includes/archiver.inc](https://github.com/drupal/drupal/blob/7.103/includes/archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
