# modules/forum/forum.module

- **Source:** [local](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · 1398 lines
- **Module/theme:** forum

## File documentation

```text
@file
Provides discussion forums.
```

## Functions (derived index)

- [forum_help()](forum_help.md) — Implements hook_help().
- [forum_theme()](forum_theme.md) — Implements hook_theme().
- [forum_menu()](forum_menu.md) — Implements hook_menu().
- [forum_menu_local_tasks_alter()](forum_menu_local_tasks_alter.md) — Implements hook_menu_local_tasks_alter().
- [forum_entity_info_alter()](forum_entity_info_alter.md) — Implements hook_entity_info_alter().
- [forum_uri()](forum_uri.md) — Implements callback_entity_info_uri().
- [_forum_node_check_node_type()](_forum_node_check_node_type.md) — Checks whether a node can be used in a forum, based on its content type.
- [forum_node_view()](forum_node_view.md) — Implements hook_node_view().
- [forum_node_validate()](forum_node_validate.md) — Implements hook_node_validate().
- [forum_node_presave()](forum_node_presave.md) — Implements hook_node_presave().
- [forum_node_update()](forum_node_update.md) — Implements hook_node_update().
- [forum_node_insert()](forum_node_insert.md) — Implements hook_node_insert().
- [forum_node_delete()](forum_node_delete.md) — Implements hook_node_delete().
- [forum_node_load()](forum_node_load.md) — Implements hook_node_load().
- [forum_node_info()](forum_node_info.md) — Implements hook_node_info().
- [forum_permission()](forum_permission.md) — Implements hook_permission().
- [forum_taxonomy_term_delete()](forum_taxonomy_term_delete.md) — Implements hook_taxonomy_term_delete().
- [forum_comment_publish()](forum_comment_publish.md) — Implements hook_comment_publish().
- [forum_comment_update()](forum_comment_update.md) — Implements hook_comment_update().
- [forum_comment_unpublish()](forum_comment_unpublish.md) — Implements hook_comment_unpublish().
- [forum_comment_delete()](forum_comment_delete.md) — Implements hook_comment_delete().
- [forum_field_storage_pre_insert()](forum_field_storage_pre_insert.md) — Implements hook_field_storage_pre_insert().
- [forum_field_storage_pre_update()](forum_field_storage_pre_update.md) — Implements hook_field_storage_pre_update().
- [forum_form_taxonomy_form_vocabulary_alter()](forum_form_taxonomy_form_vocabulary_alter.md) — Implements hook_form_FORM_ID_alter() for taxonomy_form_vocabulary().
- [forum_form_taxonomy_form_term_alter()](forum_form_taxonomy_form_term_alter.md) — Implements hook_form_FORM_ID_alter() for taxonomy_form_term().
- [forum_form_node_form_alter()](forum_form_node_form_alter.md) — Implements hook_form_BASE_FORM_ID_alter() for node_form().
- [forum_block_info()](forum_block_info.md) — Implements hook_block_info().
- [forum_block_configure()](forum_block_configure.md) — Implements hook_block_configure().
- [forum_block_save()](forum_block_save.md) — Implements hook_block_save().
- [forum_block_view()](forum_block_view.md) — Implements hook_block_view().
- [forum_block_view_pre_render()](forum_block_view_pre_render.md) — Render API callback: Lists nodes based on the element's #query property.
- [forum_form()](forum_form.md) — Implements hook_form().
- [forum_forum_load()](forum_forum_load.md) — Returns a tree of all forums for a given taxonomy term ID.
- [_forum_topics_unread()](_forum_topics_unread.md) — Calculates the number of new posts in a forum that the user has not yet read.
- [forum_get_topics()](forum_get_topics.md) — Gets all the topics in a forum.
- [template_preprocess_forums()](template_preprocess_forums.md) — Preprocesses variables for forums.tpl.php.
- [template_preprocess_forum_list()](template_preprocess_forum_list.md) — Preprocesses variables for forum-list.tpl.php.
- [template_preprocess_forum_topic_list()](template_preprocess_forum_topic_list.md) — Preprocesses variables for forum-topic-list.tpl.php.
- [template_preprocess_forum_icon()](template_preprocess_forum_icon.md) — Preprocesses variables for forum-icon.tpl.php.
- [template_preprocess_forum_submitted()](template_preprocess_forum_submitted.md) — Preprocesses variables for forum-submitted.tpl.php.
- [_forum_user_last_visit()](_forum_user_last_visit.md) — Gets the last time the user viewed a node.
- [_forum_get_topic_order()](_forum_get_topic_order.md) — Gets topic sorting information based on an integer code.
- [_forum_update_forum_index()](_forum_update_forum_index.md) — Updates the taxonomy index for a given node.
- [forum_rdf_mapping()](forum_rdf_mapping.md) — Implements hook_rdf_mapping().

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
