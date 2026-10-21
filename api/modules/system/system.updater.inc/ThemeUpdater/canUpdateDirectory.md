# ThemeUpdater::canUpdateDirectory()

- **Type:** Method
- **File:** [`modules/system/system.updater.inc`](../_file.md), lines 100–106 · [local source](../../../../../source/modules/system/system.updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc#L100-L106)
- **Class:** [ThemeUpdater](../ThemeUpdater.md)
- **Module/theme:** system

## Signature

```php
static function canUpdateDirectory($directory)
```

## Documentation

_No docblock in source._

## Code

```php
  static function canUpdateDirectory($directory) {
    // This is a lousy test, but don't know how else to confirm it is a theme.
    if (file_scan_directory($directory, '/.*\.module$/')) {
      return FALSE;
    }
    return TRUE;
  }
```

---
_Drupal 7.103 · [modules/system/system.updater.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
