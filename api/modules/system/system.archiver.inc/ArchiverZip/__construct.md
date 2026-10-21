# ArchiverZip::__construct()

- **Type:** Method
- **File:** [`modules/system/system.archiver.inc`](../_file.md), lines 87–93 · [local source](../../../../../source/modules/system/system.archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc#L87-L93)
- **Class:** [ArchiverZip](../ArchiverZip.md)
- **Module/theme:** system

## Signature

```php
public function __construct($file_path)
```

## Documentation

_No docblock in source._

## Code

```php
  public function __construct($file_path) {
    $this->zip = new ZipArchive();
    if ($this->zip->open($file_path) !== TRUE) {
      // @todo: This should be an interface-specific exception some day.
      throw new Exception(t('Cannot open %file_path', array('%file_path' => $file_path)));
    }
  }
```

---
_Drupal 7.103 · [modules/system/system.archiver.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
