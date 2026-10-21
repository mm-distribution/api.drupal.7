# ArchiverZip::add()

- **Type:** Method
- **File:** [`modules/system/system.archiver.inc`](../_file.md), lines 95–99 · [local source](../../../../../source/modules/system/system.archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc#L95-L99)
- **Class:** [ArchiverZip](../ArchiverZip.md)
- **Module/theme:** system

## Signature

```php
public function add($file_path)
```

## Documentation

_No docblock in source._

## Code

```php
  public function add($file_path) {
    $this->zip->addFile($file_path);

    return $this;
  }
```

---
_Drupal 7.103 · [modules/system/system.archiver.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
