# Extra updates for 7.x

- **Topic id:** `updates-7.x-extra`
- **Defined in:** [`modules/system/system.install`](../modules/system/system.install/_file.md), line 3195 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3195)

## Documentation

```text
@defgroup updates-7.x-extra Extra updates for 7.x
@{
Update functions between 7.x versions.
```

## Members (derived, 66)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_image_update_7002_add_columns()](../modules/image/image.install/_image_update_7002_add_columns.md) (function) — Add width and height columns to a specific table.
- [_image_update_7002_populate_dimensions()](../modules/image/image.install/_image_update_7002_populate_dimensions.md) (function) — Populate image dimensions in a specific table.
- [aggregator_update_7003()](../modules/aggregator/aggregator.install/aggregator_update_7003.md) (function) — Increase the length of {aggregator_feed}.url.
- [aggregator_update_7004()](../modules/aggregator/aggregator.install/aggregator_update_7004.md) (function) — Add index on timestamp.
- [block_update_7008()](../modules/block/block.install/block_update_7008.md) (function) — Update database to match Drupal 7 schema.
- [block_update_7009()](../modules/block/block.install/block_update_7009.md) (function) — Increase {block}.title length to 255 characters.
- [color_update_7001()](../modules/color/color.install/color_update_7001.md) (function) — Warn site administrator if unsafe CSS color codes are found in the database.
- [comment_update_7007()](../modules/comment/comment.install/comment_update_7007.md) (function) — Add an index to the created column.
- [comment_update_7008()](../modules/comment/comment.install/comment_update_7008.md) (function) — Update database to match Drupal 7 schema.
- [comment_update_7009()](../modules/comment/comment.install/comment_update_7009.md) (function) — Change the last_comment_timestamp column description.
- [dblog_update_7002()](../modules/dblog/dblog.install/dblog_update_7002.md) (function) — Add an index to the severity column in the watchdog database table.
- [dblog_update_7003()](../modules/dblog/dblog.install/dblog_update_7003.md) (function) — Account for possible legacy systems where dblog was not installed.
- [field_update_7002()](../modules/field/field.install/field_update_7002.md) (function) — Split the all-inclusive field_bundle_settings variable per bundle.
- [field_update_7003()](../modules/field/field.install/field_update_7003.md) (function) — Add the FieldInfo class to the class registry.
- [field_update_7004()](../modules/field/field.install/field_update_7004.md) (function) — Grant the new "administer fields" permission to trusted users.
- [forum_update_7002()](../modules/forum/forum.install/forum_update_7002.md) (function) — Add new index to forum_index table.
- [forum_update_7003()](../modules/forum/forum.install/forum_update_7003.md) (function) — Rename field to 'taxonomy_forums'.
- [forum_update_7011()](../modules/forum/forum.install/forum_update_7011.md) (function) — Update {forum_index} so that only published nodes are indexed.
- [forum_update_7012()](../modules/forum/forum.install/forum_update_7012.md) (function) — Add 'created' and 'last_comment_timestamp' indexes.
- [image_update_7001()](../modules/image/image.install/image_update_7001.md) (function) — Rename possibly misnamed {image_effect} table to {image_effects}.
- [image_update_7002()](../modules/image/image.install/image_update_7002.md) (function) — Add width and height columns to image field schema and populate.
- [image_update_7003()](../modules/image/image.install/image_update_7003.md) (function) — Remove the variables that set alt and title length since they were not used for database column size and could cause PDO exceptions.
- [image_update_7004()](../modules/image/image.install/image_update_7004.md) (function) — Use a large setting (512 and 1024 characters) for the length of the image alt and title fields.
- [image_update_7005()](../modules/image/image.install/image_update_7005.md) (function) — Add a column to the 'image_style' table to store administrative labels.
- [list_update_7002()](../modules/field/modules/list/list.install/list_update_7002.md) (function) — Re-apply list_update_7001() for deleted fields.
- [locale_update_7003()](../modules/locale/locale.install/locale_update_7003.md) (function) — Update "language_count" variable.
- [locale_update_7004()](../modules/locale/locale.install/locale_update_7004.md) (function) — Remove duplicates in {locales_source}.
- [locale_update_7005()](../modules/locale/locale.install/locale_update_7005.md) (function) — Increase {locales_languages}.formula column's length.
- [menu_update_7000()](../modules/menu/menu.install/menu_update_7000.md) (function) — Migrate the "Default menu for content" setting to individual node types.
- [menu_update_7001()](../modules/menu/menu.install/menu_update_7001.md) (function) — Rename "Primary Links" and "Secondary Links" to their Drupal 7 equivalents.
- [menu_update_7002()](../modules/menu/menu.install/menu_update_7002.md) (function) — Rename the primary/secondary menu blocks to match previously renamed menus.
- [menu_update_7003()](../modules/menu/menu.install/menu_update_7003.md) (function) — Add missing custom menus to active menus list.
- [node_update_7011()](../modules/node/node.install/node_update_7011.md) (function) — Update the database from Drupal 6 to match the schema.
- [node_update_7012()](../modules/node/node.install/node_update_7012.md) (function) — Switches body fields to untranslatable while upgrading from D6 and makes them language neutral.
- [node_update_7013()](../modules/node/node.install/node_update_7013.md) (function) — Change {node}.vid default value from 0 to NULL to avoid deadlock issues on MySQL.
- [node_update_7014()](../modules/node/node.install/node_update_7014.md) (function) — Add an index on {node}.language.
- [node_update_7015()](../modules/node/node.install/node_update_7015.md) (function) — Enable node types that may have been erroneously disabled in Drupal 7.36.
- [node_update_7016()](../modules/node/node.install/node_update_7016.md) (function) — Change {history}.nid to an unsigned int in order to match {node}.nid.
- [openid_update_7000()](../modules/openid/openid.install/openid_update_7000.md) (function) — Bind associations to their providers.
- [poll_update_7004()](../modules/poll/poll.install/poll_update_7004.md) (function) — Update the database to match the schema.
- [system_update_7070()](../modules/system/system.install/system_update_7070.md) (function) — Remove the obsolete 'drupal_badge_color' and 'drupal_badge_size' variables.
- [system_update_7071()](../modules/system/system.install/system_update_7071.md) (function) — Add index missed during upgrade, and fix field default.
- [system_update_7072()](../modules/system/system.install/system_update_7072.md) (function) — Remove the obsolete 'site_offline_message' variable.
- [system_update_7073()](../modules/system/system.install/system_update_7073.md) (function) — Add binary to {file_managed}, in case system_update_7034() was run without it.
- [system_update_7074()](../modules/system/system.install/system_update_7074.md) (function) — This update has been removed and will not run.
- [system_update_7076()](../modules/system/system.install/system_update_7076.md) (function) — Convert menu_links query strings into arrays.
- [system_update_7077()](../modules/system/system.install/system_update_7077.md) (function) — Revert {file_managed}.filename changed to a binary column.
- [system_update_7078()](../modules/system/system.install/system_update_7078.md) (function) — Add binary to {date_formats}.format.
- [system_update_7079()](../modules/system/system.install/system_update_7079.md) (function) — Convert the 'filesize' column in {file_managed} to a bigint.
- [system_update_7080()](../modules/system/system.install/system_update_7080.md) (function) — Convert the 'format' column in {date_format_locale} to case sensitive varchar.
- [system_update_7081()](../modules/system/system.install/system_update_7081.md) (function) — Remove the Drupal 6 default install profile if it is still in the database.
- [system_update_7082()](../modules/system/system.install/system_update_7082.md) (function) — Add 'jquery-extend-3.4.0.js' to the 'jquery' library.
- [system_update_7083()](../modules/system/system.install/system_update_7083.md) (function) — Add 'jquery-html-prefilter-3.5.0-backport.js' to the 'jquery' library.
- [system_update_7084()](../modules/system/system.install/system_update_7084.md) (function) — Rebuild JavaScript aggregates to include 'ajax.js' fix for Chrome 83.
- [system_update_7085()](../modules/system/system.install/system_update_7085.md) (function) — Remove FLoC-blocking variable.
- [system_update_7086()](../modules/system/system.install/system_update_7086.md) (function) — Prepare the schema and data of the sessions table for hashed session ids.
- [system_update_7087()](../modules/system/system.install/system_update_7087.md) (function) — Enable the Announcements module; see 7.100 Release Notes for opt-out details.
- [system_update_7088()](../modules/system/system.install/system_update_7088.md) (function) — Clear caches as registry has been altered.
- [taxonomy_update_7011()](../modules/taxonomy/taxonomy.install/taxonomy_update_7011.md) (function) — Drop unpublished nodes from the index.
- [trigger_update_7001()](../modules/trigger/trigger.install/trigger_update_7001.md) (function) — Increase the length of the "hook" field to 78 characters.
- [trigger_update_7002()](../modules/trigger/trigger.install/trigger_update_7002.md) (function) — Renames nodeapi to node.
- [user_update_7016()](../modules/user/user.install/user_update_7016.md) (function) — Update the database to match the schema.
- [user_update_7017()](../modules/user/user.install/user_update_7017.md) (function) — Update email templates to use new tokens.
- [user_update_7018()](../modules/user/user.install/user_update_7018.md) (function) — Ensure there is an index on {users}.picture.
- [user_update_7019()](../modules/user/user.install/user_update_7019.md) (function) — Ensure there is a combined index on {authmap}.uid and {authmap}.module.
- [user_update_7020()](../modules/user/user.install/user_update_7020.md) (function) — Add changed field to users table.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
