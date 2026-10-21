# ModuleUpdater::postInstallTasks()

- **Type:** Method
- **File:** [`modules/system/system.updater.inc`](../_file.md), lines 54–60 · [local source](../../../../../source/modules/system/system.updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc#L54-L60)
- **Class:** [ModuleUpdater](../ModuleUpdater.md)
- **Module/theme:** system

## Signature

```php
public function postInstallTasks()
```

## Documentation

```text
Returns a list of post install actions.
```

## Code

```php
  public function postInstallTasks() {
    return array(
      l(t('Install another module'), 'admin/modules/install'),
      l(t('Enable newly added modules'), 'admin/modules'),
      l(t('Administration pages'), 'admin'),
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.updater.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
