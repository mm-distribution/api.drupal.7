# modules/simpletest/tests/entity_crud_hook_test.module

- **Source:** [local](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · 262 lines
- **Module/theme:** batch_test

## File documentation

```text
@file
Test module for the Entity CRUD API.
```

## Functions (derived index)

- [entity_crud_hook_test_entity_presave()](entity_crud_hook_test_entity_presave.md) — Implements hook_entity_presave().
- [entity_crud_hook_test_comment_presave()](entity_crud_hook_test_comment_presave.md) — Implements hook_comment_presave().
- [entity_crud_hook_test_file_presave()](entity_crud_hook_test_file_presave.md) — Implements hook_file_presave().
- [entity_crud_hook_test_node_presave()](entity_crud_hook_test_node_presave.md) — Implements hook_node_presave().
- [entity_crud_hook_test_taxonomy_term_presave()](entity_crud_hook_test_taxonomy_term_presave.md) — Implements hook_taxonomy_term_presave().
- [entity_crud_hook_test_taxonomy_vocabulary_presave()](entity_crud_hook_test_taxonomy_vocabulary_presave.md) — Implements hook_taxonomy_vocabulary_presave().
- [entity_crud_hook_test_user_presave()](entity_crud_hook_test_user_presave.md) — Implements hook_user_presave().
- [entity_crud_hook_test_entity_insert()](entity_crud_hook_test_entity_insert.md) — Implements hook_entity_insert().
- [entity_crud_hook_test_comment_insert()](entity_crud_hook_test_comment_insert.md) — Implements hook_comment_insert().
- [entity_crud_hook_test_file_insert()](entity_crud_hook_test_file_insert.md) — Implements hook_file_insert().
- [entity_crud_hook_test_node_insert()](entity_crud_hook_test_node_insert.md) — Implements hook_node_insert().
- [entity_crud_hook_test_taxonomy_term_insert()](entity_crud_hook_test_taxonomy_term_insert.md) — Implements hook_taxonomy_term_insert().
- [entity_crud_hook_test_taxonomy_vocabulary_insert()](entity_crud_hook_test_taxonomy_vocabulary_insert.md) — Implements hook_taxonomy_vocabulary_insert().
- [entity_crud_hook_test_user_insert()](entity_crud_hook_test_user_insert.md) — Implements hook_user_insert().
- [entity_crud_hook_test_entity_load()](entity_crud_hook_test_entity_load.md) — Implements hook_entity_load().
- [entity_crud_hook_test_comment_load()](entity_crud_hook_test_comment_load.md) — Implements hook_comment_load().
- [entity_crud_hook_test_file_load()](entity_crud_hook_test_file_load.md) — Implements hook_file_load().
- [entity_crud_hook_test_node_load()](entity_crud_hook_test_node_load.md) — Implements hook_node_load().
- [entity_crud_hook_test_taxonomy_term_load()](entity_crud_hook_test_taxonomy_term_load.md) — Implements hook_taxonomy_term_load().
- [entity_crud_hook_test_taxonomy_vocabulary_load()](entity_crud_hook_test_taxonomy_vocabulary_load.md) — Implements hook_taxonomy_vocabulary_load().
- [entity_crud_hook_test_user_load()](entity_crud_hook_test_user_load.md) — Implements hook_user_load().
- [entity_crud_hook_test_entity_update()](entity_crud_hook_test_entity_update.md) — Implements hook_entity_update().
- [entity_crud_hook_test_comment_update()](entity_crud_hook_test_comment_update.md) — Implements hook_comment_update().
- [entity_crud_hook_test_file_update()](entity_crud_hook_test_file_update.md) — Implements hook_file_update().
- [entity_crud_hook_test_node_update()](entity_crud_hook_test_node_update.md) — Implements hook_node_update().
- [entity_crud_hook_test_taxonomy_term_update()](entity_crud_hook_test_taxonomy_term_update.md) — Implements hook_taxonomy_term_update().
- [entity_crud_hook_test_taxonomy_vocabulary_update()](entity_crud_hook_test_taxonomy_vocabulary_update.md) — Implements hook_taxonomy_vocabulary_update().
- [entity_crud_hook_test_user_update()](entity_crud_hook_test_user_update.md) — Implements hook_user_update().
- [entity_crud_hook_test_entity_delete()](entity_crud_hook_test_entity_delete.md) — Implements hook_entity_delete().
- [entity_crud_hook_test_comment_delete()](entity_crud_hook_test_comment_delete.md) — Implements hook_comment_delete().
- [entity_crud_hook_test_file_delete()](entity_crud_hook_test_file_delete.md) — Implements hook_file_delete().
- [entity_crud_hook_test_node_delete()](entity_crud_hook_test_node_delete.md) — Implements hook_node_delete().
- [entity_crud_hook_test_taxonomy_term_delete()](entity_crud_hook_test_taxonomy_term_delete.md) — Implements hook_taxonomy_term_delete().
- [entity_crud_hook_test_taxonomy_vocabulary_delete()](entity_crud_hook_test_taxonomy_vocabulary_delete.md) — Implements hook_taxonomy_vocabulary_delete().
- [entity_crud_hook_test_user_delete()](entity_crud_hook_test_user_delete.md) — Implements hook_user_delete().
- [entity_crud_hook_test_entity_info_alter()](entity_crud_hook_test_entity_info_alter.md) — Implements hook_entity_info_alter().

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
