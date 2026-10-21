# ajax_forms_test_validation_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_forms_test.module`](_file.md), lines 437–464 · [local source](../../../../../source/modules/simpletest/tests/ajax_forms_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module#L437-L464)
- **Module/theme:** batch_test

## Signature

```php
function ajax_forms_test_validation_form($form, &$form_state)
```

## Documentation

```text
This form and its related submit and callback functions demonstrate
not validating another form element when a single Ajax element is triggered.

The "drivertext" element is an Ajax-enabled textfield, free-form.
The "required_field" element is a textfield marked required.

The correct behavior is that the Ajax-enabled drivertext element should
be able to trigger without causing validation of the "required_field".
```

## Code

```php
function ajax_forms_test_validation_form($form, &$form_state) {

  $form['drivertext'] = array(
    '#title' => t('AJAX-enabled textfield.'),
    '#description' => t("When this one AJAX-triggers and the spare required field is empty, you should not get an error."),
    '#type' => 'textfield',
    '#default_value' => !empty($form_state['values']['drivertext']) ? $form_state['values']['drivertext'] : "",
    '#ajax' => array(
      'callback' => 'ajax_forms_test_validation_form_callback',
      'wrapper' => 'message_area',
      'method' => 'replace',
    ),
    '#suffix' => '<div id="message_area"></div>',
  );

  $form['spare_required_field'] = array(
    '#title' => t("Spare Required Field"),
    '#type' => 'textfield',
    '#required' => TRUE,
  );

  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Submit'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_forms_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
