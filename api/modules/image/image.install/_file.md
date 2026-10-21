# modules/image/image.install

- **Source:** [local](../../../../source/modules/image/image.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install) · 523 lines
- **Module/theme:** image

## File documentation

```text
@file
Install, update and uninstall functions for the image module.
```

## Functions (derived index)

- [image_install()](image_install.md) — Implements hook_install().
- [image_uninstall()](image_uninstall.md) — Implements hook_uninstall().
- [image_schema()](image_schema.md) — Implements hook_schema().
- [image_field_schema()](image_field_schema.md) — Implements hook_field_schema().
- [image_update_dependencies()](image_update_dependencies.md) — Implements hook_update_dependencies().
- [image_update_7000()](image_update_7000.md) — Install the schema for users upgrading from the contributed module.
- [image_update_7001()](image_update_7001.md) — Rename possibly misnamed {image_effect} table to {image_effects}.
- [_image_update_7002_add_columns()](_image_update_7002_add_columns.md) — Add width and height columns to a specific table.
- [_image_update_7002_populate_dimensions()](_image_update_7002_populate_dimensions.md) — Populate image dimensions in a specific table.
- [image_update_7002()](image_update_7002.md) — Add width and height columns to image field schema and populate.
- [image_update_7003()](image_update_7003.md) — Remove the variables that set alt and title length since they were not used for database column size and could cause PDO exceptions.
- [image_update_7004()](image_update_7004.md) — Use a large setting (512 and 1024 characters) for the length of the image alt and title fields.
- [image_update_7005()](image_update_7005.md) — Add a column to the 'image_style' table to store administrative labels.
- [image_requirements()](image_requirements.md) — Implements hook_requirements() to check the PHP GD Library.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
