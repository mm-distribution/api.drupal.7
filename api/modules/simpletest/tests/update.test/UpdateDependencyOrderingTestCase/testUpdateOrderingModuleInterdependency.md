# UpdateDependencyOrderingTestCase::testUpdateOrderingModuleInterdependency()

- **Type:** Method
- **File:** [`modules/simpletest/tests/update.test`](../_file.md), lines 44–55 · [local source](../../../../../../source/modules/simpletest/tests/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update.test#L44-L55)
- **Class:** [UpdateDependencyOrderingTestCase](../UpdateDependencyOrderingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testUpdateOrderingModuleInterdependency()
```

## Documentation

```text
Test that dependencies between modules are resolved correctly.
```

## Code

```php
  function testUpdateOrderingModuleInterdependency() {
    $starting_updates = array(
      'update_test_2' => 7000,
      'update_test_3' => 7000,
    );
    $update_order = array_keys(update_resolve_dependencies($starting_updates));
    // Make sure that each dependency is satisfied.
    $first_dependency_satisfied = array_search('update_test_2_update_7000', $update_order) < array_search('update_test_3_update_7000', $update_order);
    $this->assertTrue($first_dependency_satisfied, 'The dependency of the second module on the first module is respected by the update function order.');
    $second_dependency_satisfied = array_search('update_test_3_update_7000', $update_order) < array_search('update_test_2_update_7001', $update_order);
    $this->assertTrue($second_dependency_satisfied, 'The dependency of the first module on the second module is respected by the update function order.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/update.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
