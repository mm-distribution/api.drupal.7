# block_update_7002()

- **Type:** Function
- **File:** [`modules/block/block.install`](_file.md), lines 226–231 · [local source](../../../../source/modules/block/block.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install#L226-L231)
- **Module/theme:** block
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function block_update_7002()
```

## Documentation

```text
Rename {blocks} table to {block}, {blocks_roles} to {block_role} and
{boxes} to {block_custom}.
```

## Code

```php
function block_update_7002() {
  db_drop_index('blocks', 'list');
  db_rename_table('blocks', 'block');
  db_rename_table('blocks_roles', 'block_role');
  db_rename_table('boxes', 'block_custom');
}
```

---
_Drupal 7.103 · [modules/block/block.install](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install) · Licensed GPL-2.0-or-later (see LICENSE)._
