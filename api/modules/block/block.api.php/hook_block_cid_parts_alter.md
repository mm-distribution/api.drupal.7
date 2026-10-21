# hook_block_cid_parts_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/block/block.api.php`](_file.md), lines 385–389 · [local source](../../../../source/modules/block/block.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php#L385-L389)
- **Module/theme:** block
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_block_cid_parts_alter(&$cid_parts, $block)
```

## Documentation

```text
Act on block cache ID (cid) parts before the cid is generated.

This hook allows you to add, remove or modify the custom keys used to
generate a block cache ID (by default, these keys are set to the block
module and delta). These keys will be combined with the standard ones
provided by drupal_render_cid_parts() to generate the final block cache ID.

To change the cache granularity used by drupal_render_cid_parts(), this hook
cannot be used; instead, set the 'cache' key in the block's definition in
hook_block_info().

@params $cid_parts
  An array of elements used to build the cid.
@param $block
  The block object being acted on.

@see _block_get_cache_id()
```

## Code

```php
function hook_block_cid_parts_alter(&$cid_parts, $block) {
  global $user;
  // This example shows how to cache a block based on the user's timezone.
  $cid_parts[] = $user->timezone;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_block_cid_parts_alter()".

_None found._

---
_Drupal 7.103 · [modules/block/block.api.php](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
