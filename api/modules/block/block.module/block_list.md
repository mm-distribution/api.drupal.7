# block_list()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 677–693 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L677-L693)
- **Module/theme:** block

## Signature

```php
function block_list($region)
```

## Documentation

```text
Returns all blocks in the specified region for the current user.

@param $region
  The name of a region.

@return
  An array of block objects, indexed with the module name and block delta
  concatenated with an underscore, thus: MODULE_DELTA. If you are displaying
  your blocks in one or two sidebars, you may check whether this array is
  empty to see how many columns are going to be displayed.

@todo
  Now that the block table has a primary key, we should use that as the
  array key instead of MODULE_DELTA.
```

## Code

```php
function block_list($region) {
  $blocks = &drupal_static(__FUNCTION__);

  if (!isset($blocks)) {
    $blocks = _block_load_blocks();
  }

  // Create an empty array if there are no entries.
  if (!isset($blocks[$region])) {
    $blocks[$region] = array();
  }
  else {
    $blocks[$region] = _block_render_blocks($blocks[$region]);
  }

  return $blocks[$region];
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
