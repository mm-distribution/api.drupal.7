# _field_ui_add_default_view_mode_settings()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 1425–1445 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L1425-L1445)
- **Module/theme:** field_ui

## Signature

```php
function _field_ui_add_default_view_mode_settings($entity_type, $bundle, $view_mode, &$settings)
```

## Documentation

```text
Populates display settings for a new view mode from the default view mode.

When an administrator decides to use custom display settings for a view mode,
that view mode needs to be initialized with the display settings for the
'default' view mode, which it was previously using. This helper function
adds the new custom display settings to this bundle's instances, and saves
them. It also modifies the passed-in $settings array, which the caller can
then save using field_bundle_settings().

@param $entity_type
  The bundle's entity type.
@param $bundle
  The bundle whose view mode is being customized.
@param $view_mode
  The view mode that the administrator has set to use custom settings.
@param $settings
  An associative array of bundle settings, as expected by
  field_bundle_settings().

@see field_ui_display_overview_form_submit().
@see field_bundle_settings()
```

## Code

```php
function _field_ui_add_default_view_mode_settings($entity_type, $bundle, $view_mode, &$settings) {
  // Update display settings for field instances.
  $instances = field_read_instances(array('entity_type' => $entity_type, 'bundle' => $bundle));
  foreach ($instances as $instance) {
    // If this field instance has display settings defined for this view mode,
    // respect those settings.
    if (!isset($instance['display'][$view_mode])) {
      // The instance doesn't specify anything for this view mode, so use the
      // default display settings.
      $instance['display'][$view_mode] = $instance['display']['default'];
      field_update_instance($instance);
    }
  }

  // Update display settings for 'extra fields'.
  foreach (array_keys($settings['extra_fields']['display']) as $name) {
    if (!isset($settings['extra_fields']['display'][$name][$view_mode])) {
      $settings['extra_fields']['display'][$name][$view_mode] = $settings['extra_fields']['display'][$name]['default'];
    }
  }
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
