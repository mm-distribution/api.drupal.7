# block_update_7006()

- **Type:** Function
- **File:** [`modules/block/block.install`](_file.md), lines 440–445 · [local source](../../../../source/modules/block/block.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install#L440-L445)
- **Module/theme:** block
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function block_update_7006()
```

## Documentation

```text
Recreates cache_block table.

Converts fields that hold serialized variables from text to blob.
Removes 'headers' column.
```

## Code

```php
function block_update_7006() {
  $schema = system_schema_cache_7054();

  db_drop_table('cache_block');
  db_create_table('cache_block', $schema);
}
```

---
_Drupal 7.103 · [modules/block/block.install](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install) · Licensed GPL-2.0-or-later (see LICENSE)._
