# modules/node/node.pages.inc

- **Source:** [local](../../../../source/modules/node/node.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc) · 681 lines
- **Module/theme:** node

## File documentation

```text
@file
Page callbacks for adding, editing, deleting, and revisions management for content.
```

## Functions (derived index)

- [node_page_edit()](node_page_edit.md) — Menu callback; presents the node editing form.
- [node_add_page()](node_add_page.md) — Page callback: Displays add content links for available content types.
- [theme_node_add_list()](theme_node_add_list.md) — Returns HTML for a list of available node types for node creation.
- [node_add()](node_add.md) — Returns a node submission form.
- [node_form_validate()](node_form_validate.md) — Form validation handler for node_form().
- [node_form()](node_form.md) — Form constructor for the node add/edit form.
- [node_form_delete_submit()](node_form_delete_submit.md) — Form submission handler for node_form().
- [node_form_build_preview()](node_form_build_preview.md) — Form submission handler for node_form().
- [node_preview()](node_preview.md) — Generates a node preview.
- [theme_node_preview()](theme_node_preview.md) — Returns HTML for a node preview for display during node creation and editing.
- [node_form_submit()](node_form_submit.md) — Form submission handler for node_form().
- [node_form_submit_build_node()](node_form_submit_build_node.md) — Updates the form state's node entity by processing this submission's values.
- [node_delete_confirm()](node_delete_confirm.md) — Form constructor for the node deletion confirmation form.
- [node_delete_confirm_submit()](node_delete_confirm_submit.md) — Executes node deletion.
- [node_revision_overview()](node_revision_overview.md) — Generates an overview table of older revisions of a node.
- [node_revision_revert_confirm()](node_revision_revert_confirm.md) — Asks for confirmation of the reversion to prevent against CSRF attacks.
- [node_revision_revert_confirm_submit()](node_revision_revert_confirm_submit.md) — Form submission handler for node_revision_revert_confirm().
- [node_revision_delete_confirm()](node_revision_delete_confirm.md) — Form constructor for the revision deletion confirmation form.
- [node_revision_delete_confirm_submit()](node_revision_delete_confirm_submit.md) — Form submission handler for node_revision_delete_confirm().

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
