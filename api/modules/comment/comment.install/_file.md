# modules/comment/comment.install

- **Source:** [local](../../../../source/modules/comment/comment.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install) · 576 lines
- **Module/theme:** comment

## File documentation

```text
@file
Install, update and uninstall functions for the comment module.
```

## Functions (derived index)

- [comment_uninstall()](comment_uninstall.md) — Implements hook_uninstall().
- [comment_enable()](comment_enable.md) — Implements hook_enable().
- [comment_modules_enabled()](comment_modules_enabled.md) — Implements hook_modules_enabled().
- [comment_update_dependencies()](comment_update_dependencies.md) — Implements hook_update_dependencies().
- [comment_update_7000()](comment_update_7000.md) — Rename comment display setting variables.
- [comment_update_7001()](comment_update_7001.md) — Change comment status from published being 0 to being 1
- [comment_update_7002()](comment_update_7002.md) — Rename {comments} table to {comment} and upgrade it.
- [comment_update_7003()](comment_update_7003.md) — Split {comment}.timestamp into 'created' and 'changed', improve indexing on {comment}.
- [comment_update_7004()](comment_update_7004.md) — Upgrade the {node_comment_statistics} table.
- [comment_update_7005()](comment_update_7005.md) — Create the comment_body field.
- [comment_update_7006()](comment_update_7006.md) — Migrate data from the comment field to field storage.
- [comment_update_7007()](comment_update_7007.md) — Add an index to the created column.
- [comment_update_7008()](comment_update_7008.md) — Update database to match Drupal 7 schema.
- [comment_update_7009()](comment_update_7009.md) — Change the last_comment_timestamp column description.
- [comment_schema()](comment_schema.md) — Implements hook_schema().

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
