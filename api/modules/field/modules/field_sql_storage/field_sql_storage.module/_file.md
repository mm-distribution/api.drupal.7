# modules/field/modules/field_sql_storage/field_sql_storage.module

- **Source:** [local](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · 934 lines
- **Module/theme:** field_sql_storage

## File documentation

```text
@file
Default implementation of the field storage API.
```

## Functions (derived index)

- [field_sql_storage_help()](field_sql_storage_help.md) — Implements hook_help().
- [field_sql_storage_field_storage_info()](field_sql_storage_field_storage_info.md) — Implements hook_field_storage_info().
- [_field_sql_storage_tablename()](_field_sql_storage_tablename.md) — Generate a table name for a field data table.
- [_field_sql_storage_revision_tablename()](_field_sql_storage_revision_tablename.md) — Generate a table name for a field revision archive table.
- [_field_sql_storage_tablealias()](_field_sql_storage_tablealias.md) — Generates a table alias for a field data table.
- [_field_sql_storage_columnname()](_field_sql_storage_columnname.md) — Generate a column name for a field data table.
- [_field_sql_storage_indexname()](_field_sql_storage_indexname.md) — Generate an index name for a field data table.
- [_field_sql_storage_schema()](_field_sql_storage_schema.md) — Return the database schema for a field. This may contain one or more tables. Each table will contain the columns relevant for the specified field. Leave the $field's 'columns' and 'indexes' keys empty to get only the base schema.
- [field_sql_storage_field_storage_create_field()](field_sql_storage_field_storage_create_field.md) — Implements hook_field_storage_create_field().
- [field_sql_storage_field_update_forbid()](field_sql_storage_field_update_forbid.md) — Implements hook_field_update_forbid().
- [field_sql_storage_field_storage_update_field()](field_sql_storage_field_storage_update_field.md) — Implements hook_field_storage_update_field().
- [field_sql_storage_field_storage_delete_field()](field_sql_storage_field_storage_delete_field.md) — Implements hook_field_storage_delete_field().
- [field_sql_storage_field_storage_load()](field_sql_storage_field_storage_load.md) — Implements hook_field_storage_load().
- [_field_sql_storage_write_compare_filter_callback()](_field_sql_storage_write_compare_filter_callback.md) — Callback for array_filter().
- [_field_sql_storage_write_compare_filter()](_field_sql_storage_write_compare_filter.md) — Cleanup field values for later values comparison.
- [_field_sql_storage_write_compare()](_field_sql_storage_write_compare.md) — Compare a single field value for both entities and tell us if it changed.
- [field_sql_storage_field_storage_write()](field_sql_storage_field_storage_write.md) — Implements hook_field_storage_write().
- [field_sql_storage_field_storage_delete()](field_sql_storage_field_storage_delete.md) — Implements hook_field_storage_delete().
- [field_sql_storage_field_storage_purge()](field_sql_storage_field_storage_purge.md) — Implements hook_field_storage_purge().
- [field_sql_storage_field_storage_query()](field_sql_storage_field_storage_query.md) — Implements hook_field_storage_query().
- [_field_sql_storage_query_join_entity()](_field_sql_storage_query_join_entity.md) — Adds the base entity table to a field query object.
- [_field_sql_storage_query_field_conditions()](_field_sql_storage_query_field_conditions.md) — Adds field (meta) conditions to the given query objects respecting groupings.
- [_field_sql_storage_query_columnname()](_field_sql_storage_query_columnname.md) — Field meta condition column callback.
- [field_sql_storage_field_storage_delete_revision()](field_sql_storage_field_storage_delete_revision.md) — Implements hook_field_storage_delete_revision().
- [field_sql_storage_field_storage_delete_instance()](field_sql_storage_field_storage_delete_instance.md) — Implements hook_field_storage_delete_instance().
- [field_sql_storage_field_attach_rename_bundle()](field_sql_storage_field_attach_rename_bundle.md) — Implements hook_field_attach_rename_bundle().
- [field_sql_storage_field_storage_purge_field()](field_sql_storage_field_storage_purge_field.md) — Implements hook_field_storage_purge_field().
- [field_sql_storage_field_storage_details()](field_sql_storage_field_storage_details.md) — Implements hook_field_storage_details().

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
