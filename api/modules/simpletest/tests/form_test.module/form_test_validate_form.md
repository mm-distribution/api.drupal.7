# form_test_validate_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 320–337 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L320-L337)
- **Module/theme:** batch_test

## Signature

```php
function form_test_validate_form($form, &$form_state)
```

## Documentation

```text
Form builder for testing drupal_validate_form().

Serves for testing form processing and alterations by form validation
handlers, especially for the case of a validation error:
- form_set_value() should be able to alter submitted values in
  $form_state['values'] without affecting the form element.
- #element_validate handlers should be able to alter the $element in the form
  structure and the alterations should be contained in the rebuilt form.
- #validate handlers should be able to alter the $form and the alterations
  should be contained in the rebuilt form.
```

## Code

```php
function form_test_validate_form($form, &$form_state) {
  $form['name'] = array(
    '#type' => 'textfield',
    '#title' => 'Name',
    '#default_value' => '',
    '#element_validate' => array('form_test_element_validate_name'),
  );
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => 'Save',
  );

  // To simplify this test, enable form caching and use form storage to
  // remember our alteration.
  $form_state['cache'] = TRUE;

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
