# system_rebuild_theme_data()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2666–2672 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2666-L2672)
- **Module/theme:** system

## Signature

```php
function system_rebuild_theme_data()
```

## Documentation

```text
Rebuild, save, and return data about all currently available themes.

@return
  Array of all available themes and their data.
```

## Code

```php
function system_rebuild_theme_data() {
  $themes = _system_rebuild_theme_data();
  ksort($themes);
  system_get_files_database($themes, 'theme');
  system_update_files_database($themes, 'theme');
  return $themes;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
