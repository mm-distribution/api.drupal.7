# modules/menu/menu.module

- **Source:** [local](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · 865 lines
- **Module/theme:** menu

## File documentation

```text
@file
Allows administrators to customize the site's navigation menus.

A menu (in this context) is a hierarchical collection of links, generally
used for navigation. This is not to be confused with the
@link menu Menu system @endlink of menu.inc and hook_menu(), which defines
page routing requests for Drupal, and also allows the defined page routing
URLs to be added to the main site navigation menu.
```

## Functions (derived index)

- [menu_help()](menu_help.md) — Implements hook_help().
- [menu_permission()](menu_permission.md) — Implements hook_permission().
- [menu_menu()](menu_menu.md) — Implements hook_menu().
- [menu_theme()](menu_theme.md) — Implements hook_theme().
- [menu_enable()](menu_enable.md) — Implements hook_enable().
- [menu_overview_title()](menu_overview_title.md) — Title callback for the menu overview page and links.
- [menu_load()](menu_load.md) — Load the data for a single custom menu.
- [menu_load_all()](menu_load_all.md) — Load all custom menu data.
- [menu_save()](menu_save.md) — Save a custom menu.
- [menu_delete()](menu_delete.md) — Delete a custom menu and all contained links.
- [menu_parent_options()](menu_parent_options.md) — Return a list of menu items that are valid possible parents for the given menu item.
- [menu_parent_options_js()](menu_parent_options_js.md) — Page callback. Get all the available menus and menu items as a JavaScript array.
- [_menu_get_options()](_menu_get_options.md) — Helper function to get the items of the given menu.
- [_menu_parents_recurse()](_menu_parents_recurse.md) — Recursive helper function for menu_parent_options().
- [menu_add_link_labels()](menu_add_link_labels.md) — Adds labels to the title of a hidden, unpublished or logged-in menu link.
- [menu_reset_item()](menu_reset_item.md) — Reset a system-defined menu link.
- [menu_block_info()](menu_block_info.md) — Implements hook_block_info().
- [menu_block_view()](menu_block_view.md) — Implements hook_block_view().
- [menu_block_view_alter()](menu_block_view_alter.md) — Implements hook_block_view_alter().
- [menu_node_insert()](menu_node_insert.md) — Implements hook_node_insert().
- [menu_node_update()](menu_node_update.md) — Implements hook_node_update().
- [menu_node_save()](menu_node_save.md) — Helper for hook_node_insert() and hook_node_update().
- [menu_node_delete()](menu_node_delete.md) — Implements hook_node_delete().
- [menu_node_prepare()](menu_node_prepare.md) — Implements hook_node_prepare().
- [_menu_parent_depth_limit()](_menu_parent_depth_limit.md) — Find the depth limit for items in the parent select.
- [_menu_get_menu_weight_delta()](_menu_get_menu_weight_delta.md) — Calculate the delta for the weight element for a given set of menus.
- [menu_form_node_form_alter()](menu_form_node_form_alter.md) — Implements hook_form_BASE_FORM_ID_alter().
- [menu_node_submit()](menu_node_submit.md) — Implements hook_node_submit().
- [menu_form_node_type_form_alter()](menu_form_node_type_form_alter.md) — Implements hook_form_FORM_ID_alter().
- [menu_get_menus()](menu_get_menus.md) — Return an associative array of the custom menus names.

## Constants

### MENU_MAX_MENU_NAME_LENGTH_UI

- Line 18

```php
define('MENU_MAX_MENU_NAME_LENGTH_UI', 27);
```

```text
Maximum length of menu name as entered by the user. Database length is 32
and we add a menu- prefix.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
