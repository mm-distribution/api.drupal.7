# ModuleUpdater::isInstalled()

- **Type:** Method
- **File:** [`modules/system/system.updater.inc`](../_file.md), lines 36–38 · [local source](../../../../../source/modules/system/system.updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc#L36-L38)
- **Class:** [ModuleUpdater](../ModuleUpdater.md)
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
    return (bool) drupal_get_filename('module', $this->name, NULL, FALSE);
  }
```

---
_Drupal 7.103 · [modules/system/system.updater.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
