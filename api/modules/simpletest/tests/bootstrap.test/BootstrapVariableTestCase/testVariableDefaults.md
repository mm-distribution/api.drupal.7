# BootstrapVariableTestCase::testVariableDefaults()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 322–328 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L322-L328)
- **Class:** [BootstrapVariableTestCase](../BootstrapVariableTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testVariableDefaults()
```

## Documentation

```text
Makes sure that the default variable parameter is passed through okay.
```

## Code

```php
  function testVariableDefaults() {
    // Tests passing nothing through to the default.
    $this->assertIdentical(NULL, variable_get('simpletest_bootstrap_variable_test'), 'Variables are correctly defaulting to NULL.');

    // Tests passing 5 to the default parameter.
    $this->assertIdentical(5, variable_get('simpletest_bootstrap_variable_test', 5), 'The default variable parameter is passed through correctly.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
