# block_form_form_test_alter_form_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 281–283 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L281-L283)
- **Module/theme:** batch_test
- **Implements:** [hook_form_FORM_ID_alter()](../../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function block_form_form_test_alter_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter() on behalf of block.module.
```

## Code

```php
function block_form_form_test_alter_form_alter(&$form, &$form_state) {
  drupal_set_message('block_form_form_test_alter_form_alter() executed.');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
