# BootstrapVariableTestCase::testVariable()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 302–317 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L302-L317)
- **Class:** [BootstrapVariableTestCase](../BootstrapVariableTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testVariable()
```

## Documentation

```text
testVariable
```

## Code

```php
  function testVariable() {
    // Setting and retrieving values.
    $variable = $this->randomName();
    variable_set('simpletest_bootstrap_variable_test', $variable);
    $this->assertIdentical($variable, variable_get('simpletest_bootstrap_variable_test'), 'Setting and retrieving values');

    // Make sure the variable persists across multiple requests.
    $this->drupalGet('system-test/variable-get');
    $this->assertText($variable, 'Variable persists across multiple requests');

    // Deleting variables.
    $default_value = $this->randomName();
    variable_del('simpletest_bootstrap_variable_test');
    $variable = variable_get('simpletest_bootstrap_variable_test', $default_value);
    $this->assertIdentical($variable, $default_value, 'Deleting variables');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
