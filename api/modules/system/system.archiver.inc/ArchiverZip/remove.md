# ArchiverZip::remove()

- **Type:** Method
- **File:** [`modules/system/system.archiver.inc`](../_file.md), lines 101–105 · [local source](../../../../../source/modules/system/system.archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc#L101-L105)
- **Class:** [ArchiverZip](../ArchiverZip.md)
- **Module/theme:** system

## Signature

```php
public function remove($file_path)
```

## Documentation

_No docblock in source._

## Code

```php
  public function remove($file_path) {
    $this->zip->deleteName($file_path);

    return $this;
  }
```

---
_Drupal 7.103 · [modules/system/system.archiver.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
