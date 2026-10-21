# ArchiverTar::remove()

- **Type:** Method
- **File:** [`modules/system/system.archiver.inc`](../_file.md), lines 30–37 · [local source](../../../../../source/modules/system/system.archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc#L30-L37)
- **Class:** [ArchiverTar](../ArchiverTar.md)
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
    // @todo Archive_Tar doesn't have a remove operation
    // so we'll have to simulate it somehow, probably by
    // creating a new archive with everything but the removed
    // file.

    return $this;
  }
```

---
_Drupal 7.103 · [modules/system/system.archiver.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
