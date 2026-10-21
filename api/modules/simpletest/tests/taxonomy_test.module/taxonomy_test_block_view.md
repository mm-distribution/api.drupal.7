# taxonomy_test_block_view()

- **Type:** Function
- **File:** [`modules/simpletest/tests/taxonomy_test.module`](_file.md), lines 156–159 · [local source](../../../../../source/modules/simpletest/tests/taxonomy_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module#L156-L159)
- **Module/theme:** batch_test
- **Implements:** [hook_block_view()](../../../block/block.api.php/hook_block_view.md)

## Signature

```php
function taxonomy_test_block_view($delta = 0)
```

## Documentation

```text
Implements hook_block_view().
```

## Code

```php
function taxonomy_test_block_view($delta = 0) {
  $form = drupal_get_form('taxonomy_test_simple_form');
  return array('subject' => 'Simple form', 'content' => drupal_render($form));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/taxonomy_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
