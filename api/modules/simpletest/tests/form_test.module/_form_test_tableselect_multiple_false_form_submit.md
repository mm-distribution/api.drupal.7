# _form_test_tableselect_multiple_false_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 668–670 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L668-L670)
- **Module/theme:** batch_test

## Signature

```php
function _form_test_tableselect_multiple_false_form_submit($form, &$form_state)
```

## Documentation

```text
Process the tableselect #multiple = FALSE submitted values.
```

## Code

```php
function _form_test_tableselect_multiple_false_form_submit($form, &$form_state) {
  drupal_set_message(t('Submitted: @value', array('@value' => $form_state['values']['tableselect'])));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
