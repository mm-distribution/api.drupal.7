# ThemeUpdater::postInstall()

- **Type:** Method
- **File:** [`modules/system/system.updater.inc`](../_file.md), lines 112–117 · [local source](../../../../../source/modules/system/system.updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc#L112-L117)
- **Class:** [ThemeUpdater](../ThemeUpdater.md)
- **Module/theme:** system

## Signature

```php
public function postInstall()
```

## Documentation

_No docblock in source._

## Code

```php
  public function postInstall() {
    // Update the system table.
    clearstatcache();
    system_rebuild_theme_data();

  }
```

---
_Drupal 7.103 · [modules/system/system.updater.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
