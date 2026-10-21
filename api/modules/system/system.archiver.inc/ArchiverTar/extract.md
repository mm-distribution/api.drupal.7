# ArchiverTar::extract()

- **Type:** Method
- **File:** [`modules/system/system.archiver.inc`](../_file.md), lines 39–48 · [local source](../../../../../source/modules/system/system.archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc#L39-L48)
- **Class:** [ArchiverTar](../ArchiverTar.md)
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
      $this->tar->extractList($files, $path, '', FALSE, FALSE);
    }
    else {
      $this->tar->extract($path, FALSE, FALSE);
    }

    return $this;
  }
```

---
_Drupal 7.103 · [modules/system/system.archiver.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
