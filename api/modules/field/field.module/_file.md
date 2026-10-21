# modules/field/field.module

- **Source:** [local](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · 1233 lines
- **Module/theme:** field

## File documentation

```text
@file
Attach custom data fields to Drupal entities.
```

## Functions (derived index)

- [field_help()](field_help.md) — Implements hook_help().
- [field_permission()](field_permission.md) — Implements hook_permission().
- [field_theme()](field_theme.md) — Implements hook_theme().
- [field_cron()](field_cron.md) — Implements hook_cron().
- [field_system_info_alter()](field_system_info_alter.md) — Implements hook_system_info_alter().
- [field_flush_caches()](field_flush_caches.md) — Implements hook_flush_caches().
- [field_modules_enabled()](field_modules_enabled.md) — Implements hook_modules_enabled().
- [field_modules_disabled()](field_modules_disabled.md) — Implements hook_modules_disabled().
- [field_sync_field_status()](field_sync_field_status.md) — Refreshes the 'active' and 'storage_active' columns for fields.
- [field_associate_fields()](field_associate_fields.md) — Allows a module to update the database for fields and columns it controls.
- [field_get_default_value()](field_get_default_value.md) — Helper function to get the default value for a field on an entity.
- [_field_filter_items()](_field_filter_items.md) — Helper function to filter out empty field values.
- [_field_sort_items()](_field_sort_items.md) — Helper function to sort items in a field according to user drag-n-drop reordering.
- [_field_sort_items_helper()](_field_sort_items_helper.md) — Sort function for items order. (copied form element_sort(), which acts on #weight keys)
- [_field_sort_items_value_helper()](_field_sort_items_value_helper.md) — Same as above, using ['_weight']['#value']
- [field_bundle_settings()](field_bundle_settings.md) — Gets or sets administratively defined bundle settings.
- [field_view_mode_settings()](field_view_mode_settings.md) — Returns view mode settings in a given bundle.
- [field_get_display()](field_get_display.md) — Returns the display settings to use for an instance in a given view mode.
- [field_extra_fields_get_display()](field_extra_fields_get_display.md) — Returns the display settings to use for pseudo-fields in a given view mode.
- [_field_extra_fields_pre_render()](_field_extra_fields_pre_render.md) — Pre-render callback to adjust weights and visibility of non-field elements.
- [field_cache_clear()](field_cache_clear.md) — Clear the field info and field data caches.
- [field_filter_xss()](field_filter_xss.md) — Like filter_xss_admin(), but with a shorter list of allowed tags.
- [_field_filter_xss_allowed_tags()](_field_filter_xss_allowed_tags.md) — List of tags allowed by field_filter_xss().
- [_field_filter_xss_display_allowed_tags()](_field_filter_xss_display_allowed_tags.md) — Human-readable list of allowed tags, for display in help texts.
- [field_view_value()](field_view_value.md) — Returns a renderable array for a single field value.
- [field_view_field()](field_view_field.md) — Returns a renderable array for the value of a single field in an entity.
- [field_get_items()](field_get_items.md) — Returns the field items in the language they currently would be displayed.
- [field_has_data()](field_has_data.md) — Determine whether a field has any data.
- [field_access()](field_access.md) — Determine whether the user has access to a given field.
- [field_extract_bundle()](field_extract_bundle.md) — Helper function to extract the bundle name of from a bundle object.
- [template_preprocess_field()](template_preprocess_field.md) — Theme preprocess function for theme_field() and field.tpl.php.
- [template_process_field()](template_process_field.md) — Theme process function for theme_field() and field.tpl.php.
- [theme_field()](theme_field.md) — Returns HTML for a field.
- [_element_validate_integer()](_element_validate_integer.md) — DEPRECATED: Helper form element validator: integer.
- [_element_validate_integer_positive()](_element_validate_integer_positive.md) — DEPRECATED: Helper form element validator: integer > 0.
- [_element_validate_number()](_element_validate_number.md) — DEPRECATED: Helper form element validator: number.

## Classes and interfaces (derived index)

- [FieldException](FieldException.md) — Base class for all exceptions thrown by Field API functions.
- [FieldUpdateForbiddenException](FieldUpdateForbiddenException.md) — Exception class thrown by hook_field_update_forbid().

## Constants

### FIELD_CARDINALITY_UNLIMITED

- Line 236; topics: field

```php
define('FIELD_CARDINALITY_UNLIMITED', -1);
```

```text
Value for field API indicating a field accepts an unlimited number of values.
```

### FIELD_BEHAVIOR_NONE

- Line 243; topics: field

```php
define('FIELD_BEHAVIOR_NONE', 0x0001);
```

```text
Value for field API indicating a widget doesn't accept default values.

@see hook_field_widget_info()
```

### FIELD_BEHAVIOR_DEFAULT

- Line 255; topics: field

```php
define('FIELD_BEHAVIOR_DEFAULT', 0x0002);
```

```text
Value for field API concerning widget default and multiple value settings.

@see hook_field_widget_info()

When used in a widget default context, indicates the widget accepts default
values. When used in a multiple value context for a widget that allows the
input of one single field value, indicates that the widget will be repeated
for each value input.
```

### FIELD_BEHAVIOR_CUSTOM

- Line 262; topics: field

```php
define('FIELD_BEHAVIOR_CUSTOM', 0x0004);
```

```text
Value for field API indicating a widget can receive several field values.

@see hook_field_widget_info()
```

### FIELD_LOAD_CURRENT

- Line 268; topics: field

```php
define('FIELD_LOAD_CURRENT', 'FIELD_LOAD_CURRENT');
```

```text
Age argument for loading the most recent version of an entity's
field data with field_attach_load().
```

### FIELD_LOAD_REVISION

- Line 274; topics: field

```php
define('FIELD_LOAD_REVISION', 'FIELD_LOAD_REVISION');
```

```text
Age argument for loading the version of an entity's field data
specified in the entity with field_attach_load().
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
