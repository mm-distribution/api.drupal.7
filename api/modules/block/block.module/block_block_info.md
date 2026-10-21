# block_block_info()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 207–217 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L207-L217)
- **Module/theme:** block
- **Implements:** [hook_block_info()](../block.api.php/hook_block_info.md)

## Signature

```php
function block_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function block_block_info() {
  $blocks = array();

  $result = db_query('SELECT bid, info FROM {block_custom} ORDER BY info');
  foreach ($result as $block) {
    $blocks[$block->bid]['info'] = $block->info;
    // Not worth caching.
    $blocks[$block->bid]['cache'] = DRUPAL_NO_CACHE;
  }
  return $blocks;
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
