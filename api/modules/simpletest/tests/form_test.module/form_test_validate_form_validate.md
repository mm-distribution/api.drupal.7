# form_test_validate_form_validate()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 378–390 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L378-L390)
- **Module/theme:** batch_test

## Signature

```php
function form_test_validate_form_validate(&$form, &$form_state)
```

## Documentation

```text
Form validation handler for form_test_validate_form().
```

## Code

```php
function form_test_validate_form_validate(&$form, &$form_state) {
  if ($form_state['values']['name'] == 'validate') {
    // Alter the form element.
    $form['name']['#value'] = '#value changed by #validate';
    // Alter the submitted value in $form_state.
    form_set_value($form['name'], 'value changed by form_set_value() in #validate', $form_state);
    // Output the element's value from $form_state.
    drupal_set_message(t('@label value: @value', array('@label' => $form['name']['#title'], '@value' => $form_state['values']['name'])));

    // Trigger a form validation error to see our changes.
    form_set_error('');
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
