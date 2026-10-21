# ThemeUpdater::getInstallDirectory()

- **Type:** Method
- **File:** [`modules/system/system.updater.inc`](../_file.md), lines 86–94 · [local source](../../../../../source/modules/system/system.updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc#L86-L94)
- **Class:** [ThemeUpdater](../ThemeUpdater.md)
- **Module/theme:** system

## Signature

```php
public function getInstallDirectory()
```

## Documentation

```text
Return the directory where a theme should be installed.

If the theme is already installed, drupal_get_path() will return
a valid path and we should install it there (although we need to use an
absolute path, so we prepend DRUPAL_ROOT). If we're installing a new
theme, we always want it to go into sites/all/themes, since that's
where all the documentation recommends users install their themes, and
there's no way that can conflict on a multi-site installation, since
the Update manager won't let you install a new theme if it's already
found on your system, and if there was a copy in sites/all, we'd see it.
```

## Code

```php
  public function getInstallDirectory() {
    if ($this->isInstalled() && ($relative_path = drupal_get_path('theme', $this->name))) {
      $relative_path = dirname($relative_path);
    }
    else {
      $relative_path = 'sites/all/themes';
    }
    return DRUPAL_ROOT . '/' . $relative_path;
  }
```

---
_Drupal 7.103 · [modules/system/system.updater.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
