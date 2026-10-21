# modules/trigger/trigger.module

- **Source:** [local](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · 672 lines
- **Module/theme:** trigger

## File documentation

```text
@file
Enables functions to be stored and executed at a later time.
```

## Functions (derived index)

- [trigger_help()](trigger_help.md) — Implements hook_help().
- [trigger_menu()](trigger_menu.md) — Implements hook_menu().
- [trigger_menu_unassign_access()](trigger_menu_unassign_access.md) — Access callback: Determines if triggers can be unassigned.
- [trigger_trigger_info()](trigger_trigger_info.md) — Implements hook_trigger_info().
- [trigger_get_assigned_actions()](trigger_get_assigned_actions.md) — Gets the action IDs of actions to be executed for a hook.
- [trigger_theme()](trigger_theme.md) — Implements hook_theme().
- [trigger_forms()](trigger_forms.md) — Implements hook_forms().
- [_trigger_normalize_node_context()](_trigger_normalize_node_context.md) — Loads associated objects for node triggers.
- [_trigger_node()](_trigger_node.md) — Calls action functions for node triggers.
- [trigger_node_view()](trigger_node_view.md) — Implements hook_node_view().
- [trigger_node_update()](trigger_node_update.md) — Implements hook_node_update().
- [trigger_node_presave()](trigger_node_presave.md) — Implements hook_node_presave().
- [trigger_node_insert()](trigger_node_insert.md) — Implements hook_node_insert().
- [trigger_node_delete()](trigger_node_delete.md) — Implements hook_node_delete().
- [_trigger_normalize_comment_context()](_trigger_normalize_comment_context.md) — Loads associated objects for comment triggers.
- [trigger_comment_presave()](trigger_comment_presave.md) — Implements hook_comment_presave().
- [trigger_comment_insert()](trigger_comment_insert.md) — Implements hook_comment_insert().
- [trigger_comment_update()](trigger_comment_update.md) — Implements hook_comment_update().
- [trigger_comment_delete()](trigger_comment_delete.md) — Implements hook_comment_delete().
- [trigger_comment_view()](trigger_comment_view.md) — Implements hook_comment_view().
- [_trigger_comment()](_trigger_comment.md) — Calls action functions for comment triggers.
- [trigger_cron()](trigger_cron.md) — Implements hook_cron().
- [_trigger_normalize_user_context()](_trigger_normalize_user_context.md) — Loads associated objects for user triggers.
- [trigger_user_login()](trigger_user_login.md) — Implements hook_user_login().
- [trigger_user_logout()](trigger_user_logout.md) — Implements hook_user_logout().
- [trigger_user_insert()](trigger_user_insert.md) — Implements hook_user_insert().
- [trigger_user_update()](trigger_user_update.md) — Implements hook_user_update().
- [trigger_user_cancel()](trigger_user_cancel.md) — Implements hook_user_cancel().
- [trigger_user_delete()](trigger_user_delete.md) — Implements hook_user_delete().
- [trigger_user_view()](trigger_user_view.md) — Implements hook_user_view().
- [_trigger_user()](_trigger_user.md) — Calls action functions for user triggers.
- [_trigger_taxonomy()](_trigger_taxonomy.md) — Calls action functions for taxonomy triggers.
- [trigger_taxonomy_term_insert()](trigger_taxonomy_term_insert.md) — Implements hook_taxonomy_term_insert().
- [trigger_taxonomy_term_update()](trigger_taxonomy_term_update.md) — Implements hook_taxonomy_term_update().
- [trigger_taxonomy_term_delete()](trigger_taxonomy_term_delete.md) — Implements hook_taxonomy_term_delete().
- [trigger_actions_delete()](trigger_actions_delete.md) — Implements hook_actions_delete().
- [_trigger_get_all_info()](_trigger_get_all_info.md) — Retrieves and caches information from hook_trigger_info() implementations.
- [_trigger_tab_information()](_trigger_tab_information.md) — Gathers information about tabs on the triggers administration screen.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
