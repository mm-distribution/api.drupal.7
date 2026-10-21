# _block_rehash()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 372–487 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L372-L487)
- **Module/theme:** block

## Signature

```php
function _block_rehash($theme = NULL)
```

## Documentation

```text
Updates the 'block' DB table with the blocks currently exported by modules.

@param $theme
  The theme to rehash blocks for. If not provided, defaults to the currently
  used theme.

@return
  Blocks currently exported by modules.
```

## Code

```php
function _block_rehash($theme = NULL) {
  global $theme_key;

  drupal_theme_initialize();
  if (!isset($theme)) {
    // If theme is not specifically set, rehash for the current theme.
    $theme = $theme_key;
  }
  $regions = system_region_list($theme);

  // These are the blocks the function will return.
  $blocks = array();
  // These are the blocks defined by code and modified by the database.
  $current_blocks = array();
  // These are {block}.bid values to be kept.
  $bids = array();
  $or = db_or();
  // Gather the blocks defined by modules.
  foreach (module_implements('block_info') as $module) {
    $module_blocks = module_invoke($module, 'block_info');
    $delta_list = array();
    foreach ($module_blocks as $delta => $block) {
      // Compile a condition to retrieve this block from the database.
      // Add identifiers.
      $delta_list[] = $delta;
      $block['module'] = $module;
      $block['delta'] = $delta;
      $block['theme'] = $theme;
      $current_blocks[$module][$delta] = $block;
    }
    if (!empty($delta_list)) {
      $condition = db_and()->condition('module', $module)->condition('delta', $delta_list);
      $or->condition($condition);
    }
  }
  // Save the blocks defined in code for alter context.
  $code_blocks = $current_blocks;
  $database_blocks = db_select('block', 'b', array('fetch' => PDO::FETCH_ASSOC))
    ->fields('b')
    ->condition($or)
    ->condition('theme', $theme)
    ->execute();
  $original_database_blocks = array();
  foreach ($database_blocks as $block) {
    $module = $block['module'];
    $delta = $block['delta'];
    $original_database_blocks[$module][$delta] = $block;
    // The cache mode can only by set from hook_block_info(), so that has
    // precedence over the database's value.
    if (isset($current_blocks[$module][$delta]['cache'])) {
      $block['cache'] = $current_blocks[$module][$delta]['cache'];
    }
    // Preserve info which is not in the database.
    $block['info'] = $current_blocks[$module][$delta]['info'];
    // Blocks stored in the database override the blocks defined in code.
    $current_blocks[$module][$delta] = $block;
    // Preserve this block.
    $bids[$block['bid']] = $block['bid'];
  }
  drupal_alter('block_info', $current_blocks, $theme, $code_blocks);
  foreach ($current_blocks as $module => $module_blocks) {
    foreach ($module_blocks as $delta => $block) {
      // Make sure certain attributes are set.
      $block += array(
        'pages' => '',
        'weight' => 0,
        'status' => 0,
      );
      // Check for active blocks in regions that are not available.
      if (!empty($block['region']) && $block['region'] != BLOCK_REGION_NONE && !isset($regions[$block['region']]) && $block['status'] == 1) {
        drupal_set_message(t('The block %info was assigned to the invalid region %region and has been disabled.', array('%info' => $block['info'], '%region' => $block['region'])), 'warning');
        // Disabled modules are moved into the BLOCK_REGION_NONE later so no
        // need to move the block to another region.
        $block['status'] = 0;
      }
      // Set region to none if not enabled.
      if (empty($block['status'])) {
        $block['status'] = 0;
        $block['region'] = BLOCK_REGION_NONE;
      }
      // There is no point saving disabled blocks. Still, we need to save them
      // because the 'title' attribute is saved to the {blocks} table.
      if (isset($block['bid'])) {
        // If the block has a bid property, it comes from the database and
        // the record needs to be updated, so set the primary key to 'bid'
        // before passing to drupal_write_record().
        $primary_keys = array('bid');
        // Remove a block from the list of blocks to keep if it became disabled.
        unset($bids[$block['bid']]);
      }
      else {
        $primary_keys = array();
      }
      // If the block is new or differs from the original database block, save
      // it. To determine whether there was a change it is enough to examine
      // the values for the keys in the original database record as that
      // contained every database field.
      if (!$primary_keys || array_diff_assoc($original_database_blocks[$module][$delta], $block)) {
        drupal_write_record('block', $block, $primary_keys);
        // Make it possible to test this.
        $block['saved'] = TRUE;
      }
      // Add to the list of blocks we return.
      $blocks[] = $block;
    }
  }
  if ($bids) {
    // Remove disabled that are no longer defined by the code from the
    // database.
    db_delete('block')
      ->condition('bid', $bids, 'NOT IN')
      ->condition('theme', $theme)
      ->execute();
  }
  return $blocks;
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
