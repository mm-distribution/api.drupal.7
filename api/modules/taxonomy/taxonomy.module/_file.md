# modules/taxonomy/taxonomy.module

- **Source:** [local](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · 2073 lines
- **Module/theme:** taxonomy

## File documentation

```text
@file
Enables the organization of content into categories.
```

## Functions (derived index)

- [taxonomy_help()](taxonomy_help.md) — Implements hook_help().
- [taxonomy_permission()](taxonomy_permission.md) — Implements hook_permission().
- [taxonomy_entity_info()](taxonomy_entity_info.md) — Implements hook_entity_info().
- [taxonomy_term_uri()](taxonomy_term_uri.md) — Implements callback_entity_info_uri().
- [taxonomy_field_extra_fields()](taxonomy_field_extra_fields.md) — Implements hook_field_extra_fields().
- [taxonomy_select_nodes()](taxonomy_select_nodes.md) — Return nodes attached to a term across all field instances.
- [taxonomy_theme()](taxonomy_theme.md) — Implements hook_theme().
- [taxonomy_menu()](taxonomy_menu.md) — Implements hook_menu().
- [taxonomy_admin_paths()](taxonomy_admin_paths.md) — Implements hook_admin_paths().
- [taxonomy_term_edit_access()](taxonomy_term_edit_access.md) — Return edit access for a given term.
- [taxonomy_admin_vocabulary_title_callback()](taxonomy_admin_vocabulary_title_callback.md) — Returns the sanitized name of a vocabulary.
- [taxonomy_vocabulary_save()](taxonomy_vocabulary_save.md) — Saves a vocabulary.
- [taxonomy_vocabulary_delete()](taxonomy_vocabulary_delete.md) — Deletes a vocabulary.
- [taxonomy_taxonomy_vocabulary_update()](taxonomy_taxonomy_vocabulary_update.md) — Implements hook_taxonomy_vocabulary_update().
- [taxonomy_check_vocabulary_hierarchy()](taxonomy_check_vocabulary_hierarchy.md) — Checks and updates the hierarchy flag of a vocabulary.
- [taxonomy_term_save()](taxonomy_term_save.md) — Saves a term object to the database.
- [taxonomy_term_delete()](taxonomy_term_delete.md) — Delete a term.
- [taxonomy_term_show()](taxonomy_term_show.md) — Generates an array which displays a term detail page.
- [taxonomy_term_view_multiple()](taxonomy_term_view_multiple.md) — Constructs a drupal_render() style array from an array of loaded terms.
- [taxonomy_term_build_content()](taxonomy_term_build_content.md) — Builds a structured array representing the term's content.
- [taxonomy_term_view()](taxonomy_term_view.md) — Generate an array for rendering the given term.
- [template_preprocess_taxonomy_term()](template_preprocess_taxonomy_term.md) — Process variables for taxonomy-term.tpl.php.
- [taxonomy_term_is_page()](taxonomy_term_is_page.md) — Returns whether the current page is the page of the passed-in term.
- [taxonomy_terms_static_reset()](taxonomy_terms_static_reset.md) — Clear all static cache variables for terms.
- [taxonomy_vocabulary_static_reset()](taxonomy_vocabulary_static_reset.md) — Clear all static cache variables for vocabularies.
- [taxonomy_get_vocabularies()](taxonomy_get_vocabularies.md) — Return an array of all vocabulary objects.
- [taxonomy_vocabulary_get_names()](taxonomy_vocabulary_get_names.md) — Get names for all taxonomy vocabularies.
- [taxonomy_get_parents()](taxonomy_get_parents.md) — Finds all parents of a given term ID.
- [taxonomy_get_parents_all()](taxonomy_get_parents_all.md) — Find all ancestors of a given term ID.
- [taxonomy_get_children()](taxonomy_get_children.md) — Finds all children of a term ID.
- [taxonomy_get_tree()](taxonomy_get_tree.md) — Create a hierarchical representation of a vocabulary.
- [taxonomy_get_term_by_name()](taxonomy_get_term_by_name.md) — Try to map a string to an existing term, as for glossary use.
- [taxonomy_term_load_multiple()](taxonomy_term_load_multiple.md) — Load multiple taxonomy terms based on certain conditions.
- [taxonomy_vocabulary_load_multiple()](taxonomy_vocabulary_load_multiple.md) — Load multiple taxonomy vocabularies based on certain conditions.
- [taxonomy_vocabulary_load()](taxonomy_vocabulary_load.md) — Return the vocabulary object matching a vocabulary ID.
- [taxonomy_vocabulary_machine_name_load()](taxonomy_vocabulary_machine_name_load.md) — Return the vocabulary object matching a vocabulary machine name.
- [taxonomy_term_load()](taxonomy_term_load.md) — Return the term object matching a term ID.
- [_taxonomy_get_tid_from_term()](_taxonomy_get_tid_from_term.md) — Helper function for array_map purposes.
- [taxonomy_implode_tags()](taxonomy_implode_tags.md) — Implodes a list of tags of a certain vocabulary into a string.
- [taxonomy_field_info()](taxonomy_field_info.md) — Implements hook_field_info().
- [taxonomy_field_widget_info()](taxonomy_field_widget_info.md) — Implements hook_field_widget_info().
- [taxonomy_field_widget_info_alter()](taxonomy_field_widget_info_alter.md) — Implements hook_field_widget_info_alter().
- [taxonomy_options_list()](taxonomy_options_list.md) — Implements hook_options_list().
- [taxonomy_field_validate()](taxonomy_field_validate.md) — Implements hook_field_validate().
- [taxonomy_field_is_empty()](taxonomy_field_is_empty.md) — Implements hook_field_is_empty().
- [taxonomy_field_formatter_info()](taxonomy_field_formatter_info.md) — Implements hook_field_formatter_info().
- [taxonomy_field_formatter_view()](taxonomy_field_formatter_view.md) — Implements hook_field_formatter_view().
- [taxonomy_allowed_values()](taxonomy_allowed_values.md) — Returns the set of valid terms for a taxonomy field.
- [taxonomy_field_formatter_prepare_view()](taxonomy_field_formatter_prepare_view.md) — Implements hook_field_formatter_prepare_view().
- [taxonomy_term_title()](taxonomy_term_title.md) — Title callback: Returns the title of the taxonomy term.
- [taxonomy_field_widget_form()](taxonomy_field_widget_form.md) — Implements hook_field_widget_form().
- [taxonomy_autocomplete_validate()](taxonomy_autocomplete_validate.md) — Form element validate handler for taxonomy term autocomplete element.
- [taxonomy_field_widget_error()](taxonomy_field_widget_error.md) — Implements hook_field_widget_error().
- [taxonomy_field_settings_form()](taxonomy_field_settings_form.md) — Implements hook_field_settings_form().
- [taxonomy_rdf_mapping()](taxonomy_rdf_mapping.md) — Implements hook_rdf_mapping().
- [taxonomy_field_presave()](taxonomy_field_presave.md) — Implements hook_field_presave().
- [taxonomy_node_insert()](taxonomy_node_insert.md) — Implements hook_node_insert().
- [taxonomy_build_node_index()](taxonomy_build_node_index.md) — Builds and inserts taxonomy index entries for a given node.
- [taxonomy_node_update()](taxonomy_node_update.md) — Implements hook_node_update().
- [taxonomy_node_delete()](taxonomy_node_delete.md) — Implements hook_node_delete().
- [taxonomy_delete_node_index()](taxonomy_delete_node_index.md) — Deletes taxonomy index entries for a given node.
- [taxonomy_taxonomy_term_delete()](taxonomy_taxonomy_term_delete.md) — Implements hook_taxonomy_term_delete().
- [taxonomy_entity_query_alter()](taxonomy_entity_query_alter.md) — Implements hook_entity_query_alter().
- [taxonomy_file_download_access()](taxonomy_file_download_access.md) — Implements hook_file_download_access().

## Classes and interfaces (derived index)

- [TaxonomyTermController](TaxonomyTermController.md) — Controller class for taxonomy terms.
- [TaxonomyVocabularyController](TaxonomyVocabularyController.md) — Controller class for taxonomy vocabularies.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
