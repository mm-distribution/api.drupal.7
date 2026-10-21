# simpletest_clean_results_table()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 619–642 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L619-L642)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_clean_results_table($test_id = NULL)
```

## Documentation

```text
Clear the test result tables.

@param $test_id
  Test ID to remove results for, or NULL to remove all results.
@return
  The number of results removed.
```

## Code

```php
function simpletest_clean_results_table($test_id = NULL) {
  if (variable_get('simpletest_clear_results', TRUE)) {
    if ($test_id) {
      $count = db_query('SELECT COUNT(test_id) FROM {simpletest_test_id} WHERE test_id = :test_id', array(':test_id' => $test_id))->fetchField();

      db_delete('simpletest')
        ->condition('test_id', $test_id)
        ->execute();
      db_delete('simpletest_test_id')
        ->condition('test_id', $test_id)
        ->execute();
    }
    else {
      $count = db_query('SELECT COUNT(test_id) FROM {simpletest_test_id}')->fetchField();

      // Clear test results.
      db_delete('simpletest')->execute();
      db_delete('simpletest_test_id')->execute();
    }

    return $count;
  }
  return 0;
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
