# UpdateDependencyOrderingTestCase::testUpdateOrderingSingleModule()

- **Type:** Method
- **File:** [`modules/simpletest/tests/update.test`](../_file.md), lines 28–39 · [local source](../../../../../../source/modules/simpletest/tests/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update.test#L28-L39)
- **Class:** [UpdateDependencyOrderingTestCase](../UpdateDependencyOrderingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testUpdateOrderingSingleModule()
```

## Documentation

```text
Test that updates within a single module run in the correct order.
```

## Code

```php
  function testUpdateOrderingSingleModule() {
    $starting_updates = array(
      'update_test_1' => 7000,
    );
    $expected_updates = array(
      'update_test_1_update_7000',
      'update_test_1_update_7001',
      'update_test_1_update_7002',
    );
    $actual_updates = array_keys(update_resolve_dependencies($starting_updates));
    $this->assertEqual($expected_updates, $actual_updates, 'Updates within a single module run in the correct order.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/update.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
