# system_test_drupal_get_filename_with_schema_rebuild()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 563–578 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L563-L578)
- **Module/theme:** batch_test

## Signature

```php
function system_test_drupal_get_filename_with_schema_rebuild()
```

## Documentation

```text
Page callback to run drupal_get_filename() and do a schema rebuild.
```

## Code

```php
function system_test_drupal_get_filename_with_schema_rebuild() {
  // Prevent SimpleTest from failing as a result of the expected PHP warnings
  // this function causes.
  define('SIMPLETEST_COLLECT_ERRORS', FALSE);

  // Record the original database tables from drupal_get_schema().
  variable_set('system_test_drupal_get_filename_with_schema_rebuild_original_tables', array_keys(drupal_get_schema(NULL, TRUE)));

  // Trigger system_test_schema() and system_test_watchdog() to perform an
  // attempted recursive rebuild when drupal_get_schema() is called. See
  // BootstrapGetFilenameWebTestCase::testRecursiveRebuilds().
  variable_set('system_test_drupal_get_filename_attempt_recursive_rebuild', TRUE);
  drupal_get_schema(NULL, TRUE);

  return '';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
