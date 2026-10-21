# ArchiverZip::getArchive()

- **Type:** Method
- **File:** [`modules/system/system.archiver.inc`](../_file.md), lines 136–138 · [local source](../../../../../source/modules/system/system.archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc#L136-L138)
- **Class:** [ArchiverZip](../ArchiverZip.md)
- **Module/theme:** system

## Signature

```php
public function getArchive()
```

## Documentation

```text
Retrieve the zip engine itself.

In some cases it may be necessary to directly access the underlying
ZipArchive object for implementation-specific logic. This is for advanced
use only as it is not shared by other implementations of ArchiveInterface.

@return
  The ZipArchive object used by this object.
```

## Code

```php
  public function getArchive() {
    return $this->zip;
  }
```

---
_Drupal 7.103 · [modules/system/system.archiver.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
