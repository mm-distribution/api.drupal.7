# modules/node/node.install

- **Source:** [local](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · 967 lines
- **Module/theme:** node

## File documentation

```text
@file
Install, update and uninstall functions for the node module.
```

## Functions (derived index)

- [node_schema()](node_schema.md) — Implements hook_schema().
- [node_install()](node_install.md) — Implements hook_install().
- [node_update_dependencies()](node_update_dependencies.md) — Implements hook_update_dependencies().
- [_update_7000_node_get_types()](_update_7000_node_get_types.md) — Utility function: fetch the node types directly from the database.
- [node_update_7000()](node_update_7000.md) — Upgrade the node type table and fix node type 'module' attribute to avoid name-space conflicts.
- [node_update_7001()](node_update_7001.md) — Rename {node_revisions} table to {node_revision}.
- [node_update_7002()](node_update_7002.md) — Extend the node_promote_status index to include all fields required for the node page query.
- [node_update_7003()](node_update_7003.md) — Remove the node_counter if the statistics module is uninstalled.
- [node_update_7004()](node_update_7004.md) — Extend the existing default preview and teaser settings to all node types.
- [node_update_7005()](node_update_7005.md) — Add status/comment/promote and sticky columns to the {node_revision} table.
- [node_update_7006()](node_update_7006.md) — Convert body and teaser from node properties to fields, and migrate status/comment/promote and sticky columns to the {node_revision} table.
- [node_update_7007()](node_update_7007.md) — Remove column min_word_count.
- [node_update_7008()](node_update_7008.md) — Split the 'administer nodes' permission from 'access content overview'.
- [node_update_7009()](node_update_7009.md) — Convert node languages from the empty string to LANGUAGE_NONE.
- [node_update_7010()](node_update_7010.md) — Add the {block_node_type} table.
- [node_update_7011()](node_update_7011.md) — Update the database from Drupal 6 to match the schema.
- [node_update_7012()](node_update_7012.md) — Switches body fields to untranslatable while upgrading from D6 and makes them language neutral.
- [node_update_7013()](node_update_7013.md) — Change {node}.vid default value from 0 to NULL to avoid deadlock issues on MySQL.
- [node_update_7014()](node_update_7014.md) — Add an index on {node}.language.
- [node_update_7015()](node_update_7015.md) — Enable node types that may have been erroneously disabled in Drupal 7.36.
- [node_update_7016()](node_update_7016.md) — Change {history}.nid to an unsigned int in order to match {node}.nid.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
