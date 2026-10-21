# Field Attach API

- **Topic id:** `field_attach`
- **Defined in:** [`modules/field/field.attach.inc`](../modules/field/field.attach.inc/_file.md), line 71 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L71)

## Documentation

```text
@defgroup field_attach Field Attach API
@{
Operate on Field API data attached to Drupal entities.

Field Attach API functions load, store, display, generate Field API
structures, and perform a variety of other functions for field data attached
to individual entities.

Field Attach API functions generally take $entity_type and $entity arguments
along with additional function-specific arguments. $entity_type is the type
of the fieldable entity, such as 'node' or 'user', and $entity is the entity
itself.

hook_entity_info() is the central place for entity types to define if and
how Field API should operate on their entity objects. Notably, the
'fieldable' property needs to be set to TRUE.

The Field Attach API uses the concept of bundles: the set of fields for a
given entity is defined on a per-bundle basis. The collection of bundles for
an entity type is defined its hook_entity_info() implementation. For
instance, node_entity_info() exposes each node type as its own bundle. This
means that the set of fields of a node is determined by the node type. The
Field API reads the bundle name for a given entity from a particular
property of the entity object, and hook_entity_info() defines which property
to use. For instance, node_entity_info() specifies:
@code $info['entity keys']['bundle'] = 'type'@endcode
This indicates that for a particular node object, the bundle name can be
found in $node->type. This property can be omitted if the entity type only
exposes a single bundle (all entities of this type have the same collection
of fields). This is the case for the 'user' entity type.

Most Field Attach API functions define a corresponding hook function that
allows any module to act on Field Attach operations for any entity after the
operation is complete, and access or modify all the field, form, or display
data for that entity and operation. For example, field_attach_view() invokes
hook_field_attach_view_alter(). These all-module hooks are distinct from
those of the Field Types API, such as hook_field_load(), that are only
invoked for the module that defines a specific field type.

field_attach_load(), field_attach_insert(), and field_attach_update() also
define pre-operation hooks, e.g. hook_field_attach_pre_load(). These hooks
run before the corresponding Field Storage API and Field Type API
operations. They allow modules to define additional storage locations (e.g.
denormalizing, mirroring) for field data on a per-field basis. They also
allow modules to take over field storage completely by instructing other
implementations of the same hook and the Field Storage API itself not to
operate on specified fields.

The pre-operation hooks do not make the Field Storage API irrelevant. The
Field Storage API is essentially the "fallback mechanism" for any fields
that aren't being intercepted explicitly by pre-operation hooks.

@link field_language Field Language API @endlink provides information about
the structure of field objects.

See @link field Field API @endlink for information about the other parts of
the Field API.
```

