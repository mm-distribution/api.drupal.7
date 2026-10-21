# _simpletest_batch_finished()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 211–229 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L211-L229)
- **Module/theme:** simpletest

## Signature

```php
function _simpletest_batch_finished($success, $results, $operations, $elapsed)
```

## Documentation

```text
Implements callback_batch_finished().
```

## Code

```php
function _simpletest_batch_finished($success, $results, $operations, $elapsed) {
  if ($success) {
    drupal_set_message(t('The test run finished in @elapsed.', array('@elapsed' => $elapsed)));
  }
  else {
    // Use the test_id passed as a parameter to _simpletest_batch_operation().
    $test_id = $operations[0][1][1];

    // Retrieve the last database prefix used for testing and the last test
    // class that was run from. Use the information to read the log file
    // in case any fatal errors caused the test to crash.
    list($last_prefix, $last_test_class) = simpletest_last_test_get($test_id);
    simpletest_log_read($test_id, $last_prefix, $last_test_class);

    drupal_set_message(t('The test run did not successfully finish.'), 'error');
    drupal_set_message(t('Use the <em>Clean environment</em> button to clean-up temporary files and tables.'), 'warning');
  }
  module_invoke_all('test_group_finished');
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
