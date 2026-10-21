# simpletest_uninstall()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.install`](_file.md), lines 156–169 · [local source](../../../../source/modules/simpletest/simpletest.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.install#L156-L169)
- **Module/theme:** simpletest
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function simpletest_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function simpletest_uninstall() {
  drupal_load('module', 'simpletest');
  simpletest_clean_database();

  // Remove settings variables.
  variable_del('simpletest_httpauth_method');
  variable_del('simpletest_httpauth_username');
  variable_del('simpletest_httpauth_password');
  variable_del('simpletest_clear_results');
  variable_del('simpletest_verbose');

  // Remove generated files.
  file_unmanaged_delete_recursive('public://simpletest');
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.install](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.install) · Licensed GPL-2.0-or-later (see LICENSE)._
