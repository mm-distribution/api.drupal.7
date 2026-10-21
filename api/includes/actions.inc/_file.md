# includes/actions.inc

- **Source:** [local](../../../source/includes/actions.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc) · 389 lines

## File documentation

```text
@file
This is the actions engine for executing stored actions.
```

## Functions (derived index)

- [actions_do()](actions_do.md) — Performs a given list of actions by executing their callback functions.
- [actions_list()](actions_list.md) — Discovers all available actions by invoking hook_action_info().
- [actions_get_all_actions()](actions_get_all_actions.md) — Retrieves all action instances from the database.
- [actions_actions_map()](actions_actions_map.md) — Creates an associative array keyed by hashes of function names or IDs.
- [actions_function_lookup()](actions_function_lookup.md) — Returns an action array key (function or ID), given its hash.
- [actions_synchronize()](actions_synchronize.md) — Synchronizes actions that are provided by modules in hook_action_info().
- [actions_save()](actions_save.md) — Saves an action and its user-supplied parameter values to the database.
- [actions_load()](actions_load.md) — Retrieves a single action from the database.
- [actions_delete()](actions_delete.md) — Deletes a single action from the database.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
