# modules/book/book.module

- **Source:** [local](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · 1441 lines
- **Module/theme:** book

## File documentation

```text
@file
Allows users to create and organize related content in an outline.
```

## Functions (derived index)

- [book_help()](book_help.md) — Implements hook_help().
- [book_theme()](book_theme.md) — Implements hook_theme().
- [book_permission()](book_permission.md) — Implements hook_permission().
- [book_node_view_link()](book_node_view_link.md) — Adds relevant book links to the node's links.
- [book_menu()](book_menu.md) — Implements hook_menu().
- [_book_outline_access()](_book_outline_access.md) — Access callback: Determines if the outline tab is accessible.
- [_book_outline_remove_access()](_book_outline_remove_access.md) — Access callback: Determines if the user can remove nodes from the outline.
- [_book_node_is_removable()](_book_node_is_removable.md) — Determines if a node can be removed from the book.
- [book_admin_paths()](book_admin_paths.md) — Implements hook_admin_paths().
- [book_entity_info_alter()](book_entity_info_alter.md) — Implements hook_entity_info_alter().
- [book_block_info()](book_block_info.md) — Implements hook_block_info().
- [book_block_view()](book_block_view.md) — Implements hook_block_view().
- [book_block_configure()](book_block_configure.md) — Implements hook_block_configure().
- [book_block_save()](book_block_save.md) — Implements hook_block_save().
- [theme_book_title_link()](theme_book_title_link.md) — Returns HTML for a link to a book title when used as a block title.
- [book_get_books()](book_get_books.md) — Returns an array of all books.
- [book_form_node_form_alter()](book_form_node_form_alter.md) — Implements hook_form_BASE_FORM_ID_alter() for node_form().
- [book_pick_book_nojs_submit()](book_pick_book_nojs_submit.md) — Form submission handler for node_form().
- [_book_parent_select()](_book_parent_select.md) — Builds the parent selection form element for the node form or outline tab.
- [_book_add_form_elements()](_book_add_form_elements.md) — Builds the common elements of the book form for the node and outline forms.
- [book_form_update()](book_form_update.md) — Renders a new parent page select element when the book selection changes.
- [_book_update_outline()](_book_update_outline.md) — Handles additions and updates to the book outline.
- [book_update_bid()](book_update_bid.md) — Updates the book ID of a page and its children when it moves to a new book.
- [book_get_flat_menu()](book_get_flat_menu.md) — Gets the book menu tree for a page and returns it as a linear array.
- [_book_flatten_menu()](_book_flatten_menu.md) — Recursively converts a tree of menu links to a flat array.
- [book_prev()](book_prev.md) — Fetches the menu link for the previous page of the book.
- [book_next()](book_next.md) — Fetches the menu link for the next page of the book.
- [book_children()](book_children.md) — Formats the menu links for the child pages of the current page.
- [book_menu_name()](book_menu_name.md) — Generates the corresponding menu name from a book ID.
- [book_node_load()](book_node_load.md) — Implements hook_node_load().
- [book_node_view()](book_node_view.md) — Implements hook_node_view().
- [book_page_alter()](book_page_alter.md) — Implements hook_page_alter().
- [book_node_presave()](book_node_presave.md) — Implements hook_node_presave().
- [book_node_insert()](book_node_insert.md) — Implements hook_node_insert().
- [book_node_update()](book_node_update.md) — Implements hook_node_update().
- [book_node_delete()](book_node_delete.md) — Implements hook_node_delete().
- [book_node_prepare()](book_node_prepare.md) — Implements hook_node_prepare().
- [_book_parent_depth_limit()](_book_parent_depth_limit.md) — Finds the depth limit for items in the parent select.
- [book_form_node_delete_confirm_alter()](book_form_node_delete_confirm_alter.md) — Implements hook_form_FORM_ID_alter() for node_delete_confirm().
- [_book_link_defaults()](_book_link_defaults.md) — Returns an array with default values for a book page's menu link.
- [template_preprocess_book_all_books_block()](template_preprocess_book_all_books_block.md) — Processes variables for book-all-books-block.tpl.php.
- [template_preprocess_book_navigation()](template_preprocess_book_navigation.md) — Processes variables for book-navigation.tpl.php.
- [_book_toc_recurse()](_book_toc_recurse.md) — Recursively processes and formats menu items for book_toc().
- [book_toc()](book_toc.md) — Returns an array of book pages in table of contents order.
- [template_preprocess_book_export_html()](template_preprocess_book_export_html.md) — Processes variables for book-export-html.tpl.php.
- [book_export_traverse()](book_export_traverse.md) — Traverses the book tree to build printable or exportable output.
- [book_node_export()](book_node_export.md) — Generates printer-friendly HTML for a node.
- [template_preprocess_book_node_export_html()](template_preprocess_book_node_export_html.md) — Processes variables for book-node-export-html.tpl.php.
- [book_type_is_allowed()](book_type_is_allowed.md) — Determine if a given node type is in the list of types allowed for books.
- [book_node_type_update()](book_node_type_update.md) — Implements hook_node_type_update().
- [book_link_load()](book_link_load.md) — Gets a book menu link by its menu link ID.
- [book_menu_subtree_data()](book_menu_subtree_data.md) — Gets the data representing a subtree of the book hierarchy.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
