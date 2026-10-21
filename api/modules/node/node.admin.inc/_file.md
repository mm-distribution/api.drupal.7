# modules/node/node.admin.inc

- **Source:** [local](../../../../source/modules/node/node.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc) · 708 lines
- **Module/theme:** node

## File documentation

```text
@file
Content administration and module settings UI.
```

## Functions (derived index)

- [node_configure_rebuild_confirm()](node_configure_rebuild_confirm.md) — Menu callback: confirm rebuilding of permissions.
- [node_configure_rebuild_confirm_submit()](node_configure_rebuild_confirm_submit.md) — Handler for wipe confirmation
- [node_node_operations()](node_node_operations.md) — Implements hook_node_operations().
- [node_filters()](node_filters.md) — List node administration filters that can be applied.
- [node_build_filter_query()](node_build_filter_query.md) — Applies filters for node administration filters based on session.
- [node_filter_form()](node_filter_form.md) — Returns the node administration filters form array to node_admin_content().
- [node_filter_form_submit()](node_filter_form_submit.md) — Form submission handler for node_filter_form().
- [node_mass_update()](node_mass_update.md) — Make mass update of nodes, changing all nodes in the $nodes array to update them with the field values in $updates.
- [_node_mass_update_helper()](_node_mass_update_helper.md) — Updates individual nodes when fewer than 10 are queued.
- [_node_mass_update_batch_process()](_node_mass_update_batch_process.md) — Implements callback_batch_operation().
- [_node_mass_update_batch_finished()](_node_mass_update_batch_finished.md) — Implements callback_batch_finished().
- [node_admin_content()](node_admin_content.md) — Page callback: Form constructor for the content administration form.
- [node_admin_nodes()](node_admin_nodes.md) — Form builder: Builds the node administration overview.
- [node_admin_nodes_validate()](node_admin_nodes_validate.md) — Validate node_admin_nodes form submissions.
- [node_admin_nodes_submit()](node_admin_nodes_submit.md) — Process node_admin_nodes form submissions.
- [node_multiple_delete_confirm()](node_multiple_delete_confirm.md) — Multiple node deletion confirmation form for node_admin_content().
- [node_multiple_delete_confirm_submit()](node_multiple_delete_confirm_submit.md) — Form submission handler for node_multiple_delete_confirm().

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
