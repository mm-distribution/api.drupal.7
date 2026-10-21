# form_test_form_form_test_alter_form_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 297–299 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L297-L299)
- **Module/theme:** batch_test
- **Implements:** [hook_form_FORM_ID_alter()](../../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function form_test_form_form_test_alter_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function form_test_form_form_test_alter_form_alter(&$form, &$form_state) {
  drupal_set_message('form_test_form_form_test_alter_form_alter() executed.');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
