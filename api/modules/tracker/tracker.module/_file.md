# modules/tracker/tracker.module

- **Source:** [local](../../../../source/modules/tracker/tracker.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module) · 389 lines
- **Module/theme:** tracker

## File documentation

```text
@file
Tracks recent content posted by a user or users.
```

## Functions (derived index)

- [tracker_help()](tracker_help.md) — Implements hook_help().
- [tracker_menu()](tracker_menu.md) — Implements hook_menu().
- [tracker_cron()](tracker_cron.md) — Implements hook_cron().
- [_tracker_myrecent_access()](_tracker_myrecent_access.md) — Access callback for tracker/%user_uid_optional.
- [_tracker_user_access()](_tracker_user_access.md) — Access callback for user/%user/track.
- [tracker_node_insert()](tracker_node_insert.md) — Implements hook_node_insert().
- [tracker_node_update()](tracker_node_update.md) — Implements hook_node_update().
- [tracker_node_delete()](tracker_node_delete.md) — Implements hook_node_delete().
- [tracker_comment_update()](tracker_comment_update.md) — Implements hook_comment_update().
- [tracker_comment_publish()](tracker_comment_publish.md) — Implements hook_comment_publish().
- [tracker_comment_unpublish()](tracker_comment_unpublish.md) — Implements hook_comment_unpublish().
- [tracker_comment_delete()](tracker_comment_delete.md) — Implements hook_comment_delete().
- [_tracker_add()](_tracker_add.md) — Updates indexing tables when a node is added, updated, or commented on.
- [_tracker_calculate_changed()](_tracker_calculate_changed.md) — Determines the max timestamp between $node->changed and the last comment.
- [_tracker_remove()](_tracker_remove.md) — Cleans up indexed data when nodes or comments are removed.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
