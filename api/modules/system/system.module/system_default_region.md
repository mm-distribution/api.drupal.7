# system_default_region()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2796–2799 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2796-L2799)
- **Module/theme:** system

## Signature

```php
function system_default_region($theme)
```

## Documentation

```text
Get the name of the default region for a given theme.

@param $theme
  The name of a theme.

@return
  A string that is the region name.
```

## Code

```php
function system_default_region($theme) {
  $regions = system_region_list($theme, REGIONS_VISIBLE, FALSE);
  return $regions ? reset($regions) : '';
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
