# FormsElementsTableSelectFunctionalTest::formSubmitHelper()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1162–1188 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1162-L1188)
- **Class:** [FormsElementsTableSelectFunctionalTest](../FormsElementsTableSelectFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
private function formSubmitHelper($form, $edit)
```

## Documentation

```text
Helper function for the option check test to submit a form while collecting errors.

@param $form_element
  A form element to test.
@param $edit
  An array containing post data.

@return
  An array containing the processed form, the form_state and any errors.
```

## Code

```php
  private function formSubmitHelper($form, $edit) {
    $form_id = $this->randomName();
    $form_state = form_state_defaults();

    $form['op'] = array('#type' => 'submit', '#value' => t('Submit'));

    $form_state['input'] = $edit;
    $form_state['input']['form_id'] = $form_id;

    // The form token CSRF protection should not interfere with this test,
    // so we bypass it by marking this test form as programmed.
    $form_state['programmed'] = TRUE;

    drupal_prepare_form($form_id, $form, $form_state);

    drupal_process_form($form_id, $form, $form_state);

    $errors = form_get_errors();

    // Clear errors and messages.
    drupal_get_messages();
    form_clear_error();

    // Return the processed form together with form_state and errors
    // to allow the caller lowlevel access to the form.
    return array($form, $form_state, $errors);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
