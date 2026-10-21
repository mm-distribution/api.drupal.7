# ArchiverTar::getArchive()

- **Type:** Method
- **File:** [`modules/system/system.archiver.inc`](../_file.md), lines 68–70 · [local source](../../../../../source/modules/system/system.archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc#L68-L70)
- **Class:** [ArchiverTar](../ArchiverTar.md)
- **Module/theme:** system

## Signature

```php
public function getArchive()
```

## Documentation

```text
Retrieve the tar engine itself.

In some cases it may be necessary to directly access the underlying
Archive_Tar object for implementation-specific logic. This is for advanced
use only as it is not shared by other implementations of ArchiveInterface.

@return
  The Archive_Tar object used by this object.
```

## Code

```php
  public function getArchive() {
    return $this->tar;
  }
```

---
_Drupal 7.103 · [modules/system/system.archiver.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
