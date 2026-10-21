# ModuleUpdater::getInstallDirectory()

- **Type:** Method
- **File:** [`modules/system/system.updater.inc`](../_file.md), lines 26–34 · [local source](../../../../../source/modules/system/system.updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc#L26-L34)
- **Class:** [ModuleUpdater](../ModuleUpdater.md)
- **Module/theme:** system

## Signature

```php
public function getInstallDirectory()
```

## Documentation

```text
Return the directory where a module should be installed.

If the module is already installed, drupal_get_path() will return
a valid path and we should install it there (although we need to use an
absolute path, so we prepend DRUPAL_ROOT). If we're installing a new
module, we always want it to go into sites/all/modules, since that's
where all the documentation recommends users install their modules, and
there's no way that can conflict on a multi-site installation, since
the Update manager won't let you install a new module if it's already
found on your system, and if there was a copy in sites/all, we'd see it.
```

## Code

```php
  public function getInstallDirectory() {
    if ($this->isInstalled() && ($relative_path = drupal_get_path('module', $this->name))) {
      $relative_path = dirname($relative_path);
    }
    else {
      $relative_path = 'sites/all/modules';
    }
    return DRUPAL_ROOT . '/' . $relative_path;
  }
```

---
_Drupal 7.103 · [modules/system/system.updater.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
