# modules/comment/comment.module

- **Source:** [local](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · 2761 lines
- **Module/theme:** comment

## File documentation

```text
@file
Enables users to comment on published content.

When enabled, the Drupal comment module creates a discussion
board for each Drupal node. Users can post comments to discuss
a forum topic, weblog post, story, collaborative book page, etc.
```

## Functions (derived index)

- [comment_help()](comment_help.md) — Implements hook_help().
- [comment_entity_info()](comment_entity_info.md) — Implements hook_entity_info().
- [comment_node_type_load()](comment_node_type_load.md) — Menu loader callback for Field UI paths.
- [comment_uri()](comment_uri.md) — Implements callback_entity_info_uri().
- [comment_field_extra_fields()](comment_field_extra_fields.md) — Implements hook_field_extra_fields().
- [comment_theme()](comment_theme.md) — Implements hook_theme().
- [comment_menu()](comment_menu.md) — Implements hook_menu().
- [comment_menu_alter()](comment_menu_alter.md) — Implements hook_menu_alter().
- [comment_count_unpublished()](comment_count_unpublished.md) — Returns a menu title which includes the number of unapproved comments.
- [comment_node_type_insert()](comment_node_type_insert.md) — Implements hook_node_type_insert().
- [comment_node_type_update()](comment_node_type_update.md) — Implements hook_node_type_update().
- [comment_node_type_delete()](comment_node_type_delete.md) — Implements hook_node_type_delete().
- [_comment_body_field_create()](_comment_body_field_create.md) — Creates a comment_body field instance for a given node type.
- [comment_permission()](comment_permission.md) — Implements hook_permission().
- [comment_block_info()](comment_block_info.md) — Implements hook_block_info().
- [comment_block_configure()](comment_block_configure.md) — Implements hook_block_configure().
- [comment_block_save()](comment_block_save.md) — Implements hook_block_save().
- [comment_block_view()](comment_block_view.md) — Implements hook_block_view().
- [comment_permalink()](comment_permalink.md) — Redirects comment links to the correct page depending on comment settings.
- [comment_get_recent()](comment_get_recent.md) — Find the most recent comments that are available to the current user.
- [comment_new_page_count()](comment_new_page_count.md) — Calculate page number for first new comment.
- [theme_comment_block()](theme_comment_block.md) — Returns HTML for a list of recent comments to be displayed in the comment block.
- [comment_node_view()](comment_node_view.md) — Implements hook_node_view().
- [comment_node_page_additions()](comment_node_page_additions.md) — Build the comment-related elements for node detail pages.
- [comment_get_thread()](comment_get_thread.md) — Retrieve comments for a thread.
- [comment_prepare_thread()](comment_prepare_thread.md) — Loop over comment thread, noting indentation level.
- [comment_view()](comment_view.md) — Generate an array for rendering the given comment.
- [comment_build_content()](comment_build_content.md) — Builds a structured array representing the comment's content.
- [comment_links()](comment_links.md) — Helper function, build links for an individual comment.
- [comment_view_multiple()](comment_view_multiple.md) — Construct a drupal_render() style array from an array of loaded comments.
- [comment_form_node_type_form_alter()](comment_form_node_type_form_alter.md) — Implements hook_form_FORM_ID_alter().
- [comment_form_node_form_alter()](comment_form_node_form_alter.md) — Implements hook_form_BASE_FORM_ID_alter().
- [comment_node_load()](comment_node_load.md) — Implements hook_node_load().
- [comment_node_prepare()](comment_node_prepare.md) — Implements hook_node_prepare().
- [comment_node_insert()](comment_node_insert.md) — Implements hook_node_insert().
- [comment_node_delete()](comment_node_delete.md) — Implements hook_node_delete().
- [comment_node_update_index()](comment_node_update_index.md) — Implements hook_node_update_index().
- [comment_update_index()](comment_update_index.md) — Implements hook_update_index().
- [comment_node_search_result()](comment_node_search_result.md) — Implements hook_node_search_result().
- [comment_user_cancel()](comment_user_cancel.md) — Implements hook_user_cancel().
- [comment_user_delete()](comment_user_delete.md) — Implements hook_user_delete().
- [comment_access()](comment_access.md) — Determines whether the current user has access to a particular comment.
- [comment_save()](comment_save.md) — Accepts a submission of new or changed comment content.
- [comment_delete()](comment_delete.md) — Delete a comment and all its replies.
- [comment_delete_multiple()](comment_delete_multiple.md) — Delete comments and all their replies.
- [comment_load_multiple()](comment_load_multiple.md) — Load comments from the database.
- [comment_load()](comment_load.md) — Load the entire comment by cid.
- [comment_num_new()](comment_num_new.md) — Get number of new comments for current user and specified node.
- [comment_get_display_ordinal()](comment_get_display_ordinal.md) — Get the display ordinal for a comment, starting from 0.
- [comment_get_display_page()](comment_get_display_page.md) — Return the page number for a comment.
- [comment_edit_page()](comment_edit_page.md) — Page callback for comment editing.
- [comment_forms()](comment_forms.md) — Implements hook_forms().
- [comment_form()](comment_form.md) — Generate the basic commenting form, for appending to a node or display on a separate page.
- [comment_form_build_preview()](comment_form_build_preview.md) — Build a preview from submitted form values.
- [comment_preview()](comment_preview.md) — Generate a comment preview.
- [comment_form_validate()](comment_form_validate.md) — Validate comment form submissions.
- [comment_submit()](comment_submit.md) — Prepare a comment for submission.
- [comment_form_submit_build_comment()](comment_form_submit_build_comment.md) — Updates the form state's comment entity by processing this submission's values.
- [comment_form_submit()](comment_form_submit.md) — Process comment form submissions; prepare the comment, store it, and set a redirection target.
- [template_preprocess_comment()](template_preprocess_comment.md) — Process variables for comment.tpl.php.
- [theme_comment_post_forbidden()](theme_comment_post_forbidden.md) — Returns HTML for a "you can't post comments" notice.
- [template_preprocess_comment_wrapper()](template_preprocess_comment_wrapper.md) — Process variables for comment-wrapper.tpl.php.
- [_comment_get_modes()](_comment_get_modes.md) — Return an array of viewing modes for comment listings.
- [_comment_per_page()](_comment_per_page.md) — Return an array of "comments per page" settings from which the user can choose.
- [_comment_update_node_statistics()](_comment_update_node_statistics.md) — Updates the comment statistics for a given node. This should be called any time a comment is added, deleted, or updated.
- [int2vancode()](int2vancode.md) — Generate vancode.
- [vancode2int()](vancode2int.md) — Decode vancode back to an integer.
- [comment_action_info()](comment_action_info.md) — Implements hook_action_info().
- [comment_publish_action()](comment_publish_action.md) — Publishes a comment.
- [comment_unpublish_action()](comment_unpublish_action.md) — Unpublishes a comment.
- [comment_unpublish_by_keyword_action()](comment_unpublish_by_keyword_action.md) — Unpublishes a comment if it contains certain keywords.
- [comment_unpublish_by_keyword_action_form()](comment_unpublish_by_keyword_action_form.md) — Form builder; Prepare a form for blacklisted keywords.
- [comment_unpublish_by_keyword_action_submit()](comment_unpublish_by_keyword_action_submit.md) — Process comment_unpublish_by_keyword_action_form form submissions.
- [comment_save_action()](comment_save_action.md) — Saves a comment.
- [comment_ranking()](comment_ranking.md) — Implements hook_ranking().
- [comment_rdf_mapping()](comment_rdf_mapping.md) — Implements hook_rdf_mapping().
- [comment_file_download_access()](comment_file_download_access.md) — Implements hook_file_download_access().

## Classes and interfaces (derived index)

- [CommentController](CommentController.md) — Controller class for comments.

## Constants

### COMMENT_NOT_PUBLISHED

- Line 15

```php
define('COMMENT_NOT_PUBLISHED', 0);
```

```text
Comment is awaiting approval.
```

### COMMENT_PUBLISHED

- Line 20

```php
define('COMMENT_PUBLISHED', 1);
```

```text
Comment is published.
```

### COMMENT_MODE_FLAT

- Line 25

```php
define('COMMENT_MODE_FLAT', 0);
```

```text
Comments are displayed in a flat list - expanded.
```

### COMMENT_MODE_THREADED

- Line 30

```php
define('COMMENT_MODE_THREADED', 1);
```

```text
Comments are displayed as a threaded list - expanded.
```

### COMMENT_ANONYMOUS_MAYNOT_CONTACT

- Line 35

```php
define('COMMENT_ANONYMOUS_MAYNOT_CONTACT', 0);
```

```text
Anonymous posters cannot enter their contact information.
```

### COMMENT_ANONYMOUS_MAY_CONTACT

- Line 40

```php
define('COMMENT_ANONYMOUS_MAY_CONTACT', 1);
```

```text
Anonymous posters may leave their contact information.
```

### COMMENT_ANONYMOUS_MUST_CONTACT

- Line 45

```php
define('COMMENT_ANONYMOUS_MUST_CONTACT', 2);
```

```text
Anonymous posters are required to leave their contact information.
```

### COMMENT_FORM_SEPARATE_PAGE

- Line 50

```php
define('COMMENT_FORM_SEPARATE_PAGE', 0);
```

```text
Comment form should be displayed on a separate page.
```

### COMMENT_FORM_BELOW

- Line 55

```php
define('COMMENT_FORM_BELOW', 1);
```

```text
Comment form should be shown below post or list of comments.
```

### COMMENT_NODE_HIDDEN

- Line 60

```php
define('COMMENT_NODE_HIDDEN', 0);
```

```text
Comments for this node are hidden.
```

### COMMENT_NODE_CLOSED

- Line 65

```php
define('COMMENT_NODE_CLOSED', 1);
```

```text
Comments for this node are closed.
```

### COMMENT_NODE_OPEN

- Line 70

```php
define('COMMENT_NODE_OPEN', 2);
```

```text
Comments for this node are open.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
