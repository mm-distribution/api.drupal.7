# Block Caching

- **Topic id:** `block_caching`
- **Defined in:** [`includes/common.inc`](../includes/common.inc/_file.md), line 94 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L94)

## Documentation

```text
@defgroup block_caching Block Caching
@{
Constants that define each block's caching state.

Modules specify how their blocks can be cached in their hook_block_info()
implementations. Caching can be turned off (DRUPAL_NO_CACHE), managed by the
module declaring the block (DRUPAL_CACHE_CUSTOM), or managed by the core
Block module. If the Block module is managing the cache, you can specify that
the block is the same for every page and user (DRUPAL_CACHE_GLOBAL), or that
it can change depending on the page (DRUPAL_CACHE_PER_PAGE) or by user
(DRUPAL_CACHE_PER_ROLE or DRUPAL_CACHE_PER_USER). Page and user settings can
be combined with a bitwise-binary or operator; for example,
DRUPAL_CACHE_PER_ROLE | DRUPAL_CACHE_PER_PAGE means that the block can change
depending on the user role or page it is on.

The block cache is cleared in cache_clear_all(), and uses the same clearing
policy than page cache (node, comment, user, taxonomy added or updated...).
Blocks requiring more fine-grained clearing might consider disabling the
built-in block cache (DRUPAL_NO_CACHE) and roll their own.

Note that user 1 is excluded from block caching.
```

## Members (derived, 6)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [DRUPAL_CACHE_CUSTOM](../includes/common.inc/_file.md#drupal_cache_custom) (constant) — The block is handling its own caching in its hook_block_view().
- [DRUPAL_CACHE_GLOBAL](../includes/common.inc/_file.md#drupal_cache_global) (constant) — The block or element is the same for every user and page that it is visible.
- [DRUPAL_CACHE_PER_PAGE](../includes/common.inc/_file.md#drupal_cache_per_page) (constant) — The block or element can change depending on the page being viewed.
- [DRUPAL_CACHE_PER_ROLE](../includes/common.inc/_file.md#drupal_cache_per_role) (constant) — The block or element can change depending on the user's roles.
- [DRUPAL_CACHE_PER_USER](../includes/common.inc/_file.md#drupal_cache_per_user) (constant) — The block or element can change depending on the user.
- [DRUPAL_NO_CACHE](../includes/common.inc/_file.md#drupal_no_cache) (constant) — The block should not get cached.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
