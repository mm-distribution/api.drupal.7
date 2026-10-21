# modules/shortcut/shortcut.module

- **Source:** [local](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · 768 lines
- **Module/theme:** shortcut

## File documentation

```text
@file
Allows users to manage customizable lists of shortcut links.
```

## Functions (derived index)

- [shortcut_help()](shortcut_help.md) — Implements hook_help().
- [shortcut_permission()](shortcut_permission.md) — Implements hook_permission().
- [shortcut_menu()](shortcut_menu.md) — Implements hook_menu().
- [shortcut_admin_paths()](shortcut_admin_paths.md) — Implements hook_admin_paths().
- [shortcut_theme()](shortcut_theme.md) — Implements hook_theme().
- [shortcut_block_info()](shortcut_block_info.md) — Implements hook_block_info().
- [shortcut_block_view()](shortcut_block_view.md) — Implements hook_block_view().
- [shortcut_set_edit_access()](shortcut_set_edit_access.md) — Access callback for editing a shortcut set.
- [shortcut_set_delete_access()](shortcut_set_delete_access.md) — Access callback for deleting a shortcut set.
- [shortcut_set_switch_access()](shortcut_set_switch_access.md) — Access callback for switching the shortcut set assigned to a user account.
- [shortcut_link_access()](shortcut_link_access.md) — Access callback for editing a link in a shortcut set.
- [shortcut_set_load()](shortcut_set_load.md) — Loads the data for a shortcut set.
- [shortcut_set_save()](shortcut_set_save.md) — Saves a shortcut set.
- [shortcut_set_delete()](shortcut_set_delete.md) — Deletes a shortcut set.
- [shortcut_set_reset_link_weights()](shortcut_set_reset_link_weights.md) — Resets the link weights in a shortcut set to match their current order.
- [shortcut_set_assign_user()](shortcut_set_assign_user.md) — Assigns a user to a particular shortcut set.
- [shortcut_set_unassign_user()](shortcut_set_unassign_user.md) — Unassigns a user from any shortcut set they may have been assigned to.
- [shortcut_current_displayed_set()](shortcut_current_displayed_set.md) — Returns the current displayed shortcut set for the provided user account.
- [shortcut_default_set()](shortcut_default_set.md) — Returns the default shortcut set for a given user account.
- [shortcut_set_get_unique_name()](shortcut_set_get_unique_name.md) — Returns a unique, machine-readable shortcut set name.
- [shortcut_set_name()](shortcut_set_name.md) — Returns the name of a shortcut set, based on a provided number.
- [shortcut_sets()](shortcut_sets.md) — Returns an array of all shortcut sets, keyed by the set name.
- [shortcut_set_title_exists()](shortcut_set_title_exists.md) — Check to see if a shortcut set with the given title already exists.
- [shortcut_valid_link()](shortcut_valid_link.md) — Determines if a path corresponds to a valid shortcut link.
- [shortcut_renderable_links()](shortcut_renderable_links.md) — Returns an array of shortcut links, suitable for rendering.
- [shortcut_preprocess_page()](shortcut_preprocess_page.md) — Implements hook_preprocess_page().
- [shortcut_page_alter()](shortcut_page_alter.md) — Implements hook_page_alter().
- [shortcut_toolbar_pre_render()](shortcut_toolbar_pre_render.md) — Pre-render function for adding shortcuts to the toolbar drawer.
- [shortcut_set_title()](shortcut_set_title.md) — Returns the sanitized title of a shortcut set.
- [shortcut_set_title_callback()](shortcut_set_title_callback.md) — Returns the title of a shortcut set.

## Constants

### SHORTCUT_DEFAULT_SET_NAME

- Line 14

```php
define('SHORTCUT_DEFAULT_SET_NAME', 'shortcut-set-1');
```

```text
The name of the default shortcut set.

This set will be displayed to any user that does not have another set
assigned, unless overridden by a hook_shortcut_default_set() implementation.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
