# UpdateDependencyHookInvocationTestCase::testHookUpdateDependencies()

- **Type:** Method
- **File:** [`modules/simpletest/tests/update.test`](../_file.md), lines 108–113 · [local source](../../../../../../source/modules/simpletest/tests/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update.test#L108-L113)
- **Class:** [UpdateDependencyHookInvocationTestCase](../UpdateDependencyHookInvocationTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testHookUpdateDependencies()
```

## Documentation

```text
Test the structure of the array returned by hook_update_dependencies().
```

## Code

```php
  function testHookUpdateDependencies() {
    $update_dependencies = update_retrieve_dependencies();
    $this->assertTrue($update_dependencies['system'][7000]['update_test_1'] == 7000, 'An update function that has a dependency on two separate modules has the first dependency recorded correctly.');
    $this->assertTrue($update_dependencies['system'][7000]['update_test_2'] == 7001, 'An update function that has a dependency on two separate modules has the second dependency recorded correctly.');
    $this->assertTrue($update_dependencies['system'][7001]['update_test_1'] == 7002, 'An update function that depends on more than one update from the same module only has the dependency on the higher-numbered update function recorded.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/update.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
