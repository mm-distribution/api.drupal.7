# node_block_list_alter()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2508–2556 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2508-L2556)
- **Module/theme:** node
- **Implements:** [hook_block_list_alter()](../../block/block.api.php/hook_block_list_alter.md)

## Signature

```php
function node_block_list_alter(&$blocks)
```

## Documentation

```text
Implements hook_block_list_alter().

Check the content type specific visibilty settings. Remove the block if the
visibility conditions are not met.
```

## Code

```php
function node_block_list_alter(&$blocks) {
  global $theme_key;

  // Build an array of node types for each block.
  $block_node_types = array();
  $result = db_query('SELECT module, delta, type FROM {block_node_type}');
  foreach ($result as $record) {
    $block_node_types[$record->module][$record->delta][$record->type] = TRUE;
  }

  $node = menu_get_object();
  $node_types = node_type_get_types();
  if (arg(0) == 'node' && arg(1) == 'add' && arg(2)) {
    $node_add_arg = strtr(arg(2), '-', '_');
  }
  foreach ($blocks as $key => $block) {
    if (!isset($block->theme) || !isset($block->status) || $block->theme != $theme_key || $block->status != 1) {
      // This block was added by a contrib module, leave it in the list.
      continue;
    }

    // If a block has no node types associated, it is displayed for every type.
    // For blocks with node types associated, if the node type does not match
    // the settings from this block, remove it from the block list.
    if (isset($block_node_types[$block->module][$block->delta])) {
      if (!empty($node)) {
        // This is a node or node edit page.
        if (!isset($block_node_types[$block->module][$block->delta][$node->type])) {
          // This block should not be displayed for this node type.
          unset($blocks[$key]);
          continue;
        }
      }
      elseif (isset($node_add_arg) && isset($node_types[$node_add_arg])) {
        // This is a node creation page
        if (!isset($block_node_types[$block->module][$block->delta][$node_add_arg])) {
          // This block should not be displayed for this node type.
          unset($blocks[$key]);
          continue;
        }
      }
      else {
        // This is not a node page, remove the block.
        unset($blocks[$key]);
        continue;
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
