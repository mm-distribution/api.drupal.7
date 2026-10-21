# form_test_form_rebuild_preserve_values_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1575–1631 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1575-L1631)
- **Module/theme:** batch_test

## Signature

```php
function form_test_form_rebuild_preserve_values_form($form, &$form_state)
```

## Documentation

```text
Form builder for testing preservation of values during a rebuild.
```

## Code

```php
function form_test_form_rebuild_preserve_values_form($form, &$form_state) {
  // Start the form with two checkboxes, to test different defaults, and a
  // textfield, to test more than one element type.
  $form = array(
    'checkbox_1_default_off' => array(
      '#type' => 'checkbox',
      '#title' => t('This checkbox defaults to unchecked.'),
      '#default_value' => FALSE,
    ),
    'checkbox_1_default_on' => array(
      '#type' => 'checkbox',
      '#title' => t('This checkbox defaults to checked.'),
      '#default_value' => TRUE,
    ),
    'text_1' => array(
      '#type' => 'textfield',
      '#title' => t('This textfield has a non-empty default value.'),
      '#default_value' => 'DEFAULT 1',
    ),
  );
  // Provide an 'add more' button that rebuilds the form with an additional two
  // checkboxes and a textfield. The test is to make sure that the rebuild
  // triggered by this button preserves the user input values for the initial
  // elements and initializes the new elements with the correct default values.
  if (empty($form_state['storage']['add_more'])) {
    $form['add_more'] = array(
      '#type' => 'submit',
      '#value' => 'Add more',
      '#submit' => array('form_test_form_rebuild_preserve_values_form_add_more'),
    );
  }
  else {
    $form += array(
      'checkbox_2_default_off' => array(
        '#type' => 'checkbox',
        '#title' => t('This checkbox defaults to unchecked.'),
        '#default_value' => FALSE,
      ),
      'checkbox_2_default_on' => array(
        '#type' => 'checkbox',
        '#title' => t('This checkbox defaults to checked.'),
        '#default_value' => TRUE,
      ),
      'text_2' => array(
        '#type' => 'textfield',
        '#title' => t('This textfield has a non-empty default value.'),
        '#default_value' => 'DEFAULT 2',
      ),
    );
  }
  // A submit button that finishes the form workflow (does not rebuild).
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => 'Submit',
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
