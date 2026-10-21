# block_update_7009()

- **Type:** Function
- **File:** [`modules/block/block.install`](_file.md), lines 478–489 · [local source](../../../../source/modules/block/block.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install#L478-L489)
- **Module/theme:** block
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function block_update_7009()
```

## Documentation

```text
Increase {block}.title length to 255 characters.
```

## Code

```php
function block_update_7009() {
  db_change_field('block', 'title', 'title',
    array(
      'type' => 'varchar',
      'length' => 255,
      'not null' => TRUE,
      'default' => '',
      'description' => 'Custom title for the block. (Empty string will use block default title, <none> will remove the title, text will cause block to use specified title.)',
      'translatable' => TRUE,
    )
  );
}
```

---
_Drupal 7.103 · [modules/block/block.install](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install) · Licensed GPL-2.0-or-later (see LICENSE)._
