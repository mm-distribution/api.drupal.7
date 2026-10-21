# block_get_blocks_by_region()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 316–322 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L316-L322)
- **Module/theme:** block

## Signature

```php
function block_get_blocks_by_region($region)
```

## Documentation

```text
Gets a renderable array of a region containing all enabled blocks.

@param $region
  The requested region.

@return
  A renderable array of a region containing all enabled blocks.
```

## Code

```php
function block_get_blocks_by_region($region) {
  $build = array();
  if ($list = block_list($region)) {
    $build = _block_get_renderable_array($list);
  }
  return $build;
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
