# ThemeUpdater::postInstallTasks()

- **Type:** Method
- **File:** [`modules/system/system.updater.inc`](../_file.md), lines 119–124 · [local source](../../../../../source/modules/system/system.updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc#L119-L124)
- **Class:** [ThemeUpdater](../ThemeUpdater.md)
- **Module/theme:** system

## Signature

```php
public function postInstallTasks()
```

## Documentation

_No docblock in source._

## Code

```php
  public function postInstallTasks() {
    return array(
      l(t('Enable newly added themes'), 'admin/appearance'),
      l(t('Administration pages'), 'admin'),
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.updater.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
