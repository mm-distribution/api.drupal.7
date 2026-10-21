# ArchiverZip::listContents()

- **Type:** Method
- **File:** [`modules/system/system.archiver.inc`](../_file.md), lines 118–124 · [local source](../../../../../source/modules/system/system.archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc#L118-L124)
- **Class:** [ArchiverZip](../ArchiverZip.md)
- **Module/theme:** system

## Signature

```php
public function listContents()
```

## Documentation

_No docblock in source._

## Code

```php
  public function listContents() {
    $files = array();
    for ($i=0; $i < $this->zip->numFiles; $i++) {
      $files[] = $this->zip->getNameIndex($i);
    }
    return $files;
  }
```

---
_Drupal 7.103 · [modules/system/system.archiver.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
