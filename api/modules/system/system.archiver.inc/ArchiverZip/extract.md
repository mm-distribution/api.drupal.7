# ArchiverZip::extract()

- **Type:** Method
- **File:** [`modules/system/system.archiver.inc`](../_file.md), lines 107–116 · [local source](../../../../../source/modules/system/system.archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc#L107-L116)
- **Class:** [ArchiverZip](../ArchiverZip.md)
- **Module/theme:** system

## Signature

```php
public function extract($path, Array $files = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function extract($path, Array $files = array()) {
    if ($files) {
      $this->zip->extractTo($path, $files);
    }
    else {
      $this->zip->extractTo($path);
    }

    return $this;
  }
```

---
_Drupal 7.103 · [modules/system/system.archiver.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
