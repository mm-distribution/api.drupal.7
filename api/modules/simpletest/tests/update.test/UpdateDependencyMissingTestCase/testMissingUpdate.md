# UpdateDependencyMissingTestCase::testMissingUpdate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/update.test`](../_file.md), lines 77–85 · [local source](../../../../../../source/modules/simpletest/tests/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update.test#L77-L85)
- **Class:** [UpdateDependencyMissingTestCase](../UpdateDependencyMissingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMissingUpdate()
```

## Documentation

_No docblock in source._

## Code

```php
  function testMissingUpdate() {
    $starting_updates = array(
      'update_test_2' => 7000,
    );
    $update_graph = update_resolve_dependencies($starting_updates);
    $this->assertTrue($update_graph['update_test_2_update_7000']['allowed'], "The module's first update function is allowed to run, since it does not have any missing dependencies.");
    $this->assertFalse($update_graph['update_test_2_update_7001']['allowed'], "The module's second update function is not allowed to run, since it has a direct dependency on a missing update.");
    $this->assertFalse($update_graph['update_test_2_update_7002']['allowed'], "The module's third update function is not allowed to run, since it has an indirect dependency on a missing update.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/update.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
