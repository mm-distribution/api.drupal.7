# modules/taxonomy/taxonomy.install

- **Source:** [local](../../../../source/modules/taxonomy/taxonomy.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install) · 940 lines
- **Module/theme:** taxonomy

## File documentation

```text
@file
Install, update and uninstall functions for the taxonomy module.
```

## Functions (derived index)

- [taxonomy_uninstall()](taxonomy_uninstall.md) — Implements hook_uninstall().
- [taxonomy_schema()](taxonomy_schema.md) — Implements hook_schema().
- [taxonomy_field_schema()](taxonomy_field_schema.md) — Implements hook_field_schema().
- [taxonomy_update_dependencies()](taxonomy_update_dependencies.md) — Implements hook_update_dependencies().
- [_update_7002_taxonomy_get_vocabularies()](_update_7002_taxonomy_get_vocabularies.md) — Utility function: get the list of vocabularies directly from the database.
- [taxonomy_update_7001()](taxonomy_update_7001.md) — Rename taxonomy tables.
- [taxonomy_update_7002()](taxonomy_update_7002.md) — Add {vocabulary}.machine_name column.
- [taxonomy_update_7003()](taxonomy_update_7003.md) — Remove the related terms setting from vocabularies.
- [taxonomy_update_7004()](taxonomy_update_7004.md) — Move taxonomy vocabulary associations for nodes to fields and field instances.
- [taxonomy_update_7005()](taxonomy_update_7005.md) — Migrate {taxonomy_term_node} table to field storage.
- [taxonomy_update_7006()](taxonomy_update_7006.md) — Add {taxonomy_term_data}.format column.
- [taxonomy_update_7007()](taxonomy_update_7007.md) — Add index on {taxonomy_term_data}.name column to speed up taxonomy_get_term_by_name().
- [taxonomy_update_7008()](taxonomy_update_7008.md) — Change the weight columns to normal int.
- [taxonomy_update_7009()](taxonomy_update_7009.md) — Change {taxonomy_term_data}.format into varchar.
- [taxonomy_update_7010()](taxonomy_update_7010.md) — Change {taxonomy_index}.created to support signed int.
- [taxonomy_update_7011()](taxonomy_update_7011.md) — Drop unpublished nodes from the index.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
