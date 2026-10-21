# taxonomy_test_block_info()

- **Type:** Function
- **File:** [`modules/simpletest/tests/taxonomy_test.module`](_file.md), lines 146–151 · [local source](../../../../../source/modules/simpletest/tests/taxonomy_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module#L146-L151)
- **Module/theme:** batch_test
- **Implements:** [hook_block_info()](../../../block/block.api.php/hook_block_info.md)

## Signature

```php
function taxonomy_test_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function taxonomy_test_block_info() {
  $blocks['test_block_form'] = array(
    'info' => t('Test block with form'),
  );
  return $blocks;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/taxonomy_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
