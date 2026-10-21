# form_test_select()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1196–1292 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1196-L1292)
- **Module/theme:** batch_test

## Signature

```php
function form_test_select($form, &$form_state)
```

## Documentation

```text
Builds a form to test #type 'select' validation.
```

## Code

```php
function form_test_select($form, &$form_state) {
  $base = array(
    '#type' => 'select',
    '#options' => drupal_map_assoc(array('one', 'two', 'three')),
  );

  $form['select'] = $base + array(
    '#title' => '#default_value one',
    '#default_value' => 'one',
  );
  $form['select_required'] = $base + array(
    '#title' => '#default_value one, #required',
    '#required' => TRUE,
    '#default_value' => 'one',
  );
  $form['select_optional'] = $base + array(
    '#title' => '#default_value one, not #required',
    '#required' => FALSE,
    '#default_value' => 'one',
  );
  $form['empty_value'] = $base + array(
    '#title' => '#default_value one, #required, #empty_value 0',
    '#required' => TRUE,
    '#default_value' => 'one',
    '#empty_value' => 0,
  );
  $form['empty_value_one'] = $base + array(
    '#title' => '#default_value = #empty_value, #required',
    '#required' => TRUE,
    '#default_value' => 'one',
    '#empty_value' => 'one',
  );

  $form['no_default'] = $base + array(
    '#title' => 'No #default_value, #required',
    '#required' => TRUE,
  );
  $form['no_default_optional'] = $base + array(
    '#title' => 'No #default_value, not #required',
    '#required' => FALSE,
    '#description' => 'Should result in "one", because it is not required and there is no #empty_value requested, so default browser behavior of preselecting first option is in effect.',
  );
  $form['no_default_optional_empty_value'] = $base + array(
    '#title' => 'No #default_value, not #required, #empty_value empty string',
    '#empty_value' => '',
    '#required' => FALSE,
    '#description' => 'Should result in an empty string (due to #empty_value), because it is optional.',
  );

  $form['no_default_empty_option'] = $base + array(
    '#title' => 'No #default_value, #required, #empty_option',
    '#required' => TRUE,
    '#empty_option' => '- Choose -',
  );
  $form['no_default_empty_option_optional'] = $base + array(
    '#title' => 'No #default_value, not #required, #empty_option',
    '#empty_option' => '- Dismiss -',
    '#description' => 'Should result in an empty string (default of #empty_value), because it is optional.',
  );

  $form['no_default_empty_value'] = $base + array(
    '#title' => 'No #default_value, #required, #empty_value 0',
    '#required' => TRUE,
    '#empty_value' => 0,
    '#description' => 'Should never result in 0.',
  );
  $form['no_default_empty_value_one'] = $base + array(
    '#title' => 'No #default_value, #required, #empty_value one',
    '#required' => TRUE,
    '#empty_value' => 'one',
    '#description' => 'A mistakenly assigned #empty_value contained in #options should not be valid.',
  );
  $form['no_default_empty_value_optional'] = $base + array(
    '#title' => 'No #default_value, not #required, #empty_value 0',
    '#required' => FALSE,
    '#empty_value' => 0,
    '#description' => 'Should result in 0, because it is optional.',
  );

  $form['multiple'] = $base + array(
    '#title' => '#multiple, #default_value two',
    '#default_value' => array('two'),
    '#multiple' => TRUE,
  );
  $form['multiple_no_default'] = $base + array(
    '#title' => '#multiple, no #default_value',
    '#multiple' => TRUE,
  );
  $form['multiple_no_default_required'] = $base + array(
    '#title' => '#multiple, #required, no #default_value',
    '#required' => TRUE,
    '#multiple' => TRUE,
  );

  $form['submit'] = array('#type' => 'submit', '#value' => 'Submit');
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
