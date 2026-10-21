# _block_render_blocks()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 858–947 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L858-L947)
- **Module/theme:** block

## Signature

```php
function _block_render_blocks($region_blocks)
```

## Documentation

```text
Render the content and subject for a set of blocks.

@param $region_blocks
  An array of block objects such as returned for one region by
  _block_load_blocks().

@return
  An array of visible blocks as expected by drupal_render().
```

## Code

```php
function _block_render_blocks($region_blocks) {
  $cacheable = TRUE;

  // We preserve the submission of forms in blocks, by fetching from cache only
  // if the request method is 'GET' (or 'HEAD').
  if ($_SERVER['REQUEST_METHOD'] != 'GET' && $_SERVER['REQUEST_METHOD'] != 'HEAD') {
    $cacheable = FALSE;
  }
  // Block caching is not usually compatible with node access modules, so by
  // default it is disabled when node access modules exist. However, it can be
  // allowed by using the variable 'block_cache_bypass_node_grants'.
  elseif (!variable_get('block_cache_bypass_node_grants', FALSE) && count(module_implements('node_grants'))) {
    $cacheable = FALSE;
  }

  // Proceed to loop over all blocks in order to compute their respective cache
  // identifiers; this allows us to do one single cache_get_multiple() call
  // instead of doing one cache_get() call per block.
  $cached_blocks = array();
  $cids = array();

  if ($cacheable) {
    foreach ($region_blocks as $key => $block) {
      if (!isset($block->content)) {
        if (($cid = _block_get_cache_id($block))) {
          $cids[$key] = $cid;
        }
      }
    }

    if ($cids) {
      // We cannot pass $cids in directly because cache_get_multiple() will
      // modify it, and we need to use it later on in this function.
      $cid_values = array_values($cids);
      $cached_blocks = cache_get_multiple($cid_values, 'cache_block');
    }
  }

  foreach ($region_blocks as $key => $block) {
    // Render the block content if it has not been created already.
    if (!isset($block->content)) {
      // Erase the block from the static array - we'll put it back if it has
      // content.
      unset($region_blocks[$key]);

      $cid = empty($cids[$key]) ? NULL : $cids[$key];

      // Try fetching the block from the previously loaded cache entries.
      if (isset($cached_blocks[$cid])) {
        $array = $cached_blocks[$cid]->data;
      }
      else {
        $array = module_invoke($block->module, 'block_view', $block->delta);

        // Valid PHP function names cannot contain hyphens.
        $delta = str_replace('-', '_', $block->delta);
        // Allow modules to modify the block before it is viewed, via either
        // hook_block_view_alter() or hook_block_view_MODULE_DELTA_alter().
        drupal_alter(array('block_view', "block_view_{$block->module}_{$delta}"), $array, $block);

        if (isset($cid)) {
          cache_set($cid, $array, 'cache_block', CACHE_TEMPORARY);
        }
      }

      if (isset($array) && is_array($array)) {
        foreach ($array as $k => $v) {
          $block->$k = $v;
        }
      }
      if (isset($block->content) && $block->content) {
        // Normalize to the drupal_render() structure.
        if (is_string($block->content)) {
          $block->content = array('#markup' => $block->content);
        }
        // Override default block title if a custom display title is present.
        if ($block->title) {
          // Check plain here to allow module generated titles to keep any
          // markup.
          $block->subject = $block->title == '<none>' ? '' : check_plain($block->title);
        }
        if (!isset($block->subject)) {
          $block->subject = '';
        }
        $region_blocks["{$block->module}_{$block->delta}"] = $block;
      }
    }
  }
  return $region_blocks;
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
