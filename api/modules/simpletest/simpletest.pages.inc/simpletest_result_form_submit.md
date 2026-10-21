# simpletest_result_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.pages.inc`](_file.md), lines 342–368 · [local source](../../../../source/modules/simpletest/simpletest.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc#L342-L368)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_result_form_submit($form, &$form_state)
```

## Documentation

```text
Re-run the tests that match the filter.
```

## Code

```php
function simpletest_result_form_submit($form, &$form_state) {
  $pass = $form_state['values']['filter_pass'] ? explode(',', $form_state['values']['filter_pass']) : array();
  $fail = $form_state['values']['filter_fail'] ? explode(',', $form_state['values']['filter_fail']) : array();

  if ($form_state['values']['filter'] == 'all') {
    $classes = array_merge($pass, $fail);
  }
  elseif ($form_state['values']['filter'] == 'pass') {
    $classes = $pass;
  }
  else {
    $classes = $fail;
  }

  if (!$classes) {
    $form_state['redirect'] = 'admin/config/development/testing';
    return;
  }

  $form_state_execute = array('values' => array());
  foreach ($classes as $class) {
    $form_state_execute['values'][$class] = 1;
  }

  simpletest_test_form_submit(array(), $form_state_execute);
  $form_state['redirect'] = $form_state_execute['redirect'];
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
