# ArchiverTar::listContents()

- **Type:** Method
- **File:** [`modules/system/system.archiver.inc`](../_file.md), lines 50–56 · [local source](../../../../../source/modules/system/system.archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc#L50-L56)
- **Class:** [ArchiverTar](../ArchiverTar.md)
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
    foreach ($this->tar->listContent() as $file_data) {
      $files[] = $file_data['filename'];
    }
    return $files;
  }
```

---
_Drupal 7.103 · [modules/system/system.archiver.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
