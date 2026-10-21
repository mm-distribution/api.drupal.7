# modules/field/tests/field_test.module

- **Source:** [local](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · 285 lines
- **Module/theme:** field_test_schema_alter

## File documentation

```text
@file
Helper module for the Field API tests.

The module defines
- an entity type (field_test.entity.inc)
- a field type and its formatters and widgets (field_test.field.inc)
- a field storage backend (field_test.storage.inc)

The main field_test.module file implements generic hooks and provides some
test helper functions
```

## Functions (derived index)

- [field_test_permission()](field_test_permission.md) — Implements hook_permission().
- [field_test_menu()](field_test_menu.md) — Implements hook_menu().
- [field_test_field_test_op()](field_test_field_test_op.md) — Generic op to test _field_invoke behavior.
- [field_test_field_test_op_multiple()](field_test_field_test_op_multiple.md) — Generic op to test _field_invoke_multiple behavior.
- [field_test_field_available_languages_alter()](field_test_field_available_languages_alter.md) — Implements hook_field_available_languages_alter().
- [field_test_field_language_alter()](field_test_field_language_alter.md) — Implements hook_field_language_alter().
- [field_test_memorize()](field_test_memorize.md) — Store and retrieve keyed data for later verification by unit tests.
- [field_test_field_create_field()](field_test_field_create_field.md) — Memorize calls to hook_field_create_field().
- [field_test_entity_query_alter()](field_test_entity_query_alter.md) — Implements hook_entity_query_alter().
- [field_test_dummy_field_storage_query()](field_test_dummy_field_storage_query.md) — Pseudo-implements hook_field_storage_query().
- [field_test_entity_label_callback()](field_test_entity_label_callback.md) — Implements callback_entity_info_label().
- [field_test_field_attach_view_alter()](field_test_field_attach_view_alter.md) — Implements hook_field_attach_view_alter().
- [field_test_field_widget_properties_alter()](field_test_field_widget_properties_alter.md) — Implements hook_field_widget_properties_alter().
- [field_test_field_widget_properties_user_alter()](field_test_field_widget_properties_user_alter.md) — Implements hook_field_widget_properties_ENTITY_TYPE_alter().
- [field_test_field_widget_form_alter()](field_test_field_widget_form_alter.md) — Implements hook_field_widget_form_alter().
- [field_test_query_efq_table_prefixing_test_alter()](field_test_query_efq_table_prefixing_test_alter.md) — Implements hook_query_TAG_alter() for tag 'efq_table_prefixing_test'.
- [field_test_query_store_global_test_query_alter()](field_test_query_store_global_test_query_alter.md) — Implements hook_query_TAG_alter() for tag 'store_global_test_query'.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
