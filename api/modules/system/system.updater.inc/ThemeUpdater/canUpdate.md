# ThemeUpdater::canUpdate()

- **Type:** Method
- **File:** [`modules/system/system.updater.inc`](../_file.md), lines 108–110 · [local source](../../../../../source/modules/system/system.updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc#L108-L110)
- **Class:** [ThemeUpdater](../ThemeUpdater.md)
- **Module/theme:** system

## Signature

```php
public static function canUpdate($project_name)
```

## Documentation

_No docblock in source._

## Code

```php
  public static function canUpdate($project_name) {
    return (bool) drupal_get_path('theme', $project_name);
  }
```

---
_Drupal 7.103 · [modules/system/system.updater.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
