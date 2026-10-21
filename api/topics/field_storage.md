# Field Storage API

- **Topic id:** `field_storage`
- **Defined in:** [`modules/field/field.attach.inc`](../modules/field/field.attach.inc/_file.md), line 32 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L32)

## Documentation

```text
@defgroup field_storage Field Storage API
@{
Implement a storage engine for Field API data.

The Field Attach API uses the Field Storage API to perform all "database
access". Each Field Storage API hook function defines a primitive database
operation such as read, write, or delete. The default field storage module,
field_sql_storage.module, uses the local SQL database to implement these
operations, but alternative field storage backends can choose to represent
the data in SQL differently or use a completely different storage mechanism
such as a cloud-based database.

Each field defines which storage backend it uses. The Drupal system variable
'field_storage_default' identifies the storage backend used by default.

See @link field Field API @endlink for information about the other parts of
the Field API.
```

## Members (derived, 20)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [hook_field_storage_create_field()](../modules/field/field.api.php/hook_field_storage_create_field.md) (function) — Act on creation of a new field.
- [hook_field_storage_delete()](../modules/field/field.api.php/hook_field_storage_delete.md) (function) — Delete all field data for an entity.
- [hook_field_storage_delete_field()](../modules/field/field.api.php/hook_field_storage_delete_field.md) (function) — Act on deletion of a field.
- [hook_field_storage_delete_instance()](../modules/field/field.api.php/hook_field_storage_delete_instance.md) (function) — Act on deletion of a field instance.
- [hook_field_storage_delete_revision()](../modules/field/field.api.php/hook_field_storage_delete_revision.md) (function) — Delete a single revision of field data for an entity.
- [hook_field_storage_details()](../modules/field/field.api.php/hook_field_storage_details.md) (function) — Reveal the internal details about the storage for a field.
- [hook_field_storage_details_alter()](../modules/field/field.api.php/hook_field_storage_details_alter.md) (function) — Perform alterations on Field API storage details.
- [hook_field_storage_info()](../modules/field/field.api.php/hook_field_storage_info.md) (function) — Expose Field API storage backends.
- [hook_field_storage_info_alter()](../modules/field/field.api.php/hook_field_storage_info_alter.md) (function) — Perform alterations on Field API storage types.
- [hook_field_storage_load()](../modules/field/field.api.php/hook_field_storage_load.md) (function) — Load field data for a set of entities.
- [hook_field_storage_pre_insert()](../modules/field/field.api.php/hook_field_storage_pre_insert.md) (function) — Act before the storage backends insert field data.
- [hook_field_storage_pre_load()](../modules/field/field.api.php/hook_field_storage_pre_load.md) (function) — Act before the storage backends load field data.
- [hook_field_storage_pre_update()](../modules/field/field.api.php/hook_field_storage_pre_update.md) (function) — Act before the storage backends update field data.
- [hook_field_storage_purge()](../modules/field/field.api.php/hook_field_storage_purge.md) (function) — Remove field storage information when field data is purged.
- [hook_field_storage_purge_field()](../modules/field/field.api.php/hook_field_storage_purge_field.md) (function) — Remove field storage information when a field record is purged.
- [hook_field_storage_purge_field_instance()](../modules/field/field.api.php/hook_field_storage_purge_field_instance.md) (function) — Remove field storage information when a field instance is purged.
- [hook_field_storage_query()](../modules/field/field.api.php/hook_field_storage_query.md) (function) — Execute an EntityFieldQuery.
- [hook_field_storage_write()](../modules/field/field.api.php/hook_field_storage_write.md) (function) — Write field data for an entity.
- [FIELD_STORAGE_INSERT](../modules/field/field.attach.inc/_file.md#field_storage_insert) (constant) — Argument for an insert operation.
- [FIELD_STORAGE_UPDATE](../modules/field/field.attach.inc/_file.md#field_storage_update) (constant) — Argument for an update operation.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
