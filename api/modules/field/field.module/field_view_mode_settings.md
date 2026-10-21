# field_view_mode_settings()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 621–640 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L621-L640)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function field_view_mode_settings($entity_type, $bundle)
```

## Documentation

```text
Returns view mode settings in a given bundle.

@param $entity_type
  The type of entity; e.g. 'node' or 'user'.
@param $bundle
  The bundle name to return view mode settings for.

@return
  An array keyed by view mode, with the following key/value pairs:
  - custom_settings: Boolean specifying whether the view mode uses a
    dedicated set of display options (TRUE), or the 'default' options
    (FALSE). Defaults to FALSE.
```

## Code

```php
function field_view_mode_settings($entity_type, $bundle) {
  $cache = &drupal_static(__FUNCTION__, array());

  if (!isset($cache[$entity_type][$bundle])) {
    $bundle_settings = field_bundle_settings($entity_type, $bundle);
    $settings = $bundle_settings['view_modes'];
    // Include view modes for which nothing has been stored yet, but whose
    // definition in hook_entity_info() specify they should use custom settings
    // by default.
    $entity_info = entity_get_info($entity_type);
    foreach ($entity_info['view modes'] as $view_mode => $view_mode_info) {
      if (!isset($settings[$view_mode]['custom_settings']) && $view_mode_info['custom settings']) {
        $settings[$view_mode]['custom_settings'] = TRUE;
      }
    }
    $cache[$entity_type][$bundle] = $settings;
  }

  return $cache[$entity_type][$bundle];
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
