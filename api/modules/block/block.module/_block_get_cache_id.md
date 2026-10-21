# _block_get_cache_id()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 966–982 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L966-L982)
- **Module/theme:** block

## Signature

```php
function _block_get_cache_id($block)
```

## Documentation

```text
Assemble the cache_id to use for a given block.

The cache_id string reflects the viewing context for the current block
instance, obtained by concatenating the relevant context information
(user, page, ...) according to the block's cache settings (BLOCK_CACHE_*
constants). Two block instances can use the same cached content when
they share the same cache_id.

Theme and language contexts are automatically differentiated.

@param $block
  The block to get the cache_id from.

@return
  The string used as cache_id for the block.
```

## Code

```php
function _block_get_cache_id($block) {
  global $user;

  // User 1 being out of the regular 'roles define permissions' schema,
  // it brings too many chances of having unwanted output get in the cache
  // and later be served to other users. We therefore exclude user 1 from
  // block caching.
  if (variable_get('block_cache', FALSE) && !in_array($block->cache, array(DRUPAL_NO_CACHE, DRUPAL_CACHE_CUSTOM)) && $user->uid != 1) {
    // Start with common sub-patterns: block identification, theme, language.
    $cid_parts[] = $block->module;
    $cid_parts[] = $block->delta;
    drupal_alter('block_cid_parts', $cid_parts, $block);
    $cid_parts = array_merge($cid_parts, drupal_render_cid_parts($block->cache));

    return implode(':', $cid_parts);
  }
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
