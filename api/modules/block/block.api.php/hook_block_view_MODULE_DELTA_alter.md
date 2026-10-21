# hook_block_view_MODULE_DELTA_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/block/block.api.php`](_file.md), lines 309–317 · [local source](../../../../source/modules/block/block.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php#L309-L317)
- **Module/theme:** block
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_block_view_MODULE_DELTA_alter(&$data, $block)
```

## Documentation

```text
Perform alterations to a specific block.

Modules can implement hook_block_view_MODULE_DELTA_alter() to modify a
specific block, rather than implementing hook_block_view_alter().

@param $data
  The data as returned from the hook_block_view() implementation of the
  module that defined the block. This could be an empty array or NULL value
  (if the block is empty) or an array containing:
  - subject: The localized title of the block.
  - content: Either a string or a renderable array representing the content
    of the block. You should check that the content is an array before trying
    to modify parts of the renderable structure.
@param $block
  The block object, as loaded from the database, having the main properties:
  - module: The name of the module that defined the block.
  - delta: The unique identifier for the block within that module, as defined
    in hook_block_info().

@see hook_block_view_alter()
@see hook_block_view()
```

## Code

```php
function hook_block_view_MODULE_DELTA_alter(&$data, $block) {
  // This code will only run for a specific block. For example, if MODULE_DELTA
  // in the function definition above is set to "mymodule_somedelta", the code
  // will only run on the "somedelta" block provided by the "mymodule" module.

  // Change the title of the "somedelta" block provided by the "mymodule"
  // module.
  $data['subject'] = t('New title of the block');
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_block_view_MODULE_DELTA_alter()".

- [block_test_block_view_block_test_test_hyphen_alter()](../tests/block_test.module/block_test_block_view_block_test_test_hyphen_alter.md) — `modules/block/tests/block_test.module`
- [block_test_block_view_block_test_test_underscore_alter()](../tests/block_test.module/block_test_block_view_block_test_test_underscore_alter.md) — `modules/block/tests/block_test.module`

---
_Drupal 7.103 · [modules/block/block.api.php](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
