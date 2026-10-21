# Actions

- **Topic id:** `actions`
- **Defined in:** [`includes/actions.inc`](../includes/actions.inc/_file.md), line 8 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc#L8)

## Documentation

```text
@defgroup actions Actions
@{
Functions that perform an action on a certain system object.

Action functions are declared by modules by implementing hook_action_info().
Modules can cause action functions to run by calling actions_do(), and
trigger.module provides a user interface that lets administrators define
events that cause action functions to run.

Each action function takes two to four arguments:
- $entity: The object that the action acts on, such as a node, comment, or
  user.
- $context: Array of additional information about what triggered the action.
- $a1, $a2: Optional additional information, which can be passed into
  actions_do() and will be passed along to the action function.

@}
```

## Members (derived, 21)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [actions_do()](../includes/actions.inc/actions_do.md) (function) — Performs a given list of actions by executing their callback functions.
- [comment_publish_action()](../modules/comment/comment.module/comment_publish_action.md) (function) — Publishes a comment.
- [comment_save_action()](../modules/comment/comment.module/comment_save_action.md) (function) — Saves a comment.
- [comment_unpublish_action()](../modules/comment/comment.module/comment_unpublish_action.md) (function) — Unpublishes a comment.
- [comment_unpublish_by_keyword_action()](../modules/comment/comment.module/comment_unpublish_by_keyword_action.md) (function) — Unpublishes a comment if it contains certain keywords.
- [hook_action_info()](../modules/system/system.api.php/hook_action_info.md) (function) — Declares information about actions.
- [node_assign_owner_action()](../modules/node/node.module/node_assign_owner_action.md) (function) — Assigns ownership of a node to a user.
- [node_make_sticky_action()](../modules/node/node.module/node_make_sticky_action.md) (function) — Sets the sticky-at-top-of-list property of a node to 1.
- [node_make_unsticky_action()](../modules/node/node.module/node_make_unsticky_action.md) (function) — Sets the sticky-at-top-of-list property of a node to 0.
- [node_promote_action()](../modules/node/node.module/node_promote_action.md) (function) — Sets the promote property of a node to 1.
- [node_publish_action()](../modules/node/node.module/node_publish_action.md) (function) — Sets the status of a node to 1 (published).
- [node_save_action()](../modules/node/node.module/node_save_action.md) (function) — Saves a node.
- [node_unpromote_action()](../modules/node/node.module/node_unpromote_action.md) (function) — Sets the promote property of a node to 0.
- [node_unpublish_action()](../modules/node/node.module/node_unpublish_action.md) (function) — Sets the status of a node to 0 (unpublished).
- [node_unpublish_by_keyword_action()](../modules/node/node.module/node_unpublish_by_keyword_action.md) (function) — Unpublishes a node containing certain keywords.
- [system_block_ip_action()](../modules/system/system.module/system_block_ip_action.md) (function) — Blocks the current user's IP address.
- [system_goto_action()](../modules/system/system.module/system_goto_action.md) (function) — Redirects to a different URL.
- [system_message_action()](../modules/system/system.module/system_message_action.md) (function) — Sends a message to the current user's screen.
- [system_send_email_action()](../modules/system/system.module/system_send_email_action.md) (function) — Sends an e-mail message.
- [user_block_user_action()](../modules/user/user.module/user_block_user_action.md) (function) — Blocks a specific user or the current user, if one is not specified.
- [user_unblock_user_action()](../modules/user/user.module/user_unblock_user_action.md) (function) — Unblocks a specific user or the current user, if one is not specified.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
