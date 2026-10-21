# block_test_block_info()

- **Type:** Function
- **File:** [`modules/block/tests/block_test.module`](_file.md), lines 19–37 · [local source](../../../../../source/modules/block/tests/block_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/tests/block_test.module#L19-L37)
- **Module/theme:** block_test
- **Implements:** [hook_block_info()](../../block.api.php/hook_block_info.md)

## Signature

```php
function block_test_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function block_test_block_info() {
  $blocks['test_cache'] = array(
    'info' => t('Test block caching'),
    'cache' => variable_get('block_test_caching', DRUPAL_CACHE_PER_ROLE),
  );

  $blocks['test_underscore'] = array(
    'info' => t('Test underscore'),
  );

  $blocks['test-hyphen'] = array(
    'info' => t('Test hyphen'),
  );

  $blocks['test_html_id'] = array(
    'info' => t('Test block html id'),
  );
  return $blocks;
}
```

---
_Drupal 7.103 · [modules/block/tests/block_test.module](https://github.com/drupal/drupal/blob/7.103/modules/block/tests/block_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
