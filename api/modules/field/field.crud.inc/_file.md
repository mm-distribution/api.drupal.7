# modules/field/field.crud.inc

- **Source:** [local](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · 1027 lines
- **Module/theme:** field

## File documentation

```text
@file
Field CRUD API, handling field and field instance creation and deletion.
```

## Functions (derived index)

- [field_retrieve_schema()](field_retrieve_schema.md) — Retrieves the schema for a field.
- [field_create_field()](field_create_field.md) — Creates a field.
- [field_update_field()](field_update_field.md) — Updates a field.
- [field_read_field()](field_read_field.md) — Reads a single field record directly from the database.
- [field_read_fields()](field_read_fields.md) — Reads in fields that match an array of conditions.
- [field_delete_field()](field_delete_field.md) — Marks a field and its instances and data for deletion.
- [field_create_instance()](field_create_instance.md) — Creates an instance of a field, binding it to a bundle.
- [field_update_instance()](field_update_instance.md) — Updates an instance of a field.
- [_field_write_instance()](_field_write_instance.md) — Stores an instance record in the field configuration database.
- [field_read_instance()](field_read_instance.md) — Reads a single instance record from the database.
- [field_read_instances()](field_read_instances.md) — Reads in field instances that match an array of conditions.
- [field_delete_instance()](field_delete_instance.md) — Marks a field instance and its data for deletion.
- [field_purge_batch()](field_purge_batch.md) — Purges a batch of deleted Field API data, instances, or fields.
- [field_purge_data()](field_purge_data.md) — Purges the field data for a single field on a single pseudo-entity.
- [field_purge_instance()](field_purge_instance.md) — Purges a field instance record from the database.
- [field_purge_field()](field_purge_field.md) — Purges a field record from the database.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
