# form_test_form_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 288–292 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L288-L292)
- **Module/theme:** batch_test
- **Implements:** [hook_form_alter()](../../../system/system.api.php/hook_form_alter.md)

## Signature

```php
function form_test_form_alter(&$form, &$form_state, $form_id)
```

## Documentation

```text
Implements hook_form_alter().
```

## Code

```php
function form_test_form_alter(&$form, &$form_state, $form_id) {
  if ($form_id == 'form_test_alter_form') {
    drupal_set_message('form_test_form_alter() executed.');
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
