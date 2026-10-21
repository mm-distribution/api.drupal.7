# hook_block_list_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/block/block.api.php`](_file.md), lines 333–364 · [local source](../../../../source/modules/block/block.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php#L333-L364)
- **Module/theme:** block
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_block_list_alter(&$blocks)
```

## Documentation

```text
Act on blocks prior to rendering.

This hook allows you to add, remove or modify blocks in the block list. The
block list contains the block definitions, not the rendered blocks. The
blocks are rendered after the modules have had a chance to manipulate the
block list.

You can also set $block->content here, which will override the content of the
block and prevent hook_block_view() from running.

@param $blocks
  An array of $blocks, keyed by the block ID.
```

## Code

```php
function hook_block_list_alter(&$blocks) {
  global $language, $theme_key;

  // This example shows how to achieve language specific visibility setting for
  // blocks.

  $result = db_query('SELECT module, delta, language FROM {my_table}');
  $block_languages = array();
  foreach ($result as $record) {
    $block_languages[$record->module][$record->delta][$record->language] = TRUE;
  }

  foreach ($blocks as $key => $block) {
    // Any module using this alter should inspect the data before changing it,
    // to ensure it is what they expect.
    if (!isset($block->theme) || !isset($block->status) || $block->theme != $theme_key || $block->status != 1) {
      // This block was added by a contrib module, leave it in the list.
      continue;
    }

    if (!isset($block_languages[$block->module][$block->delta])) {
      // No language setting for this block, leave it in the list.
      continue;
    }

    if (!isset($block_languages[$block->module][$block->delta][$language->language])) {
      // This block should not be displayed with the active language, remove
      // from the list.
      unset($blocks[$key]);
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_block_list_alter()".

- [block_block_list_alter()](../block.module/block_block_list_alter.md) — `modules/block/block.module`
- [dashboard_block_list_alter()](../../dashboard/dashboard.module/dashboard_block_list_alter.md) — `modules/dashboard/dashboard.module`
- [node_block_list_alter()](../../node/node.module/node_block_list_alter.md) — `modules/node/node.module`
- [overlay_block_list_alter()](../../overlay/overlay.module/overlay_block_list_alter.md) — `modules/overlay/overlay.module`

---
_Drupal 7.103 · [modules/block/block.api.php](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
