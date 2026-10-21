# ArchiverTar::__construct()

- **Type:** Method
- **File:** [`modules/system/system.archiver.inc`](../_file.md), lines 20–22 · [local source](../../../../../source/modules/system/system.archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc#L20-L22)
- **Class:** [ArchiverTar](../ArchiverTar.md)
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
    $this->tar = new Archive_Tar($file_path);
  }
```

---
_Drupal 7.103 · [modules/system/system.archiver.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
