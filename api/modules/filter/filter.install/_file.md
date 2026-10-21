# modules/filter/filter.install

- **Source:** [local](../../../../source/modules/filter/filter.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install) · 495 lines
- **Module/theme:** filter

## File documentation

```text
@file
Install, update, and uninstall functions for the Filter module.
```

## Functions (derived index)

- [filter_schema()](filter_schema.md) — Implements hook_schema().
- [filter_install()](filter_install.md) — Implements hook_install().
- [filter_update_dependencies()](filter_update_dependencies.md) — Implements hook_update_dependencies().
- [filter_update_7000()](filter_update_7000.md) — Upgrade the {filter_formats} table and rename it to {filter_format}.
- [filter_update_7001()](filter_update_7001.md) — Break out "escape HTML filter" option to its own filter.
- [filter_update_7003()](filter_update_7003.md) — Upgrade the {filter} table for core filters.
- [filter_update_7005()](filter_update_7005.md) — Integrate text formats with the user permissions system.
- [filter_update_7008()](filter_update_7008.md) — Grant usage of all text formats to user roles having the 'administer filters' permission.
- [filter_update_7009()](filter_update_7009.md) — Converts fields that store serialized variables from text to blob.
- [filter_update_7010()](filter_update_7010.md) — Change {filter_format}.format and {filter}.format into varchar.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
