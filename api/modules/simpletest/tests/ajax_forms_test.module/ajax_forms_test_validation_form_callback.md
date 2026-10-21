# ajax_forms_test_validation_form_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_forms_test.module`](_file.md), lines 475–479 · [local source](../../../../../source/modules/simpletest/tests/ajax_forms_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module#L475-L479)
- **Module/theme:** batch_test

## Signature

```php
function ajax_forms_test_validation_form_callback($form, $form_state)
```

## Documentation

```text
Ajax callback for the 'drivertext' element of the validation form.
```

## Code

```php
function ajax_forms_test_validation_form_callback($form, $form_state) {
  drupal_set_message("ajax_forms_test_validation_form_callback invoked");
  drupal_set_message(t("Callback: drivertext=%drivertext, spare_required_field=%spare_required_field", array('%drivertext' => $form_state['values']['drivertext'], '%spare_required_field' => $form_state['values']['spare_required_field'])));
  return '<div id="message_area">ajax_forms_test_validation_form_callback at ' . date('c') . '</div>';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_forms_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
