# modules/node/tests/node_access_test.module

- **Source:** [local](../../../../../source/modules/node/tests/node_access_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module) · 231 lines
- **Module/theme:** node_test

## File documentation

```text
@file
A dummy module implementing node access related hooks for testing purposes.

A dummy module implementing node access related hooks to test API interaction
with the Node module. This module restricts view permission to those with
a special 'node test view' permission.
```

## Functions (derived index)

- [node_access_test_node_grants()](node_access_test_node_grants.md) — Implements hook_node_grants().
- [node_access_test_node_access_records()](node_access_test_node_access_records.md) — Implements hook_node_access_records().
- [node_access_test_permission()](node_access_test_permission.md) — Implements hook_permission().
- [node_access_test_menu()](node_access_test_menu.md) — Implements hook_menu().
- [node_access_test_page()](node_access_test_page.md) — Page callback for node access test page.
- [node_access_entity_test_page()](node_access_entity_test_page.md) — Page callback for node access entity test page.
- [node_access_test_form_node_form_alter()](node_access_test_form_node_form_alter.md) — Implements hook_form_BASE_FORM_ID_alter().
- [node_access_test_node_load()](node_access_test_node_load.md) — Implements hook_node_load().
- [node_access_test_node_delete()](node_access_test_node_delete.md) — Implements hook_node_delete().
- [node_access_test_node_insert()](node_access_test_node_insert.md) — Implements hook_node_insert().
- [node_access_test_node_update()](node_access_test_node_update.md) — Implements hook_node_update().
- [_node_access_test_node_write()](_node_access_test_node_write.md) — Helper for node insert/update.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
