# Field Info API

- **Topic id:** `field_info`
- **Defined in:** [`modules/field/field.info.inc`](../modules/field/field.info.inc/_file.md), line 34 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L34)

## Documentation

```text
@defgroup field_info Field Info API
@{
Obtain information about Field API configuration.

The Field Info API exposes information about field types, fields,
instances, bundles, widget types, display formatters, behaviors,
and settings defined by or with the Field API.

See @link field Field API @endlink for information about the other parts of
the Field API.
```

## Members (derived, 29)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_field_info_collate_fields()](../modules/field/field.info.inc/_field_info_collate_fields.md) (function) — Collates all information on existing fields and instances.
- [_field_info_collate_types()](../modules/field/field.info.inc/_field_info_collate_types.md) (function) — Collates all information on field types, widget types and related structures.
- [_field_info_prepare_extra_fields()](../modules/field/field.info.inc/_field_info_prepare_extra_fields.md) (function) — Prepares 'extra fields' for the current run-time context.
- [_field_info_prepare_field()](../modules/field/field.info.inc/_field_info_prepare_field.md) (function) — Prepares a field definition for the current run-time context.
- [_field_info_prepare_instance()](../modules/field/field.info.inc/_field_info_prepare_instance.md) (function) — Prepares an instance definition for the current run-time context.
- [_field_info_prepare_instance_display()](../modules/field/field.info.inc/_field_info_prepare_instance_display.md) (function) — Adapts display specifications to the current run-time context.
- [_field_info_prepare_instance_widget()](../modules/field/field.info.inc/_field_info_prepare_instance_widget.md) (function) — Prepares widget specifications for the current run-time context.
- [field_behaviors_widget()](../modules/field/field.info.inc/field_behaviors_widget.md) (function) — Determines the behavior of a widget with respect to an operation.
- [field_info_bundles()](../modules/field/field.info.inc/field_info_bundles.md) (function) — Returns information about existing bundles.
- [field_info_cache_clear()](../modules/field/field.info.inc/field_info_cache_clear.md) (function) — Clears the field info cache without clearing the field data cache.
- [field_info_extra_fields()](../modules/field/field.info.inc/field_info_extra_fields.md) (function) — Returns a list and settings of pseudo-field elements in a given bundle.
- [field_info_field()](../modules/field/field.info.inc/field_info_field.md) (function) — Returns data about an individual field, given a field name.
- [field_info_field_by_id()](../modules/field/field.info.inc/field_info_field_by_id.md) (function) — Returns data about an individual field, given a field ID.
- [field_info_field_by_ids()](../modules/field/field.info.inc/field_info_field_by_ids.md) (function) — Returns the same data as field_info_field_by_id() for every field.
- [field_info_field_map()](../modules/field/field.info.inc/field_info_field_map.md) (function) — Returns a lightweight map of fields across bundles.
- [field_info_field_settings()](../modules/field/field.info.inc/field_info_field_settings.md) (function) — Returns a field type's default settings.
- [field_info_field_types()](../modules/field/field.info.inc/field_info_field_types.md) (function) — Returns information about field types from hook_field_info().
- [field_info_fields()](../modules/field/field.info.inc/field_info_fields.md) (function) — Returns all field definitions.
- [field_info_formatter_settings()](../modules/field/field.info.inc/field_info_formatter_settings.md) (function) — Returns a field formatter's default settings.
- [field_info_formatter_types()](../modules/field/field.info.inc/field_info_formatter_types.md) (function) — Returns information about field formatters from hook_field_formatter_info().
- [field_info_instance()](../modules/field/field.info.inc/field_info_instance.md) (function) — Returns an array of instance data for a specific field and bundle.
- [field_info_instance_settings()](../modules/field/field.info.inc/field_info_instance_settings.md) (function) — Returns a field type's default instance settings.
- [field_info_instances()](../modules/field/field.info.inc/field_info_instances.md) (function) — Retrieves information about field instances.
- [field_info_max_weight()](../modules/field/field.info.inc/field_info_max_weight.md) (function) — Returns the maximum weight of all the components in an entity.
- [field_info_storage_settings()](../modules/field/field.info.inc/field_info_storage_settings.md) (function) — Returns a field storage type's default settings.
- [field_info_storage_types()](../modules/field/field.info.inc/field_info_storage_types.md) (function) — Returns information about field storage from hook_field_storage_info().
- [field_info_widget_settings()](../modules/field/field.info.inc/field_info_widget_settings.md) (function) — Returns a field widget's default settings.
- [field_info_widget_types()](../modules/field/field.info.inc/field_info_widget_types.md) (function) — Returns information about field widgets from hook_field_widget_info().
- [hook_field_info_max_weight()](../modules/field/field.api.php/hook_field_info_max_weight.md) (function) — Returns the maximum weight for the entity components handled by the module.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
