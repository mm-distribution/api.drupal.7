# modules/field/field.info.inc

- **Source:** [local](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · 817 lines
- **Module/theme:** field

## File documentation

```text
@file
Field Info API, providing information about available fields and field types.
```

## Functions (derived index)

- [_field_info_field_cache()](_field_info_field_cache.md) — Retrieves the FieldInfo object for the current request.
- [field_info_cache_clear()](field_info_cache_clear.md) — Clears the field info cache without clearing the field data cache.
- [_field_info_collate_fields()](_field_info_collate_fields.md) — Collates all information on existing fields and instances.
- [_field_info_collate_types()](_field_info_collate_types.md) — Collates all information on field types, widget types and related structures.
- [_field_info_prepare_field()](_field_info_prepare_field.md) — Prepares a field definition for the current run-time context.
- [_field_info_prepare_instance()](_field_info_prepare_instance.md) — Prepares an instance definition for the current run-time context.
- [_field_info_prepare_instance_display()](_field_info_prepare_instance_display.md) — Adapts display specifications to the current run-time context.
- [_field_info_prepare_instance_widget()](_field_info_prepare_instance_widget.md) — Prepares widget specifications for the current run-time context.
- [_field_info_prepare_extra_fields()](_field_info_prepare_extra_fields.md) — Prepares 'extra fields' for the current run-time context.
- [field_behaviors_widget()](field_behaviors_widget.md) — Determines the behavior of a widget with respect to an operation.
- [field_info_field_types()](field_info_field_types.md) — Returns information about field types from hook_field_info().
- [field_info_widget_types()](field_info_widget_types.md) — Returns information about field widgets from hook_field_widget_info().
- [field_info_formatter_types()](field_info_formatter_types.md) — Returns information about field formatters from hook_field_formatter_info().
- [field_info_storage_types()](field_info_storage_types.md) — Returns information about field storage from hook_field_storage_info().
- [field_info_bundles()](field_info_bundles.md) — Returns information about existing bundles.
- [field_info_field_map()](field_info_field_map.md) — Returns a lightweight map of fields across bundles.
- [field_info_fields()](field_info_fields.md) — Returns all field definitions.
- [field_info_field()](field_info_field.md) — Returns data about an individual field, given a field name.
- [field_info_field_by_id()](field_info_field_by_id.md) — Returns data about an individual field, given a field ID.
- [field_info_field_by_ids()](field_info_field_by_ids.md) — Returns the same data as field_info_field_by_id() for every field.
- [field_info_instances()](field_info_instances.md) — Retrieves information about field instances.
- [field_info_instance()](field_info_instance.md) — Returns an array of instance data for a specific field and bundle.
- [field_info_extra_fields()](field_info_extra_fields.md) — Returns a list and settings of pseudo-field elements in a given bundle.
- [field_info_max_weight()](field_info_max_weight.md) — Returns the maximum weight of all the components in an entity.
- [field_info_field_settings()](field_info_field_settings.md) — Returns a field type's default settings.
- [field_info_instance_settings()](field_info_instance_settings.md) — Returns a field type's default instance settings.
- [field_info_widget_settings()](field_info_widget_settings.md) — Returns a field widget's default settings.
- [field_info_formatter_settings()](field_info_formatter_settings.md) — Returns a field formatter's default settings.
- [field_info_storage_settings()](field_info_storage_settings.md) — Returns a field storage type's default settings.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
