# block_load()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 710–724 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L710-L724)
- **Module/theme:** block

## Signature

```php
function block_load($module, $delta)
```

## Documentation

```text
Loads a block object from the database.

This function returns the first block matching the module and delta
parameters, so it should not be used for theme-specific functionality.

@param $module
  Name of the module that implements the block to load.
@param $delta
  Unique ID of the block within the context of $module. Pass NULL to return
  an empty block object for $module.

@return
  A block object.
```

## Code

```php
function block_load($module, $delta) {
  if (isset($delta)) {
    $block = db_query('SELECT * FROM {block} WHERE module = :module AND delta = :delta', array(':module' => $module, ':delta' => $delta))->fetchObject();
  }

  // If the block does not exist in the database yet return a stub block
  // object.
  if (empty($block)) {
    $block = new stdClass();
    $block->module = $module;
    $block->delta = $delta;
  }

  return $block;
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
