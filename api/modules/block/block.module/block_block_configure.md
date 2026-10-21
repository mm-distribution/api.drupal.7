# block_block_configure()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 222–230 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L222-L230)
- **Module/theme:** block
- **Implements:** [hook_block_configure()](../block.api.php/hook_block_configure.md)

## Signature

```php
function block_block_configure($delta = 0)
```

## Documentation

```text
Implements hook_block_configure().
```

## Code

```php
function block_block_configure($delta = 0) {
  if ($delta) {
    $custom_block = block_custom_block_get($delta);
  }
  else {
    $custom_block = array();
  }
  return block_custom_block_form($custom_block);
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
