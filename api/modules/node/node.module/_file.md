# modules/node/node.module

- **Source:** [local](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · 4202 lines
- **Module/theme:** node

## File documentation

```text
@file
The core that allows content to be submitted to the site. Modules and
scripts may programmatically submit nodes using the usual form API pattern.
```

## Functions (derived index)

- [node_help()](node_help.md) — Implements hook_help().
- [node_theme()](node_theme.md) — Implements hook_theme().
- [node_cron()](node_cron.md) — Implements hook_cron().
- [node_entity_info()](node_entity_info.md) — Implements hook_entity_info().
- [node_field_display_node_alter()](node_field_display_node_alter.md) — Implements hook_field_display_ENTITY_TYPE_alter().
- [node_uri()](node_uri.md) — Implements callback_entity_info_uri().
- [node_admin_paths()](node_admin_paths.md) — Implements hook_admin_paths().
- [node_title_list()](node_title_list.md) — Gathers a listing of links to nodes.
- [node_tag_new()](node_tag_new.md) — Updates the 'last viewed' timestamp of the specified node for current user.
- [node_last_viewed()](node_last_viewed.md) — Retrieves the timestamp for the current user's last view of a specified node.
- [node_mark()](node_mark.md) — Determines the type of marker to be displayed for a given node.
- [_node_extract_type()](_node_extract_type.md) — Extracts the type name.
- [node_type_get_types()](node_type_get_types.md) — Returns a list of all the available node types.
- [node_type_get_type()](node_type_get_type.md) — Returns the node type of the passed node or node type string.
- [node_type_get_base()](node_type_get_base.md) — Returns the node type base of the passed node or node type string.
- [node_type_get_names()](node_type_get_names.md) — Returns a list of available node type names.
- [node_type_get_name()](node_type_get_name.md) — Returns the node type name of the passed node or node type string.
- [node_types_rebuild()](node_types_rebuild.md) — Updates the database cache of node types.
- [node_type_load()](node_type_load.md) — Menu argument loader: loads a node type by string.
- [node_type_save()](node_type_save.md) — Saves a node type to the database.
- [node_add_body_field()](node_add_body_field.md) — Adds default body field to a node type.
- [node_field_extra_fields()](node_field_extra_fields.md) — Implements hook_field_extra_fields().
- [node_type_delete()](node_type_delete.md) — Deletes a node type from the database.
- [node_type_update_nodes()](node_type_update_nodes.md) — Updates all nodes of one type to be of another type.
- [_node_types_build()](_node_types_build.md) — Builds and returns the list of available node types.
- [node_type_cache_reset()](node_type_cache_reset.md) — Clears the node type cache.
- [node_type_set_defaults()](node_type_set_defaults.md) — Sets the default values for a node type.
- [node_rdf_mapping()](node_rdf_mapping.md) — Implements hook_rdf_mapping().
- [node_hook()](node_hook.md) — Determines whether a node hook exists.
- [node_invoke()](node_invoke.md) — Invokes a node hook.
- [node_load_multiple()](node_load_multiple.md) — Loads node entities from the database.
- [node_load()](node_load.md) — Loads a node object from the database.
- [node_object_prepare()](node_object_prepare.md) — Prepares a node object for editing.
- [node_validate()](node_validate.md) — Implements hook_validate().
- [node_submit()](node_submit.md) — Prepares node for saving by populating author and creation date.
- [node_save()](node_save.md) — Saves changes to a node or adds a new node.
- [_node_save_revision()](_node_save_revision.md) — Helper function to save a revision with the uid of the current user.
- [node_delete()](node_delete.md) — Deletes a node.
- [node_delete_multiple()](node_delete_multiple.md) — Deletes multiple nodes.
- [node_revision_delete()](node_revision_delete.md) — Deletes a node revision.
- [node_view()](node_view.md) — Generates an array for rendering the given node.
- [node_build_content()](node_build_content.md) — Builds a structured array representing the node's content.
- [node_show()](node_show.md) — Generates an array which displays a node detail page.
- [node_is_page()](node_is_page.md) — Returns whether the current page is the full page view of the passed-in node.
- [template_preprocess_node()](template_preprocess_node.md) — Processes variables for node.tpl.php
- [node_permission()](node_permission.md) — Implements hook_permission().
- [_node_rankings()](_node_rankings.md) — Gathers the rankings from the hook_ranking() implementations.
- [node_search_info()](node_search_info.md) — Implements hook_search_info().
- [node_search_access()](node_search_access.md) — Implements hook_search_access().
- [node_search_reset()](node_search_reset.md) — Implements hook_search_reset().
- [node_search_status()](node_search_status.md) — Implements hook_search_status().
- [node_search_admin()](node_search_admin.md) — Implements hook_search_admin().
- [node_search_execute()](node_search_execute.md) — Implements hook_search_execute().
- [node_ranking()](node_ranking.md) — Implements hook_ranking().
- [node_user_cancel()](node_user_cancel.md) — Implements hook_user_cancel().
- [node_user_delete()](node_user_delete.md) — Implements hook_user_delete().
- [theme_node_search_admin()](theme_node_search_admin.md) — Returns HTML for the content ranking part of the search settings admin page.
- [_node_revision_access()](_node_revision_access.md) — Access callback: Checks node revision access.
- [_node_add_access()](_node_add_access.md) — Access callback: Checks whether the user has permission to add a node.
- [node_menu()](node_menu.md) — Implements hook_menu().
- [node_menu_local_tasks_alter()](node_menu_local_tasks_alter.md) — Implements hook_menu_local_tasks_alter().
- [node_type_page_title()](node_type_page_title.md) — Title callback: Returns the unsanitized title of the node type edit form.
- [node_page_title()](node_page_title.md) — Title callback: Returns the title of the node.
- [node_last_changed()](node_last_changed.md) — Finds the last time a node was changed.
- [node_revision_list()](node_revision_list.md) — Returns a list of all the existing revision numbers.
- [node_block_info()](node_block_info.md) — Implements hook_block_info().
- [node_block_view()](node_block_view.md) — Implements hook_block_view().
- [node_block_configure()](node_block_configure.md) — Implements hook_block_configure().
- [node_block_save()](node_block_save.md) — Implements hook_block_save().
- [node_get_recent()](node_get_recent.md) — Finds the most recently changed nodes that are available to the current user.
- [theme_node_recent_block()](theme_node_recent_block.md) — Returns HTML for a list of recent content.
- [theme_node_recent_content()](theme_node_recent_content.md) — Returns HTML for a recent node to be displayed in the recent content block.
- [node_form_block_add_block_form_alter()](node_form_block_add_block_form_alter.md) — Implements hook_form_FORMID_alter().
- [node_form_block_admin_configure_alter()](node_form_block_admin_configure_alter.md) — Implements hook_form_FORMID_alter().
- [node_form_block_admin_configure_submit()](node_form_block_admin_configure_submit.md) — Form submission handler for node_form_block_admin_configure_alter().
- [node_form_block_custom_block_delete_alter()](node_form_block_custom_block_delete_alter.md) — Implements hook_form_FORMID_alter().
- [node_form_block_custom_block_delete_submit()](node_form_block_custom_block_delete_submit.md) — Form submission handler for node_form_block_custom_block_delete_alter().
- [node_modules_uninstalled()](node_modules_uninstalled.md) — Implements hook_modules_uninstalled().
- [node_block_list_alter()](node_block_list_alter.md) — Implements hook_block_list_alter().
- [node_feed()](node_feed.md) — Generates and prints an RSS feed.
- [node_view_multiple()](node_view_multiple.md) — Constructs a drupal_render() style array from an array of loaded nodes.
- [node_page_default()](node_page_default.md) — Menu callback: Generates a listing of promoted nodes.
- [node_page_view()](node_page_view.md) — Menu callback: Displays a single node.
- [node_update_index()](node_update_index.md) — Implements hook_update_index().
- [_node_index_node()](_node_index_node.md) — Indexes a single node.
- [node_form_search_form_alter()](node_form_search_form_alter.md) — Implements hook_form_FORM_ID_alter().
- [node_search_validate()](node_search_validate.md) — Form validation handler for node_form_alter().
- [node_access()](node_access.md) — Determines whether the current user may perform the operation on the node.
- [node_add_node_grants_to_query()](node_add_node_grants_to_query.md) — Helper function to create the or condition for a node grants check.
- [node_node_access()](node_node_access.md) — Implements hook_node_access().
- [node_list_permissions()](node_list_permissions.md) — Helper function to generate standard node permission list for a given type.
- [node_permissions_get_configured_types()](node_permissions_get_configured_types.md) — Returns an array of node types that should be managed by permissions.
- [node_access_grants()](node_access_grants.md) — Fetches an array of permission IDs granted to the given user ID.
- [node_access_view_all_nodes()](node_access_view_all_nodes.md) — Determines whether the user has a global viewing grant for all nodes.
- [node_query_node_access_alter()](node_query_node_access_alter.md) — Implements hook_query_TAG_alter().
- [node_query_entity_field_access_alter()](node_query_entity_field_access_alter.md) — Implements hook_query_TAG_alter().
- [_node_query_node_access_alter()](_node_query_node_access_alter.md) — Helper for node access functions.
- [node_access_acquire_grants()](node_access_acquire_grants.md) — Gets the list of node access grants and writes them to the database.
- [node_access_write_grants()](node_access_write_grants.md) — Writes a list of grants to the database, deleting any previously saved ones.
- [node_access_needs_rebuild()](node_access_needs_rebuild.md) — Flags or unflags the node access grants for rebuilding.
- [node_access_rebuild()](node_access_rebuild.md) — Rebuilds the node access database.
- [_node_access_rebuild_batch_operation()](_node_access_rebuild_batch_operation.md) — Implements callback_batch_operation().
- [_node_access_rebuild_batch_finished()](_node_access_rebuild_batch_finished.md) — Implements callback_batch_finished().
- [node_content_form()](node_content_form.md) — Implements hook_form().
- [node_forms()](node_forms.md) — Implements hook_forms().
- [node_action_info()](node_action_info.md) — Implements hook_action_info().
- [node_publish_action()](node_publish_action.md) — Sets the status of a node to 1 (published).
- [node_unpublish_action()](node_unpublish_action.md) — Sets the status of a node to 0 (unpublished).
- [node_make_sticky_action()](node_make_sticky_action.md) — Sets the sticky-at-top-of-list property of a node to 1.
- [node_make_unsticky_action()](node_make_unsticky_action.md) — Sets the sticky-at-top-of-list property of a node to 0.
- [node_promote_action()](node_promote_action.md) — Sets the promote property of a node to 1.
- [node_unpromote_action()](node_unpromote_action.md) — Sets the promote property of a node to 0.
- [node_save_action()](node_save_action.md) — Saves a node.
- [node_assign_owner_action()](node_assign_owner_action.md) — Assigns ownership of a node to a user.
- [node_assign_owner_action_form()](node_assign_owner_action_form.md) — Generates the settings form for node_assign_owner_action().
- [node_assign_owner_action_validate()](node_assign_owner_action_validate.md) — Validates settings form for node_assign_owner_action().
- [node_assign_owner_action_submit()](node_assign_owner_action_submit.md) — Saves settings form for node_assign_owner_action().
- [node_unpublish_by_keyword_action_form()](node_unpublish_by_keyword_action_form.md) — Generates settings form for node_unpublish_by_keyword_action().
- [node_unpublish_by_keyword_action_submit()](node_unpublish_by_keyword_action_submit.md) — Saves settings form for node_unpublish_by_keyword_action().
- [node_unpublish_by_keyword_action()](node_unpublish_by_keyword_action.md) — Unpublishes a node containing certain keywords.
- [node_requirements()](node_requirements.md) — Implements hook_requirements().
- [node_modules_enabled()](node_modules_enabled.md) — Implements hook_modules_enabled().
- [node_file_download_access()](node_file_download_access.md) — Implements hook_file_download_access().

## Classes and interfaces (derived index)

- [NodeController](NodeController.md) — Controller class for nodes.

## Constants

### NODE_NOT_PUBLISHED

- Line 12

```php
define('NODE_NOT_PUBLISHED', 0);
```

```text
Node is not published.
```

### NODE_PUBLISHED

- Line 17

```php
define('NODE_PUBLISHED', 1);
```

```text
Node is published.
```

### NODE_NOT_PROMOTED

- Line 22

```php
define('NODE_NOT_PROMOTED', 0);
```

```text
Node is not promoted to front page.
```

### NODE_PROMOTED

- Line 27

```php
define('NODE_PROMOTED', 1);
```

```text
Node is promoted to front page.
```

### NODE_NOT_STICKY

- Line 32

```php
define('NODE_NOT_STICKY', 0);
```

```text
Node is not sticky at top of the page.
```

### NODE_STICKY

- Line 37

```php
define('NODE_STICKY', 1);
```

```text
Node is sticky at top of the page.
```

### NODE_NEW_LIMIT

- Line 45

```php
define('NODE_NEW_LIMIT', REQUEST_TIME - 30 * 24 * 60 * 60);
```

```text
Nodes changed before this time are always marked as read.

Nodes changed after this time may be marked new, updated, or read, depending
on their state for the current user. Defaults to 30 days ago.
```

### NODE_ACCESS_ALLOW

- Line 50

```php
define('NODE_ACCESS_ALLOW', 'allow');
```

```text
Modules should return this value from hook_node_access() to allow access to a node.
```

### NODE_ACCESS_DENY

- Line 55

```php
define('NODE_ACCESS_DENY', 'deny');
```

```text
Modules should return this value from hook_node_access() to deny access to a node.
```

### NODE_ACCESS_IGNORE

- Line 60

```php
define('NODE_ACCESS_IGNORE', NULL);
```

```text
Modules should return this value from hook_node_access() to not affect node access.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
