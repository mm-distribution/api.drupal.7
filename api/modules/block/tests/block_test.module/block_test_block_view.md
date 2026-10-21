# block_test_block_view()

- **Type:** Function
- **File:** [`modules/block/tests/block_test.module`](_file.md), lines 42–44 · [local source](../../../../../source/modules/block/tests/block_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/tests/block_test.module#L42-L44)
- **Module/theme:** block_test
- **Implements:** [hook_block_view()](../../block.api.php/hook_block_view.md)

## Signature

```php
function block_test_block_view($delta = 0)
```

## Documentation

```text
Implements hook_block_view().
```

## Code

```php
function block_test_block_view($delta = 0) {
  return array('content' => variable_get('block_test_content', ''));
}
```

---
_Drupal 7.103 · [modules/block/tests/block_test.module](https://github.com/drupal/drupal/blob/7.103/modules/block/tests/block_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
