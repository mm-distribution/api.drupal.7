# modules/field/field.attach.inc

- **Source:** [local](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · 1417 lines
- **Module/theme:** field

## File documentation

```text
@file
Field attach API, allowing entities (nodes, users, ...) to be 'fieldable'.
```

## Functions (derived index)

- [_field_invoke()](_field_invoke.md) — Invoke a field hook.
- [_field_invoke_multiple()](_field_invoke_multiple.md) — Invoke a field hook across fields on multiple entities.
- [_field_invoke_default()](_field_invoke_default.md) — Invoke field.module's version of a field hook.
- [_field_invoke_multiple_default()](_field_invoke_multiple_default.md) — Invoke field.module's version of a field hook on multiple entities.
- [_field_invoke_get_instances()](_field_invoke_get_instances.md) — Helper for _field_invoke(): retrieves a list of instances to operate on.
- [field_attach_form()](field_attach_form.md) — Add form elements for all fields for an entity to a form structure.
- [field_attach_load()](field_attach_load.md) — Loads fields for the current revisions of a group of entities.
- [field_attach_load_revision()](field_attach_load_revision.md) — Load all fields for previous versions of a group of entities.
- [field_attach_validate()](field_attach_validate.md) — Perform field validation against the field data in an entity.
- [field_attach_form_validate()](field_attach_form_validate.md) — Perform field validation against form-submitted field values.
- [field_attach_submit()](field_attach_submit.md) — Perform necessary operations on field data submitted by a form.
- [field_attach_presave()](field_attach_presave.md) — Perform necessary operations just before fields data get saved.
- [field_attach_insert()](field_attach_insert.md) — Save field data for a new entity.
- [field_attach_update()](field_attach_update.md) — Save field data for an existing entity.
- [field_attach_delete()](field_attach_delete.md) — Delete field data for an existing entity. This deletes all revisions of field data for the entity.
- [field_attach_delete_revision()](field_attach_delete_revision.md) — Delete field data for a single revision of an existing entity. The passed entity must have a revision id attribute.
- [field_attach_prepare_view()](field_attach_prepare_view.md) — Prepare field data prior to display.
- [field_attach_view()](field_attach_view.md) — Returns a renderable array for the fields on an entity.
- [field_attach_preprocess()](field_attach_preprocess.md) — Populate the template variables with the field values available for rendering.
- [field_attach_prepare_translation()](field_attach_prepare_translation.md) — Prepares an entity for translation.
- [field_attach_create_bundle()](field_attach_create_bundle.md) — Notify field.module that a new bundle was created.
- [field_attach_rename_bundle()](field_attach_rename_bundle.md) — Notify field.module that a bundle was renamed.
- [field_attach_delete_bundle()](field_attach_delete_bundle.md) — Notify field.module the a bundle was deleted.

## Classes and interfaces (derived index)

- [FieldValidationException](FieldValidationException.md) — Exception thrown by field_attach_validate() on field validation errors.

## Constants

### FIELD_STORAGE_UPDATE

- Line 58; topics: field_storage

```php
define('FIELD_STORAGE_UPDATE', 'update');
```

```text
Argument for an update operation.

This is used in hook_field_storage_write when updating an
existing entity.
```

### FIELD_STORAGE_INSERT

- Line 65; topics: field_storage

```php
define('FIELD_STORAGE_INSERT', 'insert');
```

```text
Argument for an insert operation.

This is used in hook_field_storage_write when inserting a new entity.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
