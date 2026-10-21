# Menu system

- **Topic id:** `menu`
- **Defined in:** [`includes/menu.inc`](../includes/menu.inc/_file.md), line 8 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L8)

## Documentation

```text
@defgroup menu Menu system
@{
Define the navigation menus, and route page requests to code based on URLs.

The Drupal menu system drives both the navigation system from a user
perspective and the callback system that Drupal uses to respond to URLs
passed from the browser. For this reason, a good understanding of the
menu system is fundamental to the creation of complex modules. As a note,
this is related to, but separate from menu.module, which allows menus
(which in this context are hierarchical lists of links) to be customized from
the Drupal administrative interface.

Drupal's menu system follows a simple hierarchy defined by paths.
Implementations of hook_menu() define menu items and assign them to
paths (which should be unique). The menu system aggregates these items
and determines the menu hierarchy from the paths. For example, if the
paths defined were a, a/b, e, a/b/c/d, f/g, and a/b/h, the menu system
would form the structure:
- a
  - a/b
    - a/b/c/d
    - a/b/h
- e
- f/g
Note that the number of elements in the path does not necessarily
determine the depth of the menu item in the tree.

When responding to a page request, the menu system looks to see if the
path requested by the browser is registered as a menu item with a
callback. If not, the system searches up the menu tree for the most
complete match with a callback it can find. If the path a/b/i is
requested in the tree above, the callback for a/b would be used.

The found callback function is called with any arguments specified
in the "page arguments" attribute of its menu item. The
attribute must be an array. After these arguments, any remaining
components of the path are appended as further arguments. In this
way, the callback for a/b above could respond to a request for
a/b/i differently than a request for a/b/j.

For an illustration of this process, see page_example.module.

Access to the callback functions is also protected by the menu system.
The "access callback" with an optional "access arguments" of each menu
item is called before the page callback proceeds. If this returns TRUE,
then access is granted; if FALSE, then access is denied. Default local task
menu items (see next paragraph) may omit this attribute to use the value
provided by the parent item.

In the default Drupal interface, you will notice many links rendered as
tabs. These are known in the menu system as "local tasks", and they are
rendered as tabs by default, though other presentations are possible.
Local tasks function just as other menu items in most respects. It is
convention that the names of these tasks should be short verbs if
possible. In addition, a "default" local task should be provided for
each set. When visiting a local task's parent menu item, the default
local task will be rendered as if it is selected; this provides for a
normal tab user experience. This default task is special in that it
links not to its provided path, but to its parent item's path instead.
The default task's path is only used to place it appropriately in the
menu hierarchy.

Everything described so far is stored in the menu_router table. The
menu_links table holds the visible menu links. By default these are
derived from the same hook_menu definitions, however you are free to
add more with menu_link_save().
```

