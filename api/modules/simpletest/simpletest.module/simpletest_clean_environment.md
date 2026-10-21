# simpletest_clean_environment()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 546–560 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L546-L560)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_clean_environment()
```

## Documentation

```text
Remove all temporary database tables and directories.
```

## Code

```php
function simpletest_clean_environment() {
  simpletest_clean_database();
  simpletest_clean_temporary_directories();
  if (variable_get('simpletest_clear_results', TRUE)) {
    $count = simpletest_clean_results_table();
    drupal_set_message(format_plural($count, 'Removed 1 test result.', 'Removed @count test results.'));
  }
  else {
    drupal_set_message(t('Clear results is disabled and the test results table will not be cleared.'), 'warning');
  }

  // Detect test classes that have been added, renamed or deleted.
  registry_rebuild();
  cache_clear_all('simpletest', 'cache');
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
