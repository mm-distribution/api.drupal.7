# modules/field/field.install

- **Source:** [local](../../../../source/modules/field/field.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install) · 494 lines
- **Module/theme:** field

## File documentation

```text
@file
Install, update and uninstall functions for the field module.
```

## Functions (derived index)

- [field_schema()](field_schema.md) — Implements hook_schema().
- [_update_7000_field_create_field()](_update_7000_field_create_field.md) — Utility function: create a field by writing directly to the database.
- [_update_7000_field_delete_field()](_update_7000_field_delete_field.md) — Utility function: delete a field stored in SQL storage directly from the database.
- [_update_7000_field_delete_instance()](_update_7000_field_delete_instance.md) — Utility function: delete an instance and all its data of a field stored in SQL Storage.
- [_update_7000_field_read_fields()](_update_7000_field_read_fields.md) — Utility function: fetch all the field definitions from the database.
- [_update_7000_field_create_instance()](_update_7000_field_create_instance.md) — Utility function: write a field instance directly to the database.
- [field_update_7000()](field_update_7000.md) — Field update version placeholder.
- [field_update_7001()](field_update_7001.md) — Fix fields definitions created during the d6 to d7 upgrade path.
- [field_update_7002()](field_update_7002.md) — Split the all-inclusive field_bundle_settings variable per bundle.
- [field_update_7003()](field_update_7003.md) — Add the FieldInfo class to the class registry.
- [field_update_7004()](field_update_7004.md) — Grant the new "administer fields" permission to trusted users.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
