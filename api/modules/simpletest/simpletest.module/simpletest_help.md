# simpletest_help()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 11–25 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L11-L25)
- **Module/theme:** simpletest
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function simpletest_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function simpletest_help($path, $arg) {
  switch ($path) {
    case 'admin/help#simpletest':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Testing module provides a framework for running automated unit tests. It can be used to verify a working state of Drupal before and after any code changes, or as a means for developers to write and execute tests for their modules. For more information, see the online handbook entry for <a href="@simpletest">Testing module</a>.', array('@simpletest' => 'http://drupal.org/documentation/modules/simpletest', '@blocks' => url('admin/structure/block'))) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Running tests') . '</dt>';
      $output .= '<dd>' . t('Visit the <a href="@admin-simpletest">Testing page</a> to display a list of available tests. For comprehensive testing, select <em>all</em> tests, or individually select tests for more targeted testing. Note that it might take several minutes for all tests to complete. For more information on creating and modifying your own tests, see the <a href="@simpletest-api">Testing API Documentation</a> in the Drupal handbook.', array('@simpletest-api' => 'http://drupal.org/simpletest', '@admin-simpletest' => url('admin/config/development/testing'))) . '</dd>';
      $output .= '<dd>' . t('After the tests run, a message will be displayed next to each test group indicating whether tests within it passed, failed, or had exceptions. A pass means that the test returned the expected results, while fail means that it did not. An exception normally indicates an error outside of the test, such as a PHP warning or notice. If there were failures or exceptions, the results will be expanded to show details, and the tests that had failures or exceptions will be indicated in red or pink rows. You can then use these results to refine your code and tests, until all tests pass.') . '</dd>';
      $output .= '</dl>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
