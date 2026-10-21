# block_test_block_info_alter()

- **Type:** Function
- **File:** [`modules/block/tests/block_test.module`](_file.md), lines 63–67 · [local source](../../../../../source/modules/block/tests/block_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/tests/block_test.module#L63-L67)
- **Module/theme:** block_test
- **Implements:** [hook_block_info_alter()](../../block.api.php/hook_block_info_alter.md)

## Signature

```php
function block_test_block_info_alter(&$blocks)
```

## Documentation

```text
Implements hook_block_info_alter().
```

## Code

```php
function block_test_block_info_alter(&$blocks) {
  if (variable_get('block_test_info_alter')) {
    $blocks['block_test']['test_html_id']['weight'] = 10000;
  }
}
```

---
_Drupal 7.103 · [modules/block/tests/block_test.module](https://github.com/drupal/drupal/blob/7.103/modules/block/tests/block_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
