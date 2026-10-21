# ModuleUpdater::canUpdateDirectory()

- **Type:** Method
- **File:** [`modules/system/system.updater.inc`](../_file.md), lines 40–45 · [local source](../../../../../source/modules/system/system.updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc#L40-L45)
- **Class:** [ModuleUpdater](../ModuleUpdater.md)
- **Module/theme:** system

## Signature

```php
public static function canUpdateDirectory($directory)
```

## Documentation

_No docblock in source._

## Code

```php
  public static function canUpdateDirectory($directory) {
    if (file_scan_directory($directory, '/.*\.module$/')) {
      return TRUE;
    }
    return FALSE;
  }
```

---
_Drupal 7.103 · [modules/system/system.updater.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
