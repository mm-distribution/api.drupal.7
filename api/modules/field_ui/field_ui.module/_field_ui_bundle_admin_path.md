# _field_ui_bundle_admin_path()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.module`](_file.md), lines 338–344 · [local source](../../../../source/modules/field_ui/field_ui.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module#L338-L344)
- **Module/theme:** field_ui

## Signature

```php
function _field_ui_bundle_admin_path($entity_type, $bundle_name)
```

## Documentation

```text
Determines the administration path for a bundle.
```

## Code

```php
function _field_ui_bundle_admin_path($entity_type, $bundle_name) {
  $bundles = field_info_bundles($entity_type);
  $bundle_info = $bundles[$bundle_name];
  if (isset($bundle_info['admin'])) {
    return isset($bundle_info['admin']['real path']) ? $bundle_info['admin']['real path'] : $bundle_info['admin']['path'];
  }
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.module](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module) · Licensed GPL-2.0-or-later (see LICENSE)._
