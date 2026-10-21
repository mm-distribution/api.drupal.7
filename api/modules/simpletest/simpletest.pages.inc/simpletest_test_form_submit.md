# simpletest_test_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.pages.inc`](_file.md), lines 183–201 · [local source](../../../../source/modules/simpletest/simpletest.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc#L183-L201)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_test_form_submit($form, &$form_state)
```

## Documentation

```text
Run selected tests.
```

## Code

```php
function simpletest_test_form_submit($form, &$form_state) {
  simpletest_classloader_register();
  // Get list of tests.
  $tests_list = array();
  foreach ($form_state['values'] as $class_name => $value) {
    // Since class_exists() will likely trigger an autoload lookup,
    // we do the fast check first.
    if ($value === 1 && class_exists($class_name)) {
      $tests_list[] = $class_name;
    }
  }
  if (count($tests_list) > 0 ) {
    $test_id = simpletest_run_tests($tests_list, 'drupal');
    $form_state['redirect'] = 'admin/config/development/testing/results/' . $test_id;
  }
  else {
    drupal_set_message(t('No test(s) selected.'), 'error');
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
