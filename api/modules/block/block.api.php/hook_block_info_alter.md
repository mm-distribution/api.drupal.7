# hook_block_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/block/block.api.php`](_file.md), lines 136–139 · [local source](../../../../source/modules/block/block.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php#L136-L139)
- **Module/theme:** block
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_block_info_alter(&$blocks, $theme, $code_blocks)
```

## Documentation

```text
Change block definition before saving to the database.

@param $blocks
  A multidimensional array of blocks keyed by the defining module and delta;
  the values are blocks returned by hook_block_info(). This hook is fired
  after the blocks are collected from hook_block_info() and the database,
  right before saving back to the database.
@param $theme
  The theme these blocks belong to.
@param $code_blocks
  The blocks as defined in hook_block_info() before being overwritten by the
  database data.

@see hook_block_info()
```

## Code

```php
function hook_block_info_alter(&$blocks, $theme, $code_blocks) {
  // Disable the login block.
  $blocks['user']['login']['status'] = 0;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_block_info_alter()".

- [block_test_block_info_alter()](../tests/block_test.module/block_test_block_info_alter.md) — `modules/block/tests/block_test.module`
- [dashboard_block_info_alter()](../../dashboard/dashboard.module/dashboard_block_info_alter.md) — `modules/dashboard/dashboard.module`

---
_Drupal 7.103 · [modules/block/block.api.php](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
