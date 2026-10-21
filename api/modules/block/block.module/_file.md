# modules/block/block.module

- **Source:** [local](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · 1113 lines
- **Module/theme:** block

## File documentation

```text
@file
Controls the visual building blocks a page is constructed with.
```

## Functions (derived index)

- [block_help()](block_help.md) — Implements hook_help().
- [block_theme()](block_theme.md) — Implements hook_theme().
- [block_permission()](block_permission.md) — Implements hook_permission().
- [block_menu()](block_menu.md) — Implements hook_menu().
- [_block_themes_access()](_block_themes_access.md) — Menu item access callback - only admin or enabled themes can be accessed.
- [_block_custom_theme()](_block_custom_theme.md) — Theme callback for the block configuration pages.
- [block_block_info()](block_block_info.md) — Implements hook_block_info().
- [block_block_configure()](block_block_configure.md) — Implements hook_block_configure().
- [block_block_save()](block_block_save.md) — Implements hook_block_save().
- [block_block_view()](block_block_view.md) — Implements hook_block_view().
- [block_page_build()](block_page_build.md) — Implements hook_page_build().
- [block_get_blocks_by_region()](block_get_blocks_by_region.md) — Gets a renderable array of a region containing all enabled blocks.
- [_block_get_renderable_array()](_block_get_renderable_array.md) — Gets an array of blocks suitable for drupal_render().
- [_block_rehash()](_block_rehash.md) — Updates the 'block' DB table with the blocks currently exported by modules.
- [block_custom_block_get()](block_custom_block_get.md) — Returns information from database about a user-created (custom) block.
- [block_custom_block_form()](block_custom_block_form.md) — Form constructor for the custom block form.
- [block_custom_block_save()](block_custom_block_save.md) — Saves a user-created block in the database.
- [block_form_user_profile_form_alter()](block_form_user_profile_form_alter.md) — Implements hook_form_FORM_ID_alter() for user_profile_form().
- [block_user_presave()](block_user_presave.md) — Implements hook_user_presave().
- [block_themes_enabled()](block_themes_enabled.md) — Initializes blocks for enabled themes.
- [block_theme_initialize()](block_theme_initialize.md) — Assigns an initial, default set of blocks for a theme.
- [block_list()](block_list.md) — Returns all blocks in the specified region for the current user.
- [block_load()](block_load.md) — Loads a block object from the database.
- [_block_load_blocks()](_block_load_blocks.md) — Loads blocks' information from the database.
- [block_block_list_alter()](block_block_list_alter.md) — Implements hook_block_list_alter().
- [_block_render_blocks()](_block_render_blocks.md) — Render the content and subject for a set of blocks.
- [_block_get_cache_id()](_block_get_cache_id.md) — Assemble the cache_id to use for a given block.
- [block_flush_caches()](block_flush_caches.md) — Implements hook_flush_caches().
- [template_preprocess_block()](template_preprocess_block.md) — Processes variables for block.tpl.php.
- [block_user_role_delete()](block_user_role_delete.md) — Implements hook_user_role_delete().
- [block_menu_delete()](block_menu_delete.md) — Implements hook_menu_delete().
- [block_form_system_performance_settings_alter()](block_form_system_performance_settings_alter.md) — Implements hook_form_FORM_ID_alter().
- [block_admin_paths()](block_admin_paths.md) — Implements hook_admin_paths().
- [block_modules_uninstalled()](block_modules_uninstalled.md) — Implements hook_modules_uninstalled().

## Constants

### BLOCK_REGION_NONE

- Line 11

```php
define('BLOCK_REGION_NONE', -1);
```

```text
Denotes that a block is not enabled in any region and should not be shown.
```

### BLOCK_CUSTOM_FIXED

- Line 16

```php
define('BLOCK_CUSTOM_FIXED', 0);
```

```text
Users cannot control whether or not they see this block.
```

### BLOCK_CUSTOM_ENABLED

- Line 21

```php
define('BLOCK_CUSTOM_ENABLED', 1);
```

```text
Shows this block by default, but lets individual users hide it.
```

### BLOCK_CUSTOM_DISABLED

- Line 26

```php
define('BLOCK_CUSTOM_DISABLED', 2);
```

```text
Hides this block by default but lets individual users show it.
```

### BLOCK_VISIBILITY_NOTLISTED

- Line 31

```php
define('BLOCK_VISIBILITY_NOTLISTED', 0);
```

```text
Shows this block on every page except the listed pages.
```

### BLOCK_VISIBILITY_LISTED

- Line 36

```php
define('BLOCK_VISIBILITY_LISTED', 1);
```

```text
Shows this block on only the listed pages.
```

### BLOCK_VISIBILITY_PHP

- Line 41

```php
define('BLOCK_VISIBILITY_PHP', 2);
```

```text
Shows this block if the associated PHP code returns TRUE.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
