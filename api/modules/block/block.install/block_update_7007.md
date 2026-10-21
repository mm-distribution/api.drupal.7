# block_update_7007()

- **Type:** Function
- **File:** [`modules/block/block.install`](_file.md), lines 450–457 · [local source](../../../../source/modules/block/block.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install#L450-L457)
- **Module/theme:** block
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function block_update_7007()
```

## Documentation

```text
Change {block_custom}.format into varchar.
```

## Code

```php
function block_update_7007() {
  db_change_field('block_custom', 'format', 'format', array(
    'type' => 'varchar',
    'length' => 255,
    'not null' => FALSE,
    'description' => 'The {filter_format}.format of the block body.',
  ));
}
```

---
_Drupal 7.103 · [modules/block/block.install](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install) · Licensed GPL-2.0-or-later (see LICENSE)._
