# block_test_block_view_block_test_test_hyphen_alter()

- **Type:** Function
- **File:** [`modules/block/tests/block_test.module`](_file.md), lines 56–58 · [local source](../../../../../source/modules/block/tests/block_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/tests/block_test.module#L56-L58)
- **Module/theme:** block_test
- **Implements:** [hook_block_view_MODULE_DELTA_alter()](../../block.api.php/hook_block_view_MODULE_DELTA_alter.md)

## Signature

```php
function block_test_block_view_block_test_test_hyphen_alter(&$data, $block)
```

## Documentation

```text
Implements hook_block_view_MODULE_DELTA_alter().
```

## Code

```php
function block_test_block_view_block_test_test_hyphen_alter(&$data, $block) {
  $data['content'] = 'hook_block_view_MODULE_DELTA_alter';
}
```

---
_Drupal 7.103 · [modules/block/tests/block_test.module](https://github.com/drupal/drupal/blob/7.103/modules/block/tests/block_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
