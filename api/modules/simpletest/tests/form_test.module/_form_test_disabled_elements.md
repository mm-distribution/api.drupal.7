# _form_test_disabled_elements()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1364–1533 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1364-L1533)
- **Module/theme:** batch_test

## Signature

```php
function _form_test_disabled_elements($form, &$form_state)
```

## Documentation

```text
Build a form to test disabled elements.
```

## Code

```php
function _form_test_disabled_elements($form, &$form_state) {
  // Elements that take a simple default value.
  foreach (array('textfield', 'textarea', 'hidden') as $type) {
    $form[$type] = array(
      '#type' => $type,
      '#title' => $type,
      '#default_value' => $type,
      '#test_hijack_value' => 'HIJACK',
      '#disabled' => TRUE,
    );
  }

  // Multiple values option elements.
  foreach (array('checkboxes', 'select') as $type) {
    $form[$type . '_multiple'] = array(
      '#type' => $type,
      '#title' => $type . ' (multiple)',
      '#options' => array(
        'test_1' => 'Test 1',
        'test_2' => 'Test 2',
      ),
      '#multiple' => TRUE,
      '#default_value' => array('test_2' => 'test_2'),
      // The keys of #test_hijack_value need to match the #name of the control.
      // @see FormsTestCase::testDisabledElements()
      '#test_hijack_value' => $type == 'select' ? array('' => 'test_1') : array('test_1' => 'test_1'),
      '#disabled' => TRUE,
    );
  }

  // Single values option elements.
  foreach (array('radios', 'select') as $type) {
    $form[$type . '_single'] = array(
      '#type' => $type,
      '#title' => $type . ' (single)',
      '#options' => array(
        'test_1' => 'Test 1',
        'test_2' => 'Test 2',
      ),
      '#multiple' => FALSE,
      '#default_value' => 'test_2',
      '#test_hijack_value' => 'test_1',
      '#disabled' => TRUE,
    );
  }

  // Checkbox and radio.
  foreach (array('checkbox', 'radio') as $type) {
    $form[$type . '_unchecked'] = array(
      '#type' => $type,
      '#title' => $type . ' (unchecked)',
      '#return_value' => 1,
      '#default_value' => 0,
      '#test_hijack_value' => 1,
      '#disabled' => TRUE,
    );
    $form[$type . '_checked'] = array(
      '#type' => $type,
      '#title' => $type . ' (checked)',
      '#return_value' => 1,
      '#default_value' => 1,
      '#test_hijack_value' => NULL,
      '#disabled' => TRUE,
    );
  }

  // Weight.
  $form['weight'] = array(
    '#type' => 'weight',
    '#title' => 'weight',
    '#default_value' => 10,
    '#test_hijack_value' => 5,
    '#disabled' => TRUE,
  );

  // Date.
  $form['date'] = array(
    '#type' => 'date',
    '#title' => 'date',
    '#disabled' => TRUE,
    '#default_value' => array(
      'day' => 19,
      'month' => 11,
      'year' => 1978,
    ),
    '#test_hijack_value' => array(
      'day' => 20,
      'month' => 12,
      'year' => 1979,
    ),
  );

  // The #disabled state should propagate to children.
  $form['disabled_container'] = array(
    '#disabled' => TRUE,
  );
  foreach (array('textfield', 'textarea', 'hidden') as $type) {
    $form['disabled_container']['disabled_container_' . $type] = array(
      '#type' => $type,
      '#title' => $type,
      '#default_value' => $type,
      '#test_hijack_value' => 'HIJACK',
    );
  }

  // Text format.
  $form['text_format'] = array(
    '#type' => 'text_format',
    '#title' => 'Text format',
    '#disabled' => TRUE,
    '#default_value' => 'Text value',
    '#format' => 'plain_text',
    '#expected_value' => array(
      'value' => 'Text value',
      'format' => 'plain_text',
    ),
    '#test_hijack_value' => array(
      'value' => 'HIJACK',
      'format' => 'filtered_html',
    ),
  );

  // Password fields.
  $form['password'] = array(
    '#type' => 'password',
    '#title' => 'Password',
    '#disabled' => TRUE,
  );
  $form['password_confirm'] = array(
    '#type' => 'password_confirm',
    '#title' => 'Password confirm',
    '#disabled' => TRUE,
  );

  // Files.
  $form['file'] = array(
    '#type' => 'file',
    '#title' => 'File',
    '#disabled' => TRUE,
  );
  $form['managed_file'] = array(
    '#type' => 'managed_file',
    '#title' => 'Managed file',
    '#disabled' => TRUE,
  );

  // Buttons.
  $form['image_button'] = array(
    '#type' => 'image_button',
    '#value' => 'Image button',
    '#disabled' => TRUE,
  );
  $form['button'] = array(
    '#type' => 'button',
    '#value' => 'Button',
    '#disabled' => TRUE,
  );
  $form['submit_disabled'] = array(
    '#type' => 'submit',
    '#value' => 'Submit',
    '#disabled' => TRUE,
  );

  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Submit'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
