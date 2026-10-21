# modules/node/node.api.php

- **Source:** [local](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · 1334 lines
- **Module/theme:** node

## File documentation

```text
@file
Hooks provided by the Node module.
```

## Functions (derived index)

- [hook_node_grants()](hook_node_grants.md) — Inform the node access system what permissions the user has.
- [hook_node_access_records()](hook_node_access_records.md) — Set permissions for a node to be written to the database.
- [hook_node_access_records_alter()](hook_node_access_records_alter.md) — Alter permissions for a node before it is written to the database.
- [hook_node_grants_alter()](hook_node_grants_alter.md) — Alter user access rules when trying to view, edit or delete a node.
- [hook_node_operations()](hook_node_operations.md) — Add mass node operations.
- [hook_node_delete()](hook_node_delete.md) — Respond to node deletion.
- [hook_node_revision_delete()](hook_node_revision_delete.md) — Respond to deletion of a node revision.
- [hook_node_insert()](hook_node_insert.md) — Respond to creation of a new node.
- [hook_node_load()](hook_node_load.md) — Act on arbitrary nodes being loaded from the database.
- [hook_node_access()](hook_node_access.md) — Control access to a node.
- [hook_node_prepare()](hook_node_prepare.md) — Act on a node object about to be shown on the add/edit form.
- [hook_node_search_result()](hook_node_search_result.md) — Act on a node being displayed as a search result.
- [hook_node_presave()](hook_node_presave.md) — Act on a node being inserted or updated.
- [hook_node_update()](hook_node_update.md) — Respond to updates to a node.
- [hook_node_update_index()](hook_node_update_index.md) — Act on a node being indexed for searching.
- [hook_node_validate()](hook_node_validate.md) — Perform node validation before a node is created or updated.
- [hook_node_submit()](hook_node_submit.md) — Act on a node after validated form values have been copied to it.
- [hook_node_view()](hook_node_view.md) — Act on a node that is being assembled before rendering.
- [hook_node_view_alter()](hook_node_view_alter.md) — Alter the results of node_view().
- [hook_node_info()](hook_node_info.md) — Define module-provided node types.
- [hook_ranking()](hook_ranking.md) — Provide additional methods of scoring for core search results for nodes.
- [hook_node_type_insert()](hook_node_type_insert.md) — Respond to node type creation.
- [hook_node_type_update()](hook_node_type_update.md) — Respond to node type updates.
- [hook_node_type_delete()](hook_node_type_delete.md) — Respond to node type deletion.
- [hook_delete()](hook_delete.md) — Respond to node deletion.
- [hook_prepare()](hook_prepare.md) — Act on a node object about to be shown on the add/edit form.
- [hook_form()](hook_form.md) — Display a node editing form.
- [hook_insert()](hook_insert.md) — Respond to creation of a new node.
- [hook_load()](hook_load.md) — Act on nodes being loaded from the database.
- [hook_update()](hook_update.md) — Respond to updates to a node.
- [hook_validate()](hook_validate.md) — Perform node validation before a node is created or updated.
- [hook_view()](hook_view.md) — Display a node.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
