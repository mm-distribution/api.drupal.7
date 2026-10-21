# ThemeUpdater::isInstalled()

- **Type:** Method
- **File:** [`modules/system/system.updater.inc`](../_file.md), lines 96–98 · [local source](../../../../../source/modules/system/system.updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc#L96-L98)
- **Class:** [ThemeUpdater](../ThemeUpdater.md)
- **Module/theme:** system

## Signature

```php
public function isInstalled()
```

## Documentation

_No docblock in source._

## Code

```php
  public function isInstalled() {
    return (bool) drupal_get_filename('theme', $this->name, NULL, FALSE);
  }
```

---
_Drupal 7.103 · [modules/system/system.updater.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
