# form_test_limit_validation_errors_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 488–546 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L488-L546)
- **Module/theme:** batch_test

## Signature

```php
function form_test_limit_validation_errors_form($form, &$form_state)
```

## Documentation

```text
Builds a simple form with a button triggering partial validation.
```

## Code

```php
function form_test_limit_validation_errors_form($form, &$form_state) {
  $form['title'] = array(
    '#type' => 'textfield',
    '#title' => 'Title',
    '#required' => TRUE,
  );

  $form['test'] = array(
    '#title' => 'Test',
    '#type' => 'textfield',
    '#element_validate' => array('form_test_limit_validation_errors_element_validate_test'),
  );
  $form['test_numeric_index'] = array(
    '#tree' => TRUE,
  );
  $form['test_numeric_index'][0] = array(
    '#title' => 'Test (numeric index)',
    '#type' => 'textfield',
    '#element_validate' => array('form_test_limit_validation_errors_element_validate_test'),
  );

  $form['test_substring'] = array(
    '#tree' => TRUE,
  );
  $form['test_substring']['foo'] = array(
    '#title' => 'Test (substring) foo',
    '#type' => 'textfield',
    '#element_validate' => array('form_test_limit_validation_errors_element_validate_test'),
  );
  $form['test_substring']['foobar'] = array(
    '#title' => 'Test (substring) foobar',
    '#type' => 'textfield',
    '#element_validate' => array('form_test_limit_validation_errors_element_validate_test'),
  );

  $form['actions']['partial'] = array(
    '#type' => 'submit',
    '#limit_validation_errors' => array(array('test')),
    '#submit' => array('form_test_limit_validation_errors_form_partial_submit'),
    '#value' => t('Partial validate'),
  );
  $form['actions']['partial_numeric_index'] = array(
    '#type' => 'submit',
    '#limit_validation_errors' => array(array('test_numeric_index', 0)),
    '#submit' => array('form_test_limit_validation_errors_form_partial_submit'),
    '#value' => t('Partial validate (numeric index)'),
  );
  $form['actions']['substring'] = array(
    '#type' => 'submit',
    '#limit_validation_errors' => array(array('test_substring', 'foo')),
    '#submit' => array('form_test_limit_validation_errors_form_partial_submit'),
    '#value' => t('Partial validate (substring)'),
  );
  $form['actions']['full'] = array(
    '#type' => 'submit',
    '#value' => t('Full validate'),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
