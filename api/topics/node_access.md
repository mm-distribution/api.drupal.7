# Node access rights

- **Topic id:** `node_access`
- **Defined in:** [`modules/node/node.module`](../modules/node/node.module/_file.md), line 2925 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2925)

## Documentation

```text
@defgroup node_access Node access rights
@{
The node access system determines who can do what to which nodes.

In determining access rights for a node, node_access() first checks whether
the user has the "bypass node access" permission. Such users have
unrestricted access to all nodes. user 1 will always pass this check.

Next, all implementations of hook_node_access() will be called. Each
implementation may explicitly allow, explicitly deny, or ignore the access
request. If at least one module says to deny the request, it will be rejected.
If no modules deny the request and at least one says to allow it, the request
will be permitted.

If all modules ignore the access request, then the node_access table is used
to determine access. All node access modules are queried using
hook_node_grants() to assemble a list of "grant IDs" for the user. This list
is compared against the table. If any row contains the node ID in question
(or 0, which stands for "all nodes"), one of the grant IDs returned, and a
value of TRUE for the operation in question, then access is granted. Note
that this table is a list of grants; any matching row is sufficient to
grant access to the node.

In node listings (lists of nodes generated from a select query, such as the
default home page at path 'node', an RSS feed, a recent content block, etc.),
the process above is followed except that hook_node_access() is not called on
each node for performance reasons and for proper functioning of the pager
system. When adding a node listing to your module, be sure to use a dynamic
query created by db_select() and add a tag of "node_access". This will allow
modules dealing with node access to ensure only nodes to which the user has
access are retrieved, through the use of hook_query_TAG_alter(). Tagging a
query with "node_access" does not check the published/unpublished status of
nodes, so the base query is responsible for ensuring that unpublished nodes
are not displayed to inappropriate users.

Note: Even a single module returning NODE_ACCESS_DENY from hook_node_access()
will block access to the node. Therefore, implementers should take care to
not deny access unless they really intend to. Unless a module wishes to
actively deny access it should return NODE_ACCESS_IGNORE (or simply return
nothing) to allow other modules or the node_access table to control access.

To see how to write a node access module of your own, see
node_access_example.module.
```

## Members (derived, 21)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_node_access_rebuild_batch_finished()](../modules/node/node.module/_node_access_rebuild_batch_finished.md) (function) — Implements callback_batch_finished().
- [_node_access_rebuild_batch_operation()](../modules/node/node.module/_node_access_rebuild_batch_operation.md) (function) — Implements callback_batch_operation().
- [_node_query_node_access_alter()](../modules/node/node.module/_node_query_node_access_alter.md) (function) — Helper for node access functions.
- [hook_node_access()](../modules/node/node.api.php/hook_node_access.md) (function) — Control access to a node.
- [hook_node_access_records()](../modules/node/node.api.php/hook_node_access_records.md) (function) — Set permissions for a node to be written to the database.
- [hook_node_access_records_alter()](../modules/node/node.api.php/hook_node_access_records_alter.md) (function) — Alter permissions for a node before it is written to the database.
- [hook_node_grants()](../modules/node/node.api.php/hook_node_grants.md) (function) — Inform the node access system what permissions the user has.
- [hook_node_grants_alter()](../modules/node/node.api.php/hook_node_grants_alter.md) (function) — Alter user access rules when trying to view, edit or delete a node.
- [node_access()](../modules/node/node.module/node_access.md) (function) — Determines whether the current user may perform the operation on the node.
- [node_access_acquire_grants()](../modules/node/node.module/node_access_acquire_grants.md) (function) — Gets the list of node access grants and writes them to the database.
- [node_access_grants()](../modules/node/node.module/node_access_grants.md) (function) — Fetches an array of permission IDs granted to the given user ID.
- [node_access_needs_rebuild()](../modules/node/node.module/node_access_needs_rebuild.md) (function) — Flags or unflags the node access grants for rebuilding.
- [node_access_rebuild()](../modules/node/node.module/node_access_rebuild.md) (function) — Rebuilds the node access database.
- [node_access_view_all_nodes()](../modules/node/node.module/node_access_view_all_nodes.md) (function) — Determines whether the user has a global viewing grant for all nodes.
- [node_access_write_grants()](../modules/node/node.module/node_access_write_grants.md) (function) — Writes a list of grants to the database, deleting any previously saved ones.
- [node_add_node_grants_to_query()](../modules/node/node.module/node_add_node_grants_to_query.md) (function) — Helper function to create the or condition for a node grants check.
- [node_list_permissions()](../modules/node/node.module/node_list_permissions.md) (function) — Helper function to generate standard node permission list for a given type.
- [node_node_access()](../modules/node/node.module/node_node_access.md) (function) — Implements hook_node_access().
- [node_permissions_get_configured_types()](../modules/node/node.module/node_permissions_get_configured_types.md) (function) — Returns an array of node types that should be managed by permissions.
- [node_query_entity_field_access_alter()](../modules/node/node.module/node_query_entity_field_access_alter.md) (function) — Implements hook_query_TAG_alter().
- [node_query_node_access_alter()](../modules/node/node.module/node_query_node_access_alter.md) (function) — Implements hook_query_TAG_alter().

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
