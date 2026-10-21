# modules/block/block.install

- **Source:** [local](../../../../source/modules/block/block.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install) · 494 lines
- **Module/theme:** block

## File documentation

```text
@file
Install, update and uninstall functions for the block module.
```

## Functions (derived index)

- [block_schema()](block_schema.md) — Implements hook_schema().
- [block_install()](block_install.md) — Implements hook_install().
- [block_update_dependencies()](block_update_dependencies.md) — Implements hook_update_dependencies().
- [block_update_7000()](block_update_7000.md) — Set system.weight to a low value for block module.
- [block_update_7002()](block_update_7002.md) — Rename {blocks} table to {block}, {blocks_roles} to {block_role} and {boxes} to {block_custom}.
- [block_update_7003()](block_update_7003.md) — Change the weight column to normal int.
- [block_update_7004()](block_update_7004.md) — Add new blocks to new regions, migrate custom variables to blocks.
- [block_update_7005()](block_update_7005.md) — Update the {block_custom}.format column.
- [block_update_7006()](block_update_7006.md) — Recreates cache_block table.
- [block_update_7007()](block_update_7007.md) — Change {block_custom}.format into varchar.
- [block_update_7008()](block_update_7008.md) — Update database to match Drupal 7 schema.
- [block_update_7009()](block_update_7009.md) — Increase {block}.title length to 255 characters.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
