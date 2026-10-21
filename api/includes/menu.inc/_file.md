# includes/menu.inc

- **Source:** [local](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · 3971 lines

## File documentation

```text
@file
API for the Drupal menu system.
```

## Functions (derived index)

- [menu_get_ancestors()](menu_get_ancestors.md) — Returns the ancestors (and relevant placeholders) for any given path.
- [menu_unserialize()](menu_unserialize.md) — Unserializes menu data, using a map to replace path elements.
- [menu_set_item()](menu_set_item.md) — Replaces the statically cached item for a given path.
- [menu_get_item()](menu_get_item.md) — Gets a router item.
- [menu_execute_active_handler()](menu_execute_active_handler.md) — Execute the page callback associated with the current path.
- [_menu_load_objects()](_menu_load_objects.md) — Loads objects into the map as defined in the $item['load_functions'].
- [_menu_check_access()](_menu_check_access.md) — Checks access to a menu item using the access callback.
- [_menu_item_localize()](_menu_item_localize.md) — Localizes the router item title using t() or another callback.
- [_menu_translate()](_menu_translate.md) — Handles dynamic path translation and menu access control.
- [_menu_link_map_translate()](_menu_link_map_translate.md) — Translates the path elements in the map using any to_arg helper function.
- [menu_tail_to_arg()](menu_tail_to_arg.md) — Returns a string containing the path relative to the current index.
- [menu_tail_load()](menu_tail_load.md) — Loads the path as one string relative to the current index.
- [_menu_link_translate()](_menu_link_translate.md) — Provides menu link access control, translation, and argument handling.
- [menu_get_object()](menu_get_object.md) — Gets a loaded object from a router item.
- [menu_tree()](menu_tree.md) — Renders a menu tree based on the current path.
- [menu_tree_output()](menu_tree_output.md) — Returns an output structure for rendering a menu tree.
- [menu_tree_all_data()](menu_tree_all_data.md) — Gets the data structure representing a named menu tree.
- [menu_tree_set_path()](menu_tree_set_path.md) — Sets the path for determining the active trail of the specified menu tree.
- [menu_tree_get_path()](menu_tree_get_path.md) — Gets the path for determining the active trail of the specified menu tree.
- [menu_tree_page_data()](menu_tree_page_data.md) — Gets the data structure for a named menu tree, based on the current page.
- [menu_build_tree()](menu_build_tree.md) — Builds a menu tree, translates links, and checks access.
- [_menu_build_tree()](_menu_build_tree.md) — Builds a menu tree.
- [menu_tree_collect_node_links()](menu_tree_collect_node_links.md) — Collects node links from a given menu tree recursively.
- [menu_tree_check_access()](menu_tree_check_access.md) — Checks access and performs dynamic operations for each link in the tree.
- [_menu_tree_check_access()](_menu_tree_check_access.md) — Sorts the menu tree and recursively checks access for each item.
- [menu_tree_data()](menu_tree_data.md) — Sorts and returns the built data representing a menu tree.
- [_menu_tree_data()](_menu_tree_data.md) — Builds the data representing a menu tree.
- [template_preprocess_menu_tree()](template_preprocess_menu_tree.md) — Implements template_preprocess_HOOK() for theme_menu_tree().
- [theme_menu_tree()](theme_menu_tree.md) — Returns HTML for a wrapper for a menu sub-tree.
- [theme_menu_link()](theme_menu_link.md) — Returns HTML for a menu link and submenu.
- [theme_menu_local_task()](theme_menu_local_task.md) — Returns HTML for a single local task link.
- [theme_menu_local_action()](theme_menu_local_action.md) — Returns HTML for a single local action link.
- [drupal_help_arg()](drupal_help_arg.md) — Generates elements for the $arg array in the help hook.
- [menu_get_active_help()](menu_get_active_help.md) — Returns the help associated with the active menu item.
- [menu_get_custom_theme()](menu_get_custom_theme.md) — Gets the custom theme for the current page, if there is one.
- [menu_set_custom_theme()](menu_set_custom_theme.md) — Sets a custom theme for the current page, if there is one.
- [menu_get_names()](menu_get_names.md) — Build a list of named menus.
- [menu_list_system_menus()](menu_list_system_menus.md) — Returns an array containing the names of system-defined (default) menus.
- [menu_main_menu()](menu_main_menu.md) — Returns an array of links to be rendered as the Main menu.
- [menu_secondary_menu()](menu_secondary_menu.md) — Returns an array of links to be rendered as the Secondary links.
- [menu_navigation_links()](menu_navigation_links.md) — Returns an array of links for a navigation menu.
- [menu_local_tasks()](menu_local_tasks.md) — Collects the local tasks (tabs), action links, and the root path.
- [menu_contextual_links()](menu_contextual_links.md) — Retrieves contextual links for a path based on registered local tasks.
- [menu_primary_local_tasks()](menu_primary_local_tasks.md) — Returns the rendered local tasks at the top level.
- [menu_secondary_local_tasks()](menu_secondary_local_tasks.md) — Returns the rendered local tasks at the second level.
- [menu_local_actions()](menu_local_actions.md) — Returns the rendered local actions at the current level.
- [menu_tab_root_path()](menu_tab_root_path.md) — Returns the router path, or the path for a default local task's parent.
- [menu_local_tabs()](menu_local_tabs.md) — Returns a renderable element for the primary and secondary tabs.
- [theme_menu_local_tasks()](theme_menu_local_tasks.md) — Returns HTML for primary and secondary local tasks.
- [menu_set_active_menu_names()](menu_set_active_menu_names.md) — Sets (or gets) the active menu for the current page.
- [menu_get_active_menu_names()](menu_get_active_menu_names.md) — Gets the active menu for the current page.
- [menu_set_active_item()](menu_set_active_item.md) — Sets the active path, which determines which page is loaded.
- [menu_set_active_trail()](menu_set_active_trail.md) — Sets the active trail (path to the menu tree root) of the current page.
- [menu_link_get_preferred()](menu_link_get_preferred.md) — Looks up the preferred menu link for a given system path.
- [menu_get_active_trail()](menu_get_active_trail.md) — Gets the active trail (path to root menu root) of the current page.
- [menu_get_active_breadcrumb()](menu_get_active_breadcrumb.md) — Gets the breadcrumb for the current page, as determined by the active trail.
- [menu_get_active_title()](menu_get_active_title.md) — Gets the title of the current page, as determined by the active trail.
- [menu_link_load()](menu_link_load.md) — Gets a translated, access-checked menu link that is ready for rendering.
- [menu_cache_clear()](menu_cache_clear.md) — Clears the cached data for a single named menu.
- [menu_cache_clear_all()](menu_cache_clear_all.md) — Clears all cached menu data.
- [menu_reset_static_cache()](menu_reset_static_cache.md) — Resets the menu system static cache.
- [_menu_check_rebuild()](_menu_check_rebuild.md) — Checks whether a menu_rebuild() is necessary.
- [menu_rebuild()](menu_rebuild.md) — Populates the database tables used by various menu functions.
- [menu_router_build()](menu_router_build.md) — Collects and alters the menu definitions.
- [_menu_router_cache()](_menu_router_cache.md) — Stores the menu router if we have it in memory.
- [menu_get_router()](menu_get_router.md) — Gets the menu router.
- [_menu_link_build()](_menu_link_build.md) — Builds a link from a router item.
- [_menu_navigation_links_rebuild()](_menu_navigation_links_rebuild.md) — Builds menu links for the items in the menu router.
- [menu_links_clone()](menu_links_clone.md) — Clones an array of menu links.
- [menu_load_links()](menu_load_links.md) — Returns an array containing all links for a menu.
- [menu_delete_links()](menu_delete_links.md) — Deletes all links for a menu.
- [menu_link_delete()](menu_link_delete.md) — Delete one or several menu links.
- [_menu_delete_item()](_menu_delete_item.md) — Deletes a single menu link.
- [menu_link_save()](menu_link_save.md) — Saves a menu link.
- [_menu_link_find_parent()](_menu_link_find_parent.md) — Finds a possible parent for a given menu link.
- [_menu_clear_page_cache()](_menu_clear_page_cache.md) — Clears the page and block caches at most twice per page load.
- [_menu_set_expanded_menus()](_menu_set_expanded_menus.md) — Updates a list of menus with expanded items.
- [_menu_find_router_path()](_menu_find_router_path.md) — Finds the router path which will serve this path.
- [menu_link_maintain()](menu_link_maintain.md) — Inserts, updates, or deletes an uncustomized menu link related to a module.
- [menu_link_children_relative_depth()](menu_link_children_relative_depth.md) — Finds the depth of an item's children relative to its depth.
- [_menu_link_move_children()](_menu_link_move_children.md) — Updates the children of a menu link that is being moved.
- [_menu_update_parental_status()](_menu_update_parental_status.md) — Checks and updates the 'has_children' status for the parent of a link.
- [_menu_link_parents_set()](_menu_link_parents_set.md) — Sets the p1 through p9 values for a menu link being saved.
- [_menu_router_build()](_menu_router_build.md) — Builds the router table based on the data from hook_menu().
- [_menu_router_save()](_menu_router_save.md) — Saves data from menu_router_build() to the router table.
- [_menu_site_is_offline()](_menu_site_is_offline.md) — Checks whether the site is in maintenance mode.

## Constants

### MENU_IS_ROOT

- Line 86; topics: menu, menu_flags

```php
define('MENU_IS_ROOT', 0x0001);
```

```text
Internal menu flag -- menu item is the root of the menu tree.
```

### MENU_VISIBLE_IN_TREE

- Line 91; topics: menu, menu_flags

```php
define('MENU_VISIBLE_IN_TREE', 0x0002);
```

```text
Internal menu flag -- menu item is visible in the menu tree.
```

### MENU_VISIBLE_IN_BREADCRUMB

- Line 96; topics: menu, menu_flags

```php
define('MENU_VISIBLE_IN_BREADCRUMB', 0x0004);
```

```text
Internal menu flag -- menu item is visible in the breadcrumb.
```

### MENU_LINKS_TO_PARENT

- Line 101; topics: menu, menu_flags

```php
define('MENU_LINKS_TO_PARENT', 0x0008);
```

```text
Internal menu flag -- menu item links back to its parent.
```

### MENU_MODIFIED_BY_ADMIN

- Line 106; topics: menu, menu_flags

```php
define('MENU_MODIFIED_BY_ADMIN', 0x0020);
```

```text
Internal menu flag -- menu item can be modified by administrator.
```

### MENU_CREATED_BY_ADMIN

- Line 111; topics: menu, menu_flags

```php
define('MENU_CREATED_BY_ADMIN', 0x0040);
```

```text
Internal menu flag -- menu item was created by administrator.
```

### MENU_IS_LOCAL_TASK

- Line 116; topics: menu, menu_flags

```php
define('MENU_IS_LOCAL_TASK', 0x0080);
```

```text
Internal menu flag -- menu item is a local task.
```

### MENU_IS_LOCAL_ACTION

- Line 121; topics: menu, menu_flags

```php
define('MENU_IS_LOCAL_ACTION', 0x0100);
```

```text
Internal menu flag -- menu item is a local action.
```

### MENU_NORMAL_ITEM

- Line 143; topics: menu, menu_item_types

```php
define('MENU_NORMAL_ITEM', MENU_VISIBLE_IN_TREE | MENU_VISIBLE_IN_BREADCRUMB);
```

```text
Menu type -- A "normal" menu item that's shown in menu and breadcrumbs.

Normal menu items show up in the menu tree and can be moved/hidden by
the administrator. Use this for most menu items. It is the default value if
no menu item type is specified.
```

### MENU_CALLBACK

- Line 151; topics: menu, menu_item_types

```php
define('MENU_CALLBACK', 0x0000);
```

```text
Menu type -- A hidden, internal callback, typically used for API calls.

Callbacks simply register a path so that the correct function is fired
when the URL is accessed. They do not appear in menus or breadcrumbs.
```

### MENU_SUGGESTED_ITEM

- Line 161; topics: menu, menu_item_types

```php
define('MENU_SUGGESTED_ITEM', MENU_VISIBLE_IN_BREADCRUMB | 0x0010);
```

```text
Menu type -- A normal menu item, hidden until enabled by an administrator.

Modules may "suggest" menu items that the administrator may enable. They act
just as callbacks do until enabled, at which time they act like normal items.
Note for the value: 0x0010 was a flag which is no longer used, but this way
the values of MENU_CALLBACK and MENU_SUGGESTED_ITEM are separate.
```

### MENU_LOCAL_TASK

- Line 170; topics: menu, menu_item_types

```php
define('MENU_LOCAL_TASK', MENU_IS_LOCAL_TASK | MENU_VISIBLE_IN_BREADCRUMB);
```

```text
Menu type -- A task specific to the parent item, usually rendered as a tab.

Local tasks are menu items that describe actions to be performed on their
parent item. An example is the path "node/52/edit", which performs the
"edit" task on "node/52".
```

### MENU_DEFAULT_LOCAL_TASK

- Line 178; topics: menu, menu_item_types

```php
define('MENU_DEFAULT_LOCAL_TASK', MENU_IS_LOCAL_TASK | MENU_LINKS_TO_PARENT | MENU_VISIBLE_IN_BREADCRUMB);
```

```text
Menu type -- The "default" local task, which is initially active.

Every set of local tasks should provide one "default" task, that links to the
same path as its parent when clicked.
```

### MENU_LOCAL_ACTION

- Line 186; topics: menu, menu_item_types

```php
define('MENU_LOCAL_ACTION', MENU_IS_LOCAL_TASK | MENU_IS_LOCAL_ACTION | MENU_VISIBLE_IN_BREADCRUMB);
```

```text
Menu type -- An action specific to the parent, usually rendered as a link.

Local actions are menu items that describe actions on the parent item such
as adding a new user, taxonomy term, etc.
```

### MENU_CONTEXT_NONE

- Line 204; topics: menu, menu_context_types

```php
define('MENU_CONTEXT_NONE', 0x0000);
```

```text
Internal menu flag: Invisible local task.

This flag may be used for local tasks like "Delete", so custom modules and
themes can alter the default context and expose the task by altering menu.
```

### MENU_CONTEXT_PAGE

- Line 209; topics: menu, menu_context_types

```php
define('MENU_CONTEXT_PAGE', 0x0001);
```

```text
Internal menu flag: Local task should be displayed in page context.
```

### MENU_CONTEXT_INLINE

- Line 214; topics: menu, menu_context_types

```php
define('MENU_CONTEXT_INLINE', 0x0002);
```

```text
Internal menu flag: Local task should be displayed inline.
```

### MENU_FOUND

- Line 229; topics: menu, menu_status_codes

```php
define('MENU_FOUND', 1);
```

```text
Internal menu status code -- Menu item was found.
```

### MENU_NOT_FOUND

- Line 238; topics: menu, menu_status_codes

```php
define('MENU_NOT_FOUND', 2);
```

```text
Menu status code -- Not found.

This can be used as the return value from a page callback, although it is
preferable to use a load function to accomplish this; see the hook_menu()
documentation for details.
```

### MENU_ACCESS_DENIED

- Line 247; topics: menu, menu_status_codes

```php
define('MENU_ACCESS_DENIED', 3);
```

```text
Menu status code -- Access denied.

This can be used as the return value from a page callback, although it is
preferable to use an access callback to accomplish this; see the hook_menu()
documentation for details.
```

### MENU_SITE_OFFLINE

- Line 252; topics: menu, menu_status_codes

```php
define('MENU_SITE_OFFLINE', 4);
```

```text
Internal menu status code -- Menu item inaccessible because site is offline.
```

### MENU_SITE_ONLINE

- Line 257; topics: menu, menu_status_codes

```php
define('MENU_SITE_ONLINE', 5);
```

```text
Internal menu status code -- Everything is working fine.
```

### MENU_MAX_PARTS

- Line 272; topics: menu, menu_tree_parameters

```php
define('MENU_MAX_PARTS', 9);
```

```text
The maximum number of path elements for a menu callback
```

### MENU_MAX_DEPTH

- Line 278; topics: menu, menu_tree_parameters

```php
define('MENU_MAX_DEPTH', 9);
```

```text
The maximum depth of a menu links tree - matches the number of p columns.
```

### MENU_PREFERRED_LINK

- Line 297; topics: menu

```php
define('MENU_PREFERRED_LINK', '1cf698d64d1aa4b83907cf6ed55db3a7f8e92c91');
```

```text
Reserved key to identify the most specific menu link for a given path.

The value of this constant is a hash of the constant name. We use the hash
so that the reserved key is over 32 characters in length and will not
collide with allowed menu names:
@code
sha1('MENU_PREFERRED_LINK') = 1cf698d64d1aa4b83907cf6ed55db3a7f8e92c91
@endcode

@see menu_link_get_preferred()
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
