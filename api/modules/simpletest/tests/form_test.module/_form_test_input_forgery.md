# _form_test_input_forgery()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1546–1562 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1546-L1562)
- **Module/theme:** batch_test

## Signature

```php
function _form_test_input_forgery($form, &$form_state)
```

## Documentation

```text
Build a form to test input forgery of enabled elements.
```

## Code

```php
function _form_test_input_forgery($form, &$form_state) {
  // For testing that a user can't submit a value not matching one of the
  // allowed options.
  $form['checkboxes'] = array(
    '#type' => 'checkboxes',
    '#options' => array(
      'one' => 'One',
      'two' => 'Two',
    ),
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
