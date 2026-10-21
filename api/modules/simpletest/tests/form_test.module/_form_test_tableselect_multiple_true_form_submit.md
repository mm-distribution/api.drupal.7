# _form_test_tableselect_multiple_true_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 651–656 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L651-L656)
- **Module/theme:** batch_test

## Signature

```php
function _form_test_tableselect_multiple_true_form_submit($form, &$form_state)
```

## Documentation

```text
Process the tableselect #multiple = TRUE submitted values.
```

## Code

```php
function _form_test_tableselect_multiple_true_form_submit($form, &$form_state) {
  $selected = $form_state['values']['tableselect'];
  foreach ($selected as $key => $value) {
    drupal_set_message(t('Submitted: @key = @value', array('@key' => $key, '@value' => $value)));
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
