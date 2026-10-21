# locale_system_update()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 888–893 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L888-L893)
- **Module/theme:** locale

## Signature

```php
function locale_system_update($components)
```

## Documentation

```text
Imports translations when new modules or themes are installed.

This function will either import translation for the component change
right away, or start a batch if more files need to be imported.

@param $components
  An array of component (theme and/or module) names to import
  translations for.
```

## Code

```php
function locale_system_update($components) {
  include_once DRUPAL_ROOT . '/includes/locale.inc';
  if ($batch = locale_batch_by_component($components)) {
    batch_set($batch);
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
