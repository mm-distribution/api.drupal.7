# modules/field/modules/list/list.install

- **Source:** [local](../../../../../../source/modules/field/modules/list/list.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.install) · 146 lines
- **Module/theme:** list

## File documentation

```text
@file
Install, update and uninstall functions for the list module.
```

## Functions (derived index)

- [list_field_schema()](list_field_schema.md) — Implements hook_field_schema().
- [list_update_7001()](list_update_7001.md) — Rename the list field types and change 'allowed_values' format.
- [_list_update_7001_float_string_cast()](_list_update_7001_float_string_cast.md) — Helper callback function to cast the array element.
- [_list_update_7001_extract_allowed_values()](_list_update_7001_extract_allowed_values.md) — Helper function for list_update_7001: extract allowed values from a string.
- [list_update_7002()](list_update_7002.md) — Re-apply list_update_7001() for deleted fields.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
