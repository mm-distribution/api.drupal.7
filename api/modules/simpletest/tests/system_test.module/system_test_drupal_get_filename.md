# system_test_drupal_get_filename()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 548–558 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L548-L558)
- **Module/theme:** batch_test

## Signature

```php
function system_test_drupal_get_filename()
```

## Documentation

```text
Page callback to run drupal_get_filename() on a particular module.
```

## Code

```php
function system_test_drupal_get_filename() {
  // Prevent SimpleTest from failing as a result of the expected PHP warnings
  // this function causes. Any warnings will be recorded in the database logs
  // for examination by the tests.
  define('SIMPLETEST_COLLECT_ERRORS', FALSE);

  $module_name = variable_get('system_test_drupal_get_filename_test_module_name');
  drupal_get_filename('module', $module_name);

  return '';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
