# Updates from 6.x to 7.x

- **Topic id:** `updates-6.x-to-7.x`
- **Defined in:** [`modules/system/system.install`](../modules/system/system.install/_file.md), line 1887 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L1887)

## Documentation

```text
@defgroup updates-6.x-to-7.x Updates from 6.x to 7.x
@{
Update functions from 6.x to 7.x.
```

## Members (derived, 116)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [aggregator_update_7000()](../modules/aggregator/aggregator.install/aggregator_update_7000.md) (function) — Add hash column to aggregator_feed table.
- [aggregator_update_7001()](../modules/aggregator/aggregator.install/aggregator_update_7001.md) (function) — Add aggregator teaser length to settings from old global default teaser length
- [aggregator_update_7002()](../modules/aggregator/aggregator.install/aggregator_update_7002.md) (function) — Add queued timestamp.
- [block_update_7000()](../modules/block/block.install/block_update_7000.md) (function) — Set system.weight to a low value for block module.
- [block_update_7002()](../modules/block/block.install/block_update_7002.md) (function) — Rename {blocks} table to {block}, {blocks_roles} to {block_role} and {boxes} to {block_custom}.
- [block_update_7003()](../modules/block/block.install/block_update_7003.md) (function) — Change the weight column to normal int.
- [block_update_7004()](../modules/block/block.install/block_update_7004.md) (function) — Add new blocks to new regions, migrate custom variables to blocks.
- [block_update_7005()](../modules/block/block.install/block_update_7005.md) (function) — Update the {block_custom}.format column.
- [block_update_7006()](../modules/block/block.install/block_update_7006.md) (function) — Recreates cache_block table.
- [block_update_7007()](../modules/block/block.install/block_update_7007.md) (function) — Change {block_custom}.format into varchar.
- [comment_update_7000()](../modules/comment/comment.install/comment_update_7000.md) (function) — Rename comment display setting variables.
- [comment_update_7001()](../modules/comment/comment.install/comment_update_7001.md) (function) — Change comment status from published being 0 to being 1
- [comment_update_7002()](../modules/comment/comment.install/comment_update_7002.md) (function) — Rename {comments} table to {comment} and upgrade it.
- [comment_update_7003()](../modules/comment/comment.install/comment_update_7003.md) (function) — Split {comment}.timestamp into 'created' and 'changed', improve indexing on {comment}.
- [comment_update_7004()](../modules/comment/comment.install/comment_update_7004.md) (function) — Upgrade the {node_comment_statistics} table.
- [comment_update_7005()](../modules/comment/comment.install/comment_update_7005.md) (function) — Create the comment_body field.
- [comment_update_7006()](../modules/comment/comment.install/comment_update_7006.md) (function) — Migrate data from the comment field to field storage.
- [contact_update_7000()](../modules/contact/contact.install/contact_update_7000.md) (function) — Rename the threshold limit variable.
- [contact_update_7001()](../modules/contact/contact.install/contact_update_7001.md) (function) — Rename the administer contact forms permission.
- [contact_update_7002()](../modules/contact/contact.install/contact_update_7002.md) (function) — Enable the 'access user contact forms' for registered users by default.
- [contact_update_7003()](../modules/contact/contact.install/contact_update_7003.md) (function) — Change the weight column to normal int.
- [dblog_update_7001()](../modules/dblog/dblog.install/dblog_update_7001.md) (function) — Update the {watchdog} table.
- [field_sql_storage_update_7000()](../modules/field/modules/field_sql_storage/field_sql_storage.install/field_sql_storage_update_7000.md) (function) — Field SQL storage update version placeholder.
- [field_sql_storage_update_7001()](../modules/field/modules/field_sql_storage/field_sql_storage.install/field_sql_storage_update_7001.md) (function) — Remove the field_config_entity_type table and store 'entity_type' strings.
- [field_sql_storage_update_7002()](../modules/field/modules/field_sql_storage/field_sql_storage.install/field_sql_storage_update_7002.md) (function) — Fix primary keys in field revision data tables.
- [field_update_7000()](../modules/field/field.install/field_update_7000.md) (function) — Field update version placeholder.
- [field_update_7001()](../modules/field/field.install/field_update_7001.md) (function) — Fix fields definitions created during the d6 to d7 upgrade path.
- [filter_update_7000()](../modules/filter/filter.install/filter_update_7000.md) (function) — Upgrade the {filter_formats} table and rename it to {filter_format}.
- [filter_update_7001()](../modules/filter/filter.install/filter_update_7001.md) (function) — Break out "escape HTML filter" option to its own filter.
- [filter_update_7003()](../modules/filter/filter.install/filter_update_7003.md) (function) — Upgrade the {filter} table for core filters.
- [filter_update_7005()](../modules/filter/filter.install/filter_update_7005.md) (function) — Integrate text formats with the user permissions system.
- [filter_update_7008()](../modules/filter/filter.install/filter_update_7008.md) (function) — Grant usage of all text formats to user roles having the 'administer filters' permission.
- [filter_update_7009()](../modules/filter/filter.install/filter_update_7009.md) (function) — Converts fields that store serialized variables from text to blob.
- [filter_update_7010()](../modules/filter/filter.install/filter_update_7010.md) (function) — Change {filter_format}.format and {filter}.format into varchar.
- [locale_update_7000()](../modules/locale/locale.install/locale_update_7000.md) (function) — Add context field index and allow longer location.
- [locale_update_7001()](../modules/locale/locale.install/locale_update_7001.md) (function) — Upgrade language negotiation settings.
- [locale_update_7002()](../modules/locale/locale.install/locale_update_7002.md) (function) — Updates URL language negotiation by adding the URL fallback detection method.
- [node_update_7000()](../modules/node/node.install/node_update_7000.md) (function) — Upgrade the node type table and fix node type 'module' attribute to avoid name-space conflicts.
- [node_update_7001()](../modules/node/node.install/node_update_7001.md) (function) — Rename {node_revisions} table to {node_revision}.
- [node_update_7002()](../modules/node/node.install/node_update_7002.md) (function) — Extend the node_promote_status index to include all fields required for the node page query.
- [node_update_7003()](../modules/node/node.install/node_update_7003.md) (function) — Remove the node_counter if the statistics module is uninstalled.
- [node_update_7004()](../modules/node/node.install/node_update_7004.md) (function) — Extend the existing default preview and teaser settings to all node types.
- [node_update_7005()](../modules/node/node.install/node_update_7005.md) (function) — Add status/comment/promote and sticky columns to the {node_revision} table.
- [node_update_7006()](../modules/node/node.install/node_update_7006.md) (function) — Convert body and teaser from node properties to fields, and migrate status/comment/promote and sticky columns to the {node_revision} table.
- [node_update_7007()](../modules/node/node.install/node_update_7007.md) (function) — Remove column min_word_count.
- [node_update_7008()](../modules/node/node.install/node_update_7008.md) (function) — Split the 'administer nodes' permission from 'access content overview'.
- [node_update_7009()](../modules/node/node.install/node_update_7009.md) (function) — Convert node languages from the empty string to LANGUAGE_NONE.
- [node_update_7010()](../modules/node/node.install/node_update_7010.md) (function) — Add the {block_node_type} table.
- [openid_update_6000()](../modules/openid/openid.install/openid_update_6000.md) (function) — Add a table to store nonces.
- [statistics_update_7000()](../modules/statistics/statistics.install/statistics_update_7000.md) (function) — Update the {accesslog}.sid column to match the length of {sessions}.sid
- [system_update_7000()](../modules/system/system.install/system_update_7000.md) (function) — Rename blog and forum permissions to be consistent with other content types.
- [system_update_7001()](../modules/system/system.install/system_update_7001.md) (function) — Generate a cron key and save it in the variables table.
- [system_update_7002()](../modules/system/system.install/system_update_7002.md) (function) — Add a table to store blocked IP addresses.
- [system_update_7003()](../modules/system/system.install/system_update_7003.md) (function) — Update {blocked_ips} with valid IP addresses from {access}.
- [system_update_7004()](../modules/system/system.install/system_update_7004.md) (function) — Remove hardcoded numeric deltas from all blocks in core.
- [system_update_7005()](../modules/system/system.install/system_update_7005.md) (function) — Remove throttle columns and variables.
- [system_update_7007()](../modules/system/system.install/system_update_7007.md) (function) — Convert to new method of storing permissions.
- [system_update_7009()](../modules/system/system.install/system_update_7009.md) (function) — Rename the variable for primary links.
- [system_update_7011()](../modules/system/system.install/system_update_7011.md) (function) — Split the 'bypass node access' permission from 'administer nodes'.
- [system_update_7013()](../modules/system/system.install/system_update_7013.md) (function) — Convert default time zone offset to default time zone name.
- [system_update_7015()](../modules/system/system.install/system_update_7015.md) (function) — Change the user logout path.
- [system_update_7016()](../modules/system/system.install/system_update_7016.md) (function) — Remove custom datatype *_unsigned in PostgreSQL.
- [system_update_7017()](../modules/system/system.install/system_update_7017.md) (function) — Change the theme setting 'toggle_node_info' into a per content type variable.
- [system_update_7018()](../modules/system/system.install/system_update_7018.md) (function) — Shorten the {system}.type column and modify indexes.
- [system_update_7020()](../modules/system/system.install/system_update_7020.md) (function) — Enable field and field_ui modules.
- [system_update_7021()](../modules/system/system.install/system_update_7021.md) (function) — Change the PHP for settings permission.
- [system_update_7027()](../modules/system/system.install/system_update_7027.md) (function) — Enable field type modules.
- [system_update_7029()](../modules/system/system.install/system_update_7029.md) (function) — Add new 'view own unpublished content' permission for authenticated users. Preserves legacy behavior from Drupal 6.x.
- [system_update_7032()](../modules/system/system.install/system_update_7032.md) (function) — Alter field hostname to identifier in the {flood} table.
- [system_update_7033()](../modules/system/system.install/system_update_7033.md) (function) — Move CACHE_AGGRESSIVE to CACHE_NORMAL.
- [system_update_7034()](../modules/system/system.install/system_update_7034.md) (function) — Migrate the file path settings and create the new {file_managed} table.
- [system_update_7036()](../modules/system/system.install/system_update_7036.md) (function) — Split the 'access site in maintenance mode' permission from 'administer site configuration'.
- [system_update_7042()](../modules/system/system.install/system_update_7042.md) (function) — Upgrade the {url_alias} table and create a cache bin for path aliases.
- [system_update_7044()](../modules/system/system.install/system_update_7044.md) (function) — Drop the actions_aid table.
- [system_update_7045()](../modules/system/system.install/system_update_7045.md) (function) — Add expiration field to the {flood} table.
- [system_update_7046()](../modules/system/system.install/system_update_7046.md) (function) — Switch from the Minnelli theme if it is the default or admin theme.
- [system_update_7047()](../modules/system/system.install/system_update_7047.md) (function) — Normalize the front page path variable.
- [system_update_7048()](../modules/system/system.install/system_update_7048.md) (function) — Convert path languages from the empty string to LANGUAGE_NONE.
- [system_update_7049()](../modules/system/system.install/system_update_7049.md) (function) — Rename 'Default' profile to 'Standard.'
- [system_update_7050()](../modules/system/system.install/system_update_7050.md) (function) — Change {batch}.id column from serial to regular int.
- [system_update_7051()](../modules/system/system.install/system_update_7051.md) (function) — make the IP field IPv6 compatible
- [system_update_7052()](../modules/system/system.install/system_update_7052.md) (function) — Rename file to include_file in {menu_router} table.
- [system_update_7053()](../modules/system/system.install/system_update_7053.md) (function) — Upgrade standard blocks and menus.
- [system_update_7054()](../modules/system/system.install/system_update_7054.md) (function) — Remove {cache_*}.headers columns.
- [system_update_7055()](../modules/system/system.install/system_update_7055.md) (function) — Converts fields that store serialized variables from text to blob.
- [system_update_7057()](../modules/system/system.install/system_update_7057.md) (function) — Increase the size of session-ids.
- [system_update_7058()](../modules/system/system.install/system_update_7058.md) (function) — Remove cron semaphore variable.
- [system_update_7059()](../modules/system/system.install/system_update_7059.md) (function) — Create the {file_usage} table.
- [system_update_7060()](../modules/system/system.install/system_update_7060.md) (function) — Create fields in preparation for migrating upload.module to file.module.
- [system_update_7061()](../modules/system/system.install/system_update_7061.md) (function) — Migrate upload.module data to the newly created file field.
- [system_update_7062()](../modules/system/system.install/system_update_7062.md) (function) — Replace 'system_list' index with 'bootstrap' index on {system}.
- [system_update_7063()](../modules/system/system.install/system_update_7063.md) (function) — Delete {menu_links} records for 'type' => MENU_CALLBACK which would not appear in a fresh install.
- [system_update_7064()](../modules/system/system.install/system_update_7064.md) (function) — Remove block_callback field from {menu_router}.
- [system_update_7065()](../modules/system/system.install/system_update_7065.md) (function) — Remove the default value for sid.
- [system_update_7066()](../modules/system/system.install/system_update_7066.md) (function) — Migrate the 'file_directory_temp' variable.
- [system_update_7067()](../modules/system/system.install/system_update_7067.md) (function) — Grant administrators permission to view the administration theme.
- [system_update_7068()](../modules/system/system.install/system_update_7068.md) (function) — Update {url_alias}.language description.
- [system_update_7069()](../modules/system/system.install/system_update_7069.md) (function) — Remove the obsolete 'site_offline' variable.
- [tracker_update_7000()](../modules/tracker/tracker.install/tracker_update_7000.md) (function) — Create new tracker_node and tracker_user tables.
- [update_update_7000()](../modules/update/update.install/update_update_7000.md) (function) — Create a queue to store tasks for requests to fetch available update data.
- [update_update_7001()](../modules/update/update.install/update_update_7001.md) (function) — Recreates cache_update table.
- [user_update_7000()](../modules/user/user.install/user_update_7000.md) (function) — Increase the length of the password field to accommodate better hashes.
- [user_update_7001()](../modules/user/user.install/user_update_7001.md) (function) — Remove the 'threshold', 'mode' and 'sort' columns from the {users} table.
- [user_update_7002()](../modules/user/user.install/user_update_7002.md) (function) — Convert user time zones from time zone offsets to time zone names.
- [user_update_7003()](../modules/user/user.install/user_update_7003.md) (function) — Update user settings for cancelling user accounts.
- [user_update_7005()](../modules/user/user.install/user_update_7005.md) (function) — Changes the users table to allow longer e-mail addresses.
- [user_update_7006()](../modules/user/user.install/user_update_7006.md) (function) — Add module data to {role_permission}.
- [user_update_7007()](../modules/user/user.install/user_update_7007.md) (function) — Add a weight column to user roles.
- [user_update_7008()](../modules/user/user.install/user_update_7008.md) (function) — If 'user_register' variable was unset in Drupal 6, set it to be the same as the Drupal 6 default setting.
- [user_update_7009()](../modules/user/user.install/user_update_7009.md) (function) — Converts fields that store serialized variables from text to blob.
- [user_update_7010()](../modules/user/user.install/user_update_7010.md) (function) — Update the {user}.signature_format column.
- [user_update_7011()](../modules/user/user.install/user_update_7011.md) (function) — Placeholder function.
- [user_update_7012()](../modules/user/user.install/user_update_7012.md) (function) — Add the user's pictures to the {file_managed} table and make them managed files.
- [user_update_7013()](../modules/user/user.install/user_update_7013.md) (function) — Add user module file usage entries.
- [user_update_7014()](../modules/user/user.install/user_update_7014.md) (function) — Rename the 'post comments without approval' permission.
- [user_update_7015()](../modules/user/user.install/user_update_7015.md) (function) — Change {users}.signature_format into varchar.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