## Members (derived, 41)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_field_invoke()](../modules/field/field.attach.inc/_field_invoke.md) (function) — Invoke a field hook.
- [_field_invoke_default()](../modules/field/field.attach.inc/_field_invoke_default.md) (function) — Invoke field.module's version of a field hook.
- [_field_invoke_get_instances()](../modules/field/field.attach.inc/_field_invoke_get_instances.md) (function) — Helper for _field_invoke(): retrieves a list of instances to operate on.
- [_field_invoke_multiple()](../modules/field/field.attach.inc/_field_invoke_multiple.md) (function) — Invoke a field hook across fields on multiple entities.
- [_field_invoke_multiple_default()](../modules/field/field.attach.inc/_field_invoke_multiple_default.md) (function) — Invoke field.module's version of a field hook on multiple entities.
- [field_attach_create_bundle()](../modules/field/field.attach.inc/field_attach_create_bundle.md) (function) — Notify field.module that a new bundle was created.
- [field_attach_delete()](../modules/field/field.attach.inc/field_attach_delete.md) (function) — Delete field data for an existing entity. This deletes all revisions of field data for the entity.
- [field_attach_delete_bundle()](../modules/field/field.attach.inc/field_attach_delete_bundle.md) (function) — Notify field.module the a bundle was deleted.
- [field_attach_delete_revision()](../modules/field/field.attach.inc/field_attach_delete_revision.md) (function) — Delete field data for a single revision of an existing entity. The passed entity must have a revision id attribute.
- [field_attach_form()](../modules/field/field.attach.inc/field_attach_form.md) (function) — Add form elements for all fields for an entity to a form structure.
- [field_attach_form_validate()](../modules/field/field.attach.inc/field_attach_form_validate.md) (function) — Perform field validation against form-submitted field values.
- [field_attach_insert()](../modules/field/field.attach.inc/field_attach_insert.md) (function) — Save field data for a new entity.
- [field_attach_load()](../modules/field/field.attach.inc/field_attach_load.md) (function) — Loads fields for the current revisions of a group of entities.
- [field_attach_load_revision()](../modules/field/field.attach.inc/field_attach_load_revision.md) (function) — Load all fields for previous versions of a group of entities.
- [field_attach_prepare_translation()](../modules/field/field.attach.inc/field_attach_prepare_translation.md) (function) — Prepares an entity for translation.
- [field_attach_prepare_view()](../modules/field/field.attach.inc/field_attach_prepare_view.md) (function) — Prepare field data prior to display.
- [field_attach_preprocess()](../modules/field/field.attach.inc/field_attach_preprocess.md) (function) — Populate the template variables with the field values available for rendering.
- [field_attach_presave()](../modules/field/field.attach.inc/field_attach_presave.md) (function) — Perform necessary operations just before fields data get saved.
- [field_attach_rename_bundle()](../modules/field/field.attach.inc/field_attach_rename_bundle.md) (function) — Notify field.module that a bundle was renamed.
- [field_attach_submit()](../modules/field/field.attach.inc/field_attach_submit.md) (function) — Perform necessary operations on field data submitted by a form.
- [field_attach_update()](../modules/field/field.attach.inc/field_attach_update.md) (function) — Save field data for an existing entity.
- [field_attach_validate()](../modules/field/field.attach.inc/field_attach_validate.md) (function) — Perform field validation against the field data in an entity.
- [field_attach_view()](../modules/field/field.attach.inc/field_attach_view.md) (function) — Returns a renderable array for the fields on an entity.
- [hook_field_attach_create_bundle()](../modules/field/field.api.php/hook_field_attach_create_bundle.md) (function) — Act on field_attach_create_bundle().
- [hook_field_attach_delete()](../modules/field/field.api.php/hook_field_attach_delete.md) (function) — Act on field_attach_delete().
- [hook_field_attach_delete_bundle()](../modules/field/field.api.php/hook_field_attach_delete_bundle.md) (function) — Act on field_attach_delete_bundle.
- [hook_field_attach_delete_revision()](../modules/field/field.api.php/hook_field_attach_delete_revision.md) (function) — Act on field_attach_delete_revision().
- [hook_field_attach_form()](../modules/field/field.api.php/hook_field_attach_form.md) (function) — Act on field_attach_form().
- [hook_field_attach_insert()](../modules/field/field.api.php/hook_field_attach_insert.md) (function) — Act on field_attach_insert().
- [hook_field_attach_load()](../modules/field/field.api.php/hook_field_attach_load.md) (function) — Act on field_attach_load().
- [hook_field_attach_prepare_translation_alter()](../modules/field/field.api.php/hook_field_attach_prepare_translation_alter.md) (function) — Perform alterations on field_attach_prepare_translation().
- [hook_field_attach_preprocess_alter()](../modules/field/field.api.php/hook_field_attach_preprocess_alter.md) (function) — Alter field_attach_preprocess() variables.
- [hook_field_attach_presave()](../modules/field/field.api.php/hook_field_attach_presave.md) (function) — Act on field_attach_presave().
- [hook_field_attach_purge()](../modules/field/field.api.php/hook_field_attach_purge.md) (function) — Act on field_purge_data().
- [hook_field_attach_rename_bundle()](../modules/field/field.api.php/hook_field_attach_rename_bundle.md) (function) — Act on field_attach_rename_bundle().
- [hook_field_attach_submit()](../modules/field/field.api.php/hook_field_attach_submit.md) (function) — Act on field_attach_submit().
- [hook_field_attach_update()](../modules/field/field.api.php/hook_field_attach_update.md) (function) — Act on field_attach_update().
- [hook_field_attach_validate()](../modules/field/field.api.php/hook_field_attach_validate.md) (function) — Act on field_attach_validate().
- [hook_field_attach_view_alter()](../modules/field/field.api.php/hook_field_attach_view_alter.md) (function) — Perform alterations on field_attach_view() or field_view_field().
- [hook_field_available_languages_alter()](../modules/field/field.api.php/hook_field_available_languages_alter.md) (function) — Alter field_available_languages() values.
- [hook_field_language_alter()](../modules/field/field.api.php/hook_field_language_alter.md) (function) — Perform alterations on field_language() values.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
