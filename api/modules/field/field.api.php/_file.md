# modules/field/field.api.php

- **Source:** [local](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · 2787 lines
- **Module/theme:** field

## File documentation

```text
@file
Hooks provided by the Field module.
```

## Functions (derived index)

- [hook_field_extra_fields()](hook_field_extra_fields.md) — Exposes "pseudo-field" components on fieldable entities.
- [hook_field_extra_fields_alter()](hook_field_extra_fields_alter.md) — Alter "pseudo-field" components on fieldable entities.
- [hook_field_info()](hook_field_info.md) — Define Field API field types.
- [hook_field_info_alter()](hook_field_info_alter.md) — Perform alterations on Field API field types.
- [hook_field_schema()](hook_field_schema.md) — Define the Field API schema for a field structure.
- [hook_field_schema_alter()](hook_field_schema_alter.md) — Allow modules to alter the schema for a field.
- [hook_field_load()](hook_field_load.md) — Define custom load behavior for this module's field types.
- [hook_field_prepare_view()](hook_field_prepare_view.md) — Prepare field values prior to display.
- [hook_field_validate()](hook_field_validate.md) — Validate this module's field data.
- [hook_field_presave()](hook_field_presave.md) — Define custom presave behavior for this module's field types.
- [hook_field_insert()](hook_field_insert.md) — Define custom insert behavior for this module's field data.
- [hook_field_update()](hook_field_update.md) — Define custom update behavior for this module's field data.
- [hook_field_storage_update_field()](hook_field_storage_update_field.md) — Update the storage information for a field.
- [hook_field_delete()](hook_field_delete.md) — Define custom delete behavior for this module's field data.
- [hook_field_delete_revision()](hook_field_delete_revision.md) — Define custom revision delete behavior for this module's field types.
- [hook_field_prepare_translation()](hook_field_prepare_translation.md) — Define custom prepare_translation behavior for this module's field types.
- [hook_field_is_empty()](hook_field_is_empty.md) — Define what constitutes an empty item for a field type.
- [hook_field_widget_info()](hook_field_widget_info.md) — Expose Field API widget types.
- [hook_field_widget_info_alter()](hook_field_widget_info_alter.md) — Perform alterations on Field API widget types.
- [hook_field_widget_form()](hook_field_widget_form.md) — Return the form for a single field widget.
- [hook_field_widget_form_alter()](hook_field_widget_form_alter.md) — Alter forms for field widgets provided by other modules.
- [hook_field_widget_WIDGET_TYPE_form_alter()](hook_field_widget_WIDGET_TYPE_form_alter.md) — Alter widget forms for a specific widget provided by another module.
- [hook_field_widget_properties_alter()](hook_field_widget_properties_alter.md) — Alters the widget properties of a field instance before it gets displayed.
- [hook_field_widget_error()](hook_field_widget_error.md) — Flag a field-level validation error.
- [hook_field_formatter_info()](hook_field_formatter_info.md) — Expose Field API formatter types.
- [hook_field_formatter_info_alter()](hook_field_formatter_info_alter.md) — Perform alterations on Field API formatter types.
- [hook_field_formatter_prepare_view()](hook_field_formatter_prepare_view.md) — Allow formatters to load information for field values being displayed.
- [hook_field_formatter_view()](hook_field_formatter_view.md) — Build a renderable array for a field value.
- [hook_field_attach_form()](hook_field_attach_form.md) — Act on field_attach_form().
- [hook_field_attach_load()](hook_field_attach_load.md) — Act on field_attach_load().
- [hook_field_attach_validate()](hook_field_attach_validate.md) — Act on field_attach_validate().
- [hook_field_attach_submit()](hook_field_attach_submit.md) — Act on field_attach_submit().
- [hook_field_attach_presave()](hook_field_attach_presave.md) — Act on field_attach_presave().
- [hook_field_attach_insert()](hook_field_attach_insert.md) — Act on field_attach_insert().
- [hook_field_attach_update()](hook_field_attach_update.md) — Act on field_attach_update().
- [hook_field_attach_preprocess_alter()](hook_field_attach_preprocess_alter.md) — Alter field_attach_preprocess() variables.
- [hook_field_attach_delete()](hook_field_attach_delete.md) — Act on field_attach_delete().
- [hook_field_attach_delete_revision()](hook_field_attach_delete_revision.md) — Act on field_attach_delete_revision().
- [hook_field_attach_purge()](hook_field_attach_purge.md) — Act on field_purge_data().
- [hook_field_attach_view_alter()](hook_field_attach_view_alter.md) — Perform alterations on field_attach_view() or field_view_field().
- [hook_field_attach_prepare_translation_alter()](hook_field_attach_prepare_translation_alter.md) — Perform alterations on field_attach_prepare_translation().
- [hook_field_language_alter()](hook_field_language_alter.md) — Perform alterations on field_language() values.
- [hook_field_available_languages_alter()](hook_field_available_languages_alter.md) — Alter field_available_languages() values.
- [hook_field_attach_create_bundle()](hook_field_attach_create_bundle.md) — Act on field_attach_create_bundle().
- [hook_field_attach_rename_bundle()](hook_field_attach_rename_bundle.md) — Act on field_attach_rename_bundle().
- [hook_field_attach_delete_bundle()](hook_field_attach_delete_bundle.md) — Act on field_attach_delete_bundle.
- [hook_field_storage_info()](hook_field_storage_info.md) — Expose Field API storage backends.
- [hook_field_storage_info_alter()](hook_field_storage_info_alter.md) — Perform alterations on Field API storage types.
- [hook_field_storage_details()](hook_field_storage_details.md) — Reveal the internal details about the storage for a field.
- [hook_field_storage_details_alter()](hook_field_storage_details_alter.md) — Perform alterations on Field API storage details.
- [hook_field_storage_load()](hook_field_storage_load.md) — Load field data for a set of entities.
- [hook_field_storage_write()](hook_field_storage_write.md) — Write field data for an entity.
- [hook_field_storage_delete()](hook_field_storage_delete.md) — Delete all field data for an entity.
- [hook_field_storage_delete_revision()](hook_field_storage_delete_revision.md) — Delete a single revision of field data for an entity.
- [hook_field_storage_query()](hook_field_storage_query.md) — Execute an EntityFieldQuery.
- [hook_field_storage_create_field()](hook_field_storage_create_field.md) — Act on creation of a new field.
- [hook_field_storage_delete_field()](hook_field_storage_delete_field.md) — Act on deletion of a field.
- [hook_field_storage_delete_instance()](hook_field_storage_delete_instance.md) — Act on deletion of a field instance.
- [hook_field_storage_pre_load()](hook_field_storage_pre_load.md) — Act before the storage backends load field data.
- [hook_field_storage_pre_insert()](hook_field_storage_pre_insert.md) — Act before the storage backends insert field data.
- [hook_field_storage_pre_update()](hook_field_storage_pre_update.md) — Act before the storage backends update field data.
- [hook_field_info_max_weight()](hook_field_info_max_weight.md) — Returns the maximum weight for the entity components handled by the module.
- [hook_field_display_alter()](hook_field_display_alter.md) — Alters the display settings of a field before it gets displayed.
- [hook_field_display_ENTITY_TYPE_alter()](hook_field_display_ENTITY_TYPE_alter.md) — Alters the display settings of a field on a given entity type before it gets displayed.
- [hook_field_extra_fields_display_alter()](hook_field_extra_fields_display_alter.md) — Alters the display settings of pseudo-fields before an entity is displayed.
- [hook_field_widget_properties_ENTITY_TYPE_alter()](hook_field_widget_properties_ENTITY_TYPE_alter.md) — Alters the widget properties of a field instance on a given entity type before it gets displayed.
- [hook_field_create_field()](hook_field_create_field.md) — Act on a field being created.
- [hook_field_create_instance()](hook_field_create_instance.md) — Act on a field instance being created.
- [hook_field_update_forbid()](hook_field_update_forbid.md) — Forbid a field update from occurring.
- [hook_field_update_field()](hook_field_update_field.md) — Act on a field being updated.
- [hook_field_delete_field()](hook_field_delete_field.md) — Act on a field being deleted.
- [hook_field_update_instance()](hook_field_update_instance.md) — Act on a field instance being updated.
- [hook_field_delete_instance()](hook_field_delete_instance.md) — Act on a field instance being deleted.
- [hook_field_read_field()](hook_field_read_field.md) — Act on field records being read from the database.
- [hook_field_read_instance()](hook_field_read_instance.md) — Act on a field record being read from the database.
- [hook_field_purge_field()](hook_field_purge_field.md) — Acts when a field record is being purged.
- [hook_field_purge_instance()](hook_field_purge_instance.md) — Acts when a field instance is being purged.
- [hook_field_storage_purge_field()](hook_field_storage_purge_field.md) — Remove field storage information when a field record is purged.
- [hook_field_storage_purge_field_instance()](hook_field_storage_purge_field_instance.md) — Remove field storage information when a field instance is purged.
- [hook_field_storage_purge()](hook_field_storage_purge.md) — Remove field storage information when field data is purged.
- [hook_field_access()](hook_field_access.md) — Determine whether the user has access to a given field.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
