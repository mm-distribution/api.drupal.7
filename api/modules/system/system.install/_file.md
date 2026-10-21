# modules/system/system.install

- **Source:** [local](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · 3455 lines
- **Module/theme:** system

## File documentation

```text
@file
Install, update and uninstall functions for the system module.
```

## Functions (derived index)

- [system_requirements()](system_requirements.md) — Implements hook_requirements().
- [_system_check_db_utf8mb4_requirements()](_system_check_db_utf8mb4_requirements.md) — Checks whether the requirements for multi-byte UTF-8 support are met.
- [system_install()](system_install.md) — Implements hook_install().
- [system_schema()](system_schema.md) — Implements hook_schema().
- [system_schema_cache_7054()](system_schema_cache_7054.md) — The cache schema corresponding to system_update_7054.
- [system_update_last_removed()](system_update_last_removed.md)
- [system_update_dependencies()](system_update_dependencies.md) — Implements hook_update_dependencies().
- [system_update_7000()](system_update_7000.md) — Rename blog and forum permissions to be consistent with other content types.
- [system_update_7001()](system_update_7001.md) — Generate a cron key and save it in the variables table.
- [system_update_7002()](system_update_7002.md) — Add a table to store blocked IP addresses.
- [system_update_7003()](system_update_7003.md) — Update {blocked_ips} with valid IP addresses from {access}.
- [system_update_7004()](system_update_7004.md) — Remove hardcoded numeric deltas from all blocks in core.
- [system_update_7005()](system_update_7005.md) — Remove throttle columns and variables.
- [system_update_7007()](system_update_7007.md) — Convert to new method of storing permissions.
- [system_update_7009()](system_update_7009.md) — Rename the variable for primary links.
- [system_update_7011()](system_update_7011.md) — Split the 'bypass node access' permission from 'administer nodes'.
- [system_update_7013()](system_update_7013.md) — Convert default time zone offset to default time zone name.
- [system_update_7015()](system_update_7015.md) — Change the user logout path.
- [system_update_7016()](system_update_7016.md) — Remove custom datatype *_unsigned in PostgreSQL.
- [system_update_7017()](system_update_7017.md) — Change the theme setting 'toggle_node_info' into a per content type variable.
- [system_update_7018()](system_update_7018.md) — Shorten the {system}.type column and modify indexes.
- [system_update_7020()](system_update_7020.md) — Enable field and field_ui modules.
- [system_update_7021()](system_update_7021.md) — Change the PHP for settings permission.
- [system_update_7027()](system_update_7027.md) — Enable field type modules.
- [system_update_7029()](system_update_7029.md) — Add new 'view own unpublished content' permission for authenticated users. Preserves legacy behavior from Drupal 6.x.
- [system_update_7032()](system_update_7032.md) — Alter field hostname to identifier in the {flood} table.
- [system_update_7033()](system_update_7033.md) — Move CACHE_AGGRESSIVE to CACHE_NORMAL.
- [system_update_7034()](system_update_7034.md) — Migrate the file path settings and create the new {file_managed} table.
- [system_update_7036()](system_update_7036.md) — Split the 'access site in maintenance mode' permission from 'administer site configuration'.
- [system_update_7042()](system_update_7042.md) — Upgrade the {url_alias} table and create a cache bin for path aliases.
- [system_update_7044()](system_update_7044.md) — Drop the actions_aid table.
- [system_update_7045()](system_update_7045.md) — Add expiration field to the {flood} table.
- [system_update_7046()](system_update_7046.md) — Switch from the Minnelli theme if it is the default or admin theme.
- [system_update_7047()](system_update_7047.md) — Normalize the front page path variable.
- [system_update_7048()](system_update_7048.md) — Convert path languages from the empty string to LANGUAGE_NONE.
- [system_update_7049()](system_update_7049.md) — Rename 'Default' profile to 'Standard.'
- [system_update_7050()](system_update_7050.md) — Change {batch}.id column from serial to regular int.
- [system_update_7051()](system_update_7051.md) — make the IP field IPv6 compatible
- [system_update_7052()](system_update_7052.md) — Rename file to include_file in {menu_router} table.
- [system_update_7053()](system_update_7053.md) — Upgrade standard blocks and menus.
- [system_update_7054()](system_update_7054.md) — Remove {cache_*}.headers columns.
- [system_update_7055()](system_update_7055.md) — Converts fields that store serialized variables from text to blob.
- [system_update_7057()](system_update_7057.md) — Increase the size of session-ids.
- [system_update_7058()](system_update_7058.md) — Remove cron semaphore variable.
- [system_update_7059()](system_update_7059.md) — Create the {file_usage} table.
- [system_update_7060()](system_update_7060.md) — Create fields in preparation for migrating upload.module to file.module.
- [system_update_7061()](system_update_7061.md) — Migrate upload.module data to the newly created file field.
- [system_update_7062()](system_update_7062.md) — Replace 'system_list' index with 'bootstrap' index on {system}.
- [system_update_7063()](system_update_7063.md) — Delete {menu_links} records for 'type' => MENU_CALLBACK which would not appear in a fresh install.
- [system_update_7064()](system_update_7064.md) — Remove block_callback field from {menu_router}.
- [system_update_7065()](system_update_7065.md) — Remove the default value for sid.
- [system_update_7066()](system_update_7066.md) — Migrate the 'file_directory_temp' variable.
- [system_update_7067()](system_update_7067.md) — Grant administrators permission to view the administration theme.
- [system_update_7068()](system_update_7068.md) — Update {url_alias}.language description.
- [system_update_7069()](system_update_7069.md) — Remove the obsolete 'site_offline' variable.
- [system_update_7070()](system_update_7070.md) — Remove the obsolete 'drupal_badge_color' and 'drupal_badge_size' variables.
- [system_update_7071()](system_update_7071.md) — Add index missed during upgrade, and fix field default.
- [system_update_7072()](system_update_7072.md) — Remove the obsolete 'site_offline_message' variable.
- [system_update_7073()](system_update_7073.md) — Add binary to {file_managed}, in case system_update_7034() was run without it.
- [system_update_7074()](system_update_7074.md) — This update has been removed and will not run.
- [system_update_7076()](system_update_7076.md) — Convert menu_links query strings into arrays.
- [system_update_7077()](system_update_7077.md) — Revert {file_managed}.filename changed to a binary column.
- [system_update_7078()](system_update_7078.md) — Add binary to {date_formats}.format.
- [system_update_7079()](system_update_7079.md) — Convert the 'filesize' column in {file_managed} to a bigint.
- [system_update_7080()](system_update_7080.md) — Convert the 'format' column in {date_format_locale} to case sensitive varchar.
- [system_update_7081()](system_update_7081.md) — Remove the Drupal 6 default install profile if it is still in the database.
- [system_update_7082()](system_update_7082.md) — Add 'jquery-extend-3.4.0.js' to the 'jquery' library.
- [system_update_7083()](system_update_7083.md) — Add 'jquery-html-prefilter-3.5.0-backport.js' to the 'jquery' library.
- [system_update_7084()](system_update_7084.md) — Rebuild JavaScript aggregates to include 'ajax.js' fix for Chrome 83.
- [system_update_7085()](system_update_7085.md) — Remove FLoC-blocking variable.
- [system_update_7086()](system_update_7086.md) — Prepare the schema and data of the sessions table for hashed session ids.
- [system_update_7087()](system_update_7087.md) — Enable the Announcements module; see 7.100 Release Notes for opt-out details.
- [system_update_7088()](system_update_7088.md) — Clear caches as registry has been altered.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
