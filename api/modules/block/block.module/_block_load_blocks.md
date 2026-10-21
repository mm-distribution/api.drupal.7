# _block_load_blocks()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 732–756 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L732-L756)
- **Module/theme:** block

## Signature

```php
function _block_load_blocks()
```

## Documentation

```text
Loads blocks' information from the database.

@return
  An array of blocks grouped by region.
```

## Code

```php
function _block_load_blocks() {
  global $theme_key;

  $query = db_select('block', 'b');
  $result = $query
    ->fields('b')
    ->condition('b.theme', $theme_key)
    ->condition('b.status', 1)
    ->orderBy('b.region')
    ->orderBy('b.weight')
    ->orderBy('b.module')
    ->addTag('block_load')
    ->addTag('translatable')
    ->execute();

  $block_info = $result->fetchAllAssoc('bid');
  // Allow modules to modify the block list.
  drupal_alter('block_list', $block_info);

  $blocks = array();
  foreach ($block_info as $block) {
    $blocks[$block->region]["{$block->module}_{$block->delta}"] = $block;
  }
  return $blocks;
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
