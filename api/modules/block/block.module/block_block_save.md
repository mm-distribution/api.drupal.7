# block_block_save()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 235–237 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L235-L237)
- **Module/theme:** block
- **Implements:** [hook_block_save()](../block.api.php/hook_block_save.md)

## Signature

```php
function block_block_save($delta = 0, $edit = array())
```

## Documentation

```text
Implements hook_block_save().
```

## Code

```php
function block_block_save($delta = 0, $edit = array()) {
  block_custom_block_save($edit, $delta);
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
