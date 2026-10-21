# system_region_list()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2753–2773 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2753-L2773)
- **Module/theme:** system

## Signature

```php
function system_region_list($theme_key, $show = REGIONS_ALL, $labels = TRUE)
```

## Documentation

```text
Get a list of available regions from a specified theme.

@param $theme_key
  The name of a theme.
@param $show
  Possible values: REGIONS_ALL or REGIONS_VISIBLE. Visible excludes hidden
  regions.
@param bool $labels
  (optional) Boolean to specify whether the human readable machine names
  should be returned or not. Defaults to TRUE, but calling code can set
  this to FALSE for better performance, if it only needs machine names.

@return array
  An associative array of regions in the form $region['name'] = 'description'
  if $labels is set to TRUE, or $region['name'] = 'name', if $labels is set
  to FALSE.
```

## Code

```php
function system_region_list($theme_key, $show = REGIONS_ALL, $labels = TRUE) {
  $themes = list_themes();
  if (!isset($themes[$theme_key])) {
    return array();
  }

  $list = array();
  $info = $themes[$theme_key]->info;
  // If requested, suppress hidden regions. See block_admin_display_form().
  foreach ($info['regions'] as $name => $label) {
    if ($show == REGIONS_ALL || !isset($info['regions_hidden']) || !in_array($name, $info['regions_hidden'])) {
      if ($labels) {
        $list[$name] = t($label);
      }
      else {
        $list[$name] = $name;
      }
    }
  }
  return $list;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
