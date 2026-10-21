# form_test_validate_required_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 395–435 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L395-L435)
- **Module/theme:** batch_test

## Signature

```php
function form_test_validate_required_form($form, &$form_state)
```

## Documentation

```text
Form constructor to test the #required property.
```

## Code

```php
function form_test_validate_required_form($form, &$form_state) {
  $options = drupal_map_assoc(array('foo', 'bar'));

  $form['textfield'] = array(
    '#type' => 'textfield',
    '#title' => 'Textfield',
    '#required' => TRUE,
  );
  $form['checkboxes'] = array(
    '#type' => 'checkboxes',
    '#title' => 'Checkboxes',
    '#options' => $options,
    '#required' => TRUE,
  );
  $form['select'] = array(
    '#type' => 'select',
    '#title' => 'Select',
    '#options' => $options,
    '#required' => TRUE,
  );
  $form['radios'] = array(
    '#type' => 'radios',
    '#title' => 'Radios',
    '#options' => $options,
    '#required' => TRUE,
  );
  $form['radios_optional'] = array(
    '#type' => 'radios',
    '#title' => 'Radios (optional)',
    '#options' => $options,
  );
  $form['radios_optional_default_value_false'] = array(
    '#type' => 'radios',
    '#title' => 'Radios (optional, with a default value of FALSE)',
    '#options' => $options,
    '#default_value' => FALSE,
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => 'Submit');
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
