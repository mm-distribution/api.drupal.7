# Field Types API

- **Topic id:** `field_types`
- **Defined in:** [`modules/field/field.api.php`](../modules/field/field.api.php/_file.md), line 97 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L97)

## Documentation

```text
@defgroup field_types Field Types API
@{
Define field types.

In the Field API, each field has a type, which determines what kind of data
(integer, string, date, etc.) the field can hold, which settings it provides,
and so on. The data type(s) accepted by a field are defined in
hook_field_schema(); other basic properties of a field are defined in
hook_field_info(). The other hooks below are called by the Field Attach API
to perform field-type-specific actions.

The Field Types API also defines two kinds of pluggable handlers: widgets
and formatters. @link field_widget Widgets @endlink specify how the field
appears in edit forms, while @link field_formatter formatters @endlink
specify how the field appears in displayed entities.

A third kind of pluggable handlers, storage backends, is defined by the
@link field_storage Field Storage API @endlink.

See @link field Field API @endlink for information about the other parts of
the Field API.
```

## Members (derived, 26)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [hook_field_access()](../modules/field/field.api.php/hook_field_access.md) (function) — Determine whether the user has access to a given field.
- [hook_field_delete()](../modules/field/field.api.php/hook_field_delete.md) (function) — Define custom delete behavior for this module's field data.
- [hook_field_delete_revision()](../modules/field/field.api.php/hook_field_delete_revision.md) (function) — Define custom revision delete behavior for this module's field types.
- [hook_field_display_ENTITY_TYPE_alter()](../modules/field/field.api.php/hook_field_display_ENTITY_TYPE_alter.md) (function) — Alters the display settings of a field on a given entity type before it gets displayed.
- [hook_field_display_alter()](../modules/field/field.api.php/hook_field_display_alter.md) (function) — Alters the display settings of a field before it gets displayed.
- [hook_field_extra_fields()](../modules/field/field.api.php/hook_field_extra_fields.md) (function) — Exposes "pseudo-field" components on fieldable entities.
- [hook_field_extra_fields_alter()](../modules/field/field.api.php/hook_field_extra_fields_alter.md) (function) — Alter "pseudo-field" components on fieldable entities.
- [hook_field_extra_fields_display_alter()](../modules/field/field.api.php/hook_field_extra_fields_display_alter.md) (function) — Alters the display settings of pseudo-fields before an entity is displayed.
- [hook_field_formatter_settings_form()](../modules/field_ui/field_ui.api.php/hook_field_formatter_settings_form.md) (function) — Specify the form elements for a formatter's settings.
- [hook_field_formatter_settings_summary()](../modules/field_ui/field_ui.api.php/hook_field_formatter_settings_summary.md) (function) — Return a short summary for the current formatter settings of an instance.
- [hook_field_info()](../modules/field/field.api.php/hook_field_info.md) (function) — Define Field API field types.
- [hook_field_info_alter()](../modules/field/field.api.php/hook_field_info_alter.md) (function) — Perform alterations on Field API field types.
- [hook_field_insert()](../modules/field/field.api.php/hook_field_insert.md) (function) — Define custom insert behavior for this module's field data.
- [hook_field_instance_settings_form()](../modules/field_ui/field_ui.api.php/hook_field_instance_settings_form.md) (function) — Add settings to an instance field settings form.
- [hook_field_is_empty()](../modules/field/field.api.php/hook_field_is_empty.md) (function) — Define what constitutes an empty item for a field type.
- [hook_field_load()](../modules/field/field.api.php/hook_field_load.md) (function) — Define custom load behavior for this module's field types.
- [hook_field_prepare_translation()](../modules/field/field.api.php/hook_field_prepare_translation.md) (function) — Define custom prepare_translation behavior for this module's field types.
- [hook_field_prepare_view()](../modules/field/field.api.php/hook_field_prepare_view.md) (function) — Prepare field values prior to display.
- [hook_field_presave()](../modules/field/field.api.php/hook_field_presave.md) (function) — Define custom presave behavior for this module's field types.
- [hook_field_schema()](../modules/field/field.api.php/hook_field_schema.md) (function) — Define the Field API schema for a field structure.
- [hook_field_schema_alter()](../modules/field/field.api.php/hook_field_schema_alter.md) (function) — Allow modules to alter the schema for a field.
- [hook_field_settings_form()](../modules/field_ui/field_ui.api.php/hook_field_settings_form.md) (function) — Add settings to a field settings form.
- [hook_field_storage_update_field()](../modules/field/field.api.php/hook_field_storage_update_field.md) (function) — Update the storage information for a field.
- [hook_field_update()](../modules/field/field.api.php/hook_field_update.md) (function) — Define custom update behavior for this module's field data.
- [hook_field_validate()](../modules/field/field.api.php/hook_field_validate.md) (function) — Validate this module's field data.
- [hook_field_widget_settings_form()](../modules/field_ui/field_ui.api.php/hook_field_widget_settings_form.md) (function) — Add settings to a widget settings form.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
