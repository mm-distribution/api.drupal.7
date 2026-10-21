# _form_test_tableselect_multiple_false_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 661–663 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L661-L663)
- **Module/theme:** batch_test

## Signature

```php
function _form_test_tableselect_multiple_false_form($form, $form_state)
```

## Documentation

```text
Test the tableselect #multiple = FALSE functionality.
```

## Code

```php
function _form_test_tableselect_multiple_false_form($form, $form_state) {
  return _form_test_tableselect_form_builder($form, $form_state, array('#multiple' => FALSE));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
