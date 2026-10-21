# Field CRUD API

- **Topic id:** `field_crud`
- **Defined in:** [`modules/field/field.crud.inc`](../modules/field/field.crud.inc/_file.md), line 8 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L8)

## Documentation

```text
@defgroup field_crud Field CRUD API
@{
Create, update, and delete Field API fields, bundles, and instances.

Modules use this API, often in hook_install(), to create custom
data structures. UI modules will use it to create a user interface.

The Field CRUD API uses
@link field Field API data structures @endlink.

See @link field Field API @endlink for information about the other parts of
the Field API.
```

## Members (derived, 26)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_field_write_instance()](../modules/field/field.crud.inc/_field_write_instance.md) (function) — Stores an instance record in the field configuration database.
- [field_create_field()](../modules/field/field.crud.inc/field_create_field.md) (function) — Creates a field.
- [field_create_instance()](../modules/field/field.crud.inc/field_create_instance.md) (function) — Creates an instance of a field, binding it to a bundle.
- [field_delete_field()](../modules/field/field.crud.inc/field_delete_field.md) (function) — Marks a field and its instances and data for deletion.
- [field_delete_instance()](../modules/field/field.crud.inc/field_delete_instance.md) (function) — Marks a field instance and its data for deletion.
- [field_read_field()](../modules/field/field.crud.inc/field_read_field.md) (function) — Reads a single field record directly from the database.
- [field_read_fields()](../modules/field/field.crud.inc/field_read_fields.md) (function) — Reads in fields that match an array of conditions.
- [field_read_instance()](../modules/field/field.crud.inc/field_read_instance.md) (function) — Reads a single instance record from the database.
- [field_read_instances()](../modules/field/field.crud.inc/field_read_instances.md) (function) — Reads in field instances that match an array of conditions.
- [field_retrieve_schema()](../modules/field/field.crud.inc/field_retrieve_schema.md) (function) — Retrieves the schema for a field.
- [field_update_field()](../modules/field/field.crud.inc/field_update_field.md) (function) — Updates a field.
- [field_update_instance()](../modules/field/field.crud.inc/field_update_instance.md) (function) — Updates an instance of a field.
- [hook_field_create_field()](../modules/field/field.api.php/hook_field_create_field.md) (function) — Act on a field being created.
- [hook_field_create_instance()](../modules/field/field.api.php/hook_field_create_instance.md) (function) — Act on a field instance being created.
- [hook_field_delete_field()](../modules/field/field.api.php/hook_field_delete_field.md) (function) — Act on a field being deleted.
- [hook_field_delete_instance()](../modules/field/field.api.php/hook_field_delete_instance.md) (function) — Act on a field instance being deleted.
- [hook_field_purge_field()](../modules/field/field.api.php/hook_field_purge_field.md) (function) — Acts when a field record is being purged.
- [hook_field_purge_instance()](../modules/field/field.api.php/hook_field_purge_instance.md) (function) — Acts when a field instance is being purged.
- [hook_field_read_field()](../modules/field/field.api.php/hook_field_read_field.md) (function) — Act on field records being read from the database.
- [hook_field_read_instance()](../modules/field/field.api.php/hook_field_read_instance.md) (function) — Act on a field record being read from the database.
- [hook_field_storage_purge()](../modules/field/field.api.php/hook_field_storage_purge.md) (function) — Remove field storage information when field data is purged.
- [hook_field_storage_purge_field()](../modules/field/field.api.php/hook_field_storage_purge_field.md) (function) — Remove field storage information when a field record is purged.
- [hook_field_storage_purge_field_instance()](../modules/field/field.api.php/hook_field_storage_purge_field_instance.md) (function) — Remove field storage information when a field instance is purged.
- [hook_field_update_field()](../modules/field/field.api.php/hook_field_update_field.md) (function) — Act on a field being updated.
- [hook_field_update_forbid()](../modules/field/field.api.php/hook_field_update_forbid.md) (function) — Forbid a field update from occurring.
- [hook_field_update_instance()](../modules/field/field.api.php/hook_field_update_instance.md) (function) — Act on a field instance being updated.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