## Members (derived, 111)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_menu_build_tree()](../includes/menu.inc/_menu_build_tree.md) (function) — Builds a menu tree.
- [_menu_check_access()](../includes/menu.inc/_menu_check_access.md) (function) — Checks access to a menu item using the access callback.
- [_menu_check_rebuild()](../includes/menu.inc/_menu_check_rebuild.md) (function) — Checks whether a menu_rebuild() is necessary.
- [_menu_clear_page_cache()](../includes/menu.inc/_menu_clear_page_cache.md) (function) — Clears the page and block caches at most twice per page load.
- [_menu_delete_item()](../includes/menu.inc/_menu_delete_item.md) (function) — Deletes a single menu link.
- [_menu_find_router_path()](../includes/menu.inc/_menu_find_router_path.md) (function) — Finds the router path which will serve this path.
- [_menu_item_localize()](../includes/menu.inc/_menu_item_localize.md) (function) — Localizes the router item title using t() or another callback.
- [_menu_link_build()](../includes/menu.inc/_menu_link_build.md) (function) — Builds a link from a router item.
- [_menu_link_find_parent()](../includes/menu.inc/_menu_link_find_parent.md) (function) — Finds a possible parent for a given menu link.
- [_menu_link_map_translate()](../includes/menu.inc/_menu_link_map_translate.md) (function) — Translates the path elements in the map using any to_arg helper function.
- [_menu_link_move_children()](../includes/menu.inc/_menu_link_move_children.md) (function) — Updates the children of a menu link that is being moved.
- [_menu_link_parents_set()](../includes/menu.inc/_menu_link_parents_set.md) (function) — Sets the p1 through p9 values for a menu link being saved.
- [_menu_link_translate()](../includes/menu.inc/_menu_link_translate.md) (function) — Provides menu link access control, translation, and argument handling.
- [_menu_load_objects()](../includes/menu.inc/_menu_load_objects.md) (function) — Loads objects into the map as defined in the $item['load_functions'].
- [_menu_navigation_links_rebuild()](../includes/menu.inc/_menu_navigation_links_rebuild.md) (function) — Builds menu links for the items in the menu router.
- [_menu_router_build()](../includes/menu.inc/_menu_router_build.md) (function) — Builds the router table based on the data from hook_menu().
- [_menu_router_cache()](../includes/menu.inc/_menu_router_cache.md) (function) — Stores the menu router if we have it in memory.
- [_menu_router_save()](../includes/menu.inc/_menu_router_save.md) (function) — Saves data from menu_router_build() to the router table.
- [_menu_set_expanded_menus()](../includes/menu.inc/_menu_set_expanded_menus.md) (function) — Updates a list of menus with expanded items.
- [_menu_site_is_offline()](../includes/menu.inc/_menu_site_is_offline.md) (function) — Checks whether the site is in maintenance mode.
- [_menu_translate()](../includes/menu.inc/_menu_translate.md) (function) — Handles dynamic path translation and menu access control.
- [_menu_tree_check_access()](../includes/menu.inc/_menu_tree_check_access.md) (function) — Sorts the menu tree and recursively checks access for each item.
- [_menu_tree_data()](../includes/menu.inc/_menu_tree_data.md) (function) — Builds the data representing a menu tree.
- [_menu_update_parental_status()](../includes/menu.inc/_menu_update_parental_status.md) (function) — Checks and updates the 'has_children' status for the parent of a link.
- [drupal_help_arg()](../includes/menu.inc/drupal_help_arg.md) (function) — Generates elements for the $arg array in the help hook.
- [menu_build_tree()](../includes/menu.inc/menu_build_tree.md) (function) — Builds a menu tree, translates links, and checks access.
- [menu_cache_clear()](../includes/menu.inc/menu_cache_clear.md) (function) — Clears the cached data for a single named menu.
- [menu_cache_clear_all()](../includes/menu.inc/menu_cache_clear_all.md) (function) — Clears all cached menu data.
- [menu_contextual_links()](../includes/menu.inc/menu_contextual_links.md) (function) — Retrieves contextual links for a path based on registered local tasks.
- [menu_delete_links()](../includes/menu.inc/menu_delete_links.md) (function) — Deletes all links for a menu.
- [menu_execute_active_handler()](../includes/menu.inc/menu_execute_active_handler.md) (function) — Execute the page callback associated with the current path.
- [menu_get_active_breadcrumb()](../includes/menu.inc/menu_get_active_breadcrumb.md) (function) — Gets the breadcrumb for the current page, as determined by the active trail.
- [menu_get_active_help()](../includes/menu.inc/menu_get_active_help.md) (function) — Returns the help associated with the active menu item.
- [menu_get_active_menu_names()](../includes/menu.inc/menu_get_active_menu_names.md) (function) — Gets the active menu for the current page.
- [menu_get_active_title()](../includes/menu.inc/menu_get_active_title.md) (function) — Gets the title of the current page, as determined by the active trail.
- [menu_get_active_trail()](../includes/menu.inc/menu_get_active_trail.md) (function) — Gets the active trail (path to root menu root) of the current page.
- [menu_get_ancestors()](../includes/menu.inc/menu_get_ancestors.md) (function) — Returns the ancestors (and relevant placeholders) for any given path.
- [menu_get_custom_theme()](../includes/menu.inc/menu_get_custom_theme.md) (function) — Gets the custom theme for the current page, if there is one.
- [menu_get_item()](../includes/menu.inc/menu_get_item.md) (function) — Gets a router item.
- [menu_get_names()](../includes/menu.inc/menu_get_names.md) (function) — Build a list of named menus.
- [menu_get_object()](../includes/menu.inc/menu_get_object.md) (function) — Gets a loaded object from a router item.
- [menu_get_router()](../includes/menu.inc/menu_get_router.md) (function) — Gets the menu router.
- [menu_link_children_relative_depth()](../includes/menu.inc/menu_link_children_relative_depth.md) (function) — Finds the depth of an item's children relative to its depth.
- [menu_link_delete()](../includes/menu.inc/menu_link_delete.md) (function) — Delete one or several menu links.
- [menu_link_get_preferred()](../includes/menu.inc/menu_link_get_preferred.md) (function) — Looks up the preferred menu link for a given system path.
- [menu_link_load()](../includes/menu.inc/menu_link_load.md) (function) — Gets a translated, access-checked menu link that is ready for rendering.
- [menu_link_maintain()](../includes/menu.inc/menu_link_maintain.md) (function) — Inserts, updates, or deletes an uncustomized menu link related to a module.
- [menu_link_save()](../includes/menu.inc/menu_link_save.md) (function) — Saves a menu link.
- [menu_links_clone()](../includes/menu.inc/menu_links_clone.md) (function) — Clones an array of menu links.
- [menu_list_system_menus()](../includes/menu.inc/menu_list_system_menus.md) (function) — Returns an array containing the names of system-defined (default) menus.
- [menu_load_links()](../includes/menu.inc/menu_load_links.md) (function) — Returns an array containing all links for a menu.
- [menu_local_actions()](../includes/menu.inc/menu_local_actions.md) (function) — Returns the rendered local actions at the current level.
- [menu_local_tabs()](../includes/menu.inc/menu_local_tabs.md) (function) — Returns a renderable element for the primary and secondary tabs.
- [menu_local_tasks()](../includes/menu.inc/menu_local_tasks.md) (function) — Collects the local tasks (tabs), action links, and the root path.
- [menu_main_menu()](../includes/menu.inc/menu_main_menu.md) (function) — Returns an array of links to be rendered as the Main menu.
- [menu_navigation_links()](../includes/menu.inc/menu_navigation_links.md) (function) — Returns an array of links for a navigation menu.
- [menu_primary_local_tasks()](../includes/menu.inc/menu_primary_local_tasks.md) (function) — Returns the rendered local tasks at the top level.
- [menu_rebuild()](../includes/menu.inc/menu_rebuild.md) (function) — Populates the database tables used by various menu functions.
- [menu_reset_static_cache()](../includes/menu.inc/menu_reset_static_cache.md) (function) — Resets the menu system static cache.
- [menu_router_build()](../includes/menu.inc/menu_router_build.md) (function) — Collects and alters the menu definitions.
- [menu_secondary_local_tasks()](../includes/menu.inc/menu_secondary_local_tasks.md) (function) — Returns the rendered local tasks at the second level.
- [menu_secondary_menu()](../includes/menu.inc/menu_secondary_menu.md) (function) — Returns an array of links to be rendered as the Secondary links.
- [menu_set_active_item()](../includes/menu.inc/menu_set_active_item.md) (function) — Sets the active path, which determines which page is loaded.
- [menu_set_active_menu_names()](../includes/menu.inc/menu_set_active_menu_names.md) (function) — Sets (or gets) the active menu for the current page.
- [menu_set_active_trail()](../includes/menu.inc/menu_set_active_trail.md) (function) — Sets the active trail (path to the menu tree root) of the current page.
- [menu_set_custom_theme()](../includes/menu.inc/menu_set_custom_theme.md) (function) — Sets a custom theme for the current page, if there is one.
- [menu_set_item()](../includes/menu.inc/menu_set_item.md) (function) — Replaces the statically cached item for a given path.
- [menu_tab_root_path()](../includes/menu.inc/menu_tab_root_path.md) (function) — Returns the router path, or the path for a default local task's parent.
- [menu_tail_load()](../includes/menu.inc/menu_tail_load.md) (function) — Loads the path as one string relative to the current index.
- [menu_tail_to_arg()](../includes/menu.inc/menu_tail_to_arg.md) (function) — Returns a string containing the path relative to the current index.
- [menu_tree()](../includes/menu.inc/menu_tree.md) (function) — Renders a menu tree based on the current path.
- [menu_tree_all_data()](../includes/menu.inc/menu_tree_all_data.md) (function) — Gets the data structure representing a named menu tree.
- [menu_tree_check_access()](../includes/menu.inc/menu_tree_check_access.md) (function) — Checks access and performs dynamic operations for each link in the tree.
- [menu_tree_collect_node_links()](../includes/menu.inc/menu_tree_collect_node_links.md) (function) — Collects node links from a given menu tree recursively.
- [menu_tree_data()](../includes/menu.inc/menu_tree_data.md) (function) — Sorts and returns the built data representing a menu tree.
- [menu_tree_get_path()](../includes/menu.inc/menu_tree_get_path.md) (function) — Gets the path for determining the active trail of the specified menu tree.
- [menu_tree_output()](../includes/menu.inc/menu_tree_output.md) (function) — Returns an output structure for rendering a menu tree.
- [menu_tree_page_data()](../includes/menu.inc/menu_tree_page_data.md) (function) — Gets the data structure for a named menu tree, based on the current page.
- [menu_tree_set_path()](../includes/menu.inc/menu_tree_set_path.md) (function) — Sets the path for determining the active trail of the specified menu tree.
- [menu_unserialize()](../includes/menu.inc/menu_unserialize.md) (function) — Unserializes menu data, using a map to replace path elements.
- [template_preprocess_menu_tree()](../includes/menu.inc/template_preprocess_menu_tree.md) (function) — Implements template_preprocess_HOOK() for theme_menu_tree().
- [theme_menu_link()](../includes/menu.inc/theme_menu_link.md) (function) — Returns HTML for a menu link and submenu.
- [theme_menu_local_action()](../includes/menu.inc/theme_menu_local_action.md) (function) — Returns HTML for a single local action link.
- [theme_menu_local_task()](../includes/menu.inc/theme_menu_local_task.md) (function) — Returns HTML for a single local task link.
- [theme_menu_local_tasks()](../includes/menu.inc/theme_menu_local_tasks.md) (function) — Returns HTML for primary and secondary local tasks.
- [theme_menu_tree()](../includes/menu.inc/theme_menu_tree.md) (function) — Returns HTML for a wrapper for a menu sub-tree.
- [MENU_ACCESS_DENIED](../includes/menu.inc/_file.md#menu_access_denied) (constant) — Menu status code -- Access denied.
- [MENU_CALLBACK](../includes/menu.inc/_file.md#menu_callback) (constant) — Menu type -- A hidden, internal callback, typically used for API calls.
- [MENU_CONTEXT_INLINE](../includes/menu.inc/_file.md#menu_context_inline) (constant) — Internal menu flag: Local task should be displayed inline.
- [MENU_CONTEXT_NONE](../includes/menu.inc/_file.md#menu_context_none) (constant) — Internal menu flag: Invisible local task.
- [MENU_CONTEXT_PAGE](../includes/menu.inc/_file.md#menu_context_page) (constant) — Internal menu flag: Local task should be displayed in page context.
- [MENU_CREATED_BY_ADMIN](../includes/menu.inc/_file.md#menu_created_by_admin) (constant) — Internal menu flag -- menu item was created by administrator.
- [MENU_DEFAULT_LOCAL_TASK](../includes/menu.inc/_file.md#menu_default_local_task) (constant) — Menu type -- The "default" local task, which is initially active.
- [MENU_FOUND](../includes/menu.inc/_file.md#menu_found) (constant) — Internal menu status code -- Menu item was found.
- [MENU_IS_LOCAL_ACTION](../includes/menu.inc/_file.md#menu_is_local_action) (constant) — Internal menu flag -- menu item is a local action.
- [MENU_IS_LOCAL_TASK](../includes/menu.inc/_file.md#menu_is_local_task) (constant) — Internal menu flag -- menu item is a local task.
- [MENU_IS_ROOT](../includes/menu.inc/_file.md#menu_is_root) (constant) — Internal menu flag -- menu item is the root of the menu tree.
- [MENU_LINKS_TO_PARENT](../includes/menu.inc/_file.md#menu_links_to_parent) (constant) — Internal menu flag -- menu item links back to its parent.
- [MENU_LOCAL_ACTION](../includes/menu.inc/_file.md#menu_local_action) (constant) — Menu type -- An action specific to the parent, usually rendered as a link.
- [MENU_LOCAL_TASK](../includes/menu.inc/_file.md#menu_local_task) (constant) — Menu type -- A task specific to the parent item, usually rendered as a tab.
- [MENU_MAX_DEPTH](../includes/menu.inc/_file.md#menu_max_depth) (constant) — The maximum depth of a menu links tree - matches the number of p columns.
- [MENU_MAX_PARTS](../includes/menu.inc/_file.md#menu_max_parts) (constant) — The maximum number of path elements for a menu callback
- [MENU_MODIFIED_BY_ADMIN](../includes/menu.inc/_file.md#menu_modified_by_admin) (constant) — Internal menu flag -- menu item can be modified by administrator.
- [MENU_NORMAL_ITEM](../includes/menu.inc/_file.md#menu_normal_item) (constant) — Menu type -- A "normal" menu item that's shown in menu and breadcrumbs.
- [MENU_NOT_FOUND](../includes/menu.inc/_file.md#menu_not_found) (constant) — Menu status code -- Not found.
- [MENU_PREFERRED_LINK](../includes/menu.inc/_file.md#menu_preferred_link) (constant) — Reserved key to identify the most specific menu link for a given path.
- [MENU_SITE_OFFLINE](../includes/menu.inc/_file.md#menu_site_offline) (constant) — Internal menu status code -- Menu item inaccessible because site is offline.
- [MENU_SITE_ONLINE](../includes/menu.inc/_file.md#menu_site_online) (constant) — Internal menu status code -- Everything is working fine.
- [MENU_SUGGESTED_ITEM](../includes/menu.inc/_file.md#menu_suggested_item) (constant) — Menu type -- A normal menu item, hidden until enabled by an administrator.
- [MENU_VISIBLE_IN_BREADCRUMB](../includes/menu.inc/_file.md#menu_visible_in_breadcrumb) (constant) — Internal menu flag -- menu item is visible in the breadcrumb.
- [MENU_VISIBLE_IN_TREE](../includes/menu.inc/_file.md#menu_visible_in_tree) (constant) — Internal menu flag -- menu item is visible in the menu tree.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
