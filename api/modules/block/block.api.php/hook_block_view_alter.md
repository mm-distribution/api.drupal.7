# hook_block_view_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/block/block.api.php`](_file.md), lines 274–284 · [local source](../../../../source/modules/block/block.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php#L274-L284)
- **Module/theme:** block
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_block_view_alter(&$data, $block)
```

## Documentation

```text
Perform alterations to the content of a block.

This hook allows you to modify any data returned by hook_block_view().

Note that instead of hook_block_view_alter(), which is called for all
blocks, you can also use hook_block_view_MODULE_DELTA_alter() to alter a
specific block.

@param $data
  The data as returned from the hook_block_view() implementation of the
  module that defined the block. This could be an empty array or NULL value
  (if the block is empty) or an array containing:
  - subject: The default localized title of the block.
  - content: Either a string or a renderable array representing the content
    of the block. You should check that the content is an array before trying
    to modify parts of the renderable structure.
@param $block
  The block object, as loaded from the database, having the main properties:
  - module: The name of the module that defined the block.
  - delta: The unique identifier for the block within that module, as defined
    in hook_block_info().

@see hook_block_view_MODULE_DELTA_alter()
@see hook_block_view()
```

## Code

```php
function hook_block_view_alter(&$data, $block) {
  // Remove the contextual links on all blocks that provide them.
  if (is_array($data['content']) && isset($data['content']['#contextual_links'])) {
    unset($data['content']['#contextual_links']);
  }
  // Add a theme wrapper function defined by the current module to all blocks
  // provided by the "somemodule" module.
  if (is_array($data['content']) && $block->module == 'somemodule') {
    $data['content']['#theme_wrappers'][] = 'mymodule_special_block';
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_block_view_alter()".

- [menu_block_view_alter()](../../menu/menu.module/menu_block_view_alter.md) — `modules/menu/menu.module`

---
_Drupal 7.103 · [modules/block/block.api.php](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
