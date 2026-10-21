# update_test_1_update_dependencies()

- **Type:** Function
- **File:** [`modules/simpletest/tests/update_test_1.install`](_file.md), lines 13–35 · [local source](../../../../../source/modules/simpletest/tests/update_test_1.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update_test_1.install#L13-L35)
- **Module/theme:** batch_test
- **Implements:** [hook_update_dependencies()](../../../system/system.api.php/hook_update_dependencies.md)

## Signature

```php
function update_test_1_update_dependencies()
```

## Documentation

```text
Implements hook_update_dependencies().

@see update_test_2_update_dependencies()
```

## Code

```php
function update_test_1_update_dependencies() {
  // These dependencies are used in combination with those declared in
  // update_test_2_update_dependencies() for the sole purpose of testing that
  // the results of hook_update_dependencies() are collected correctly and have
  // the correct array structure. Therefore, we use updates from System module
  // (which have already run), so that they will not get in the way of other
  // tests.
  $dependencies['system'][7000] = array(
    // Compare to update_test_2_update_dependencies(), where the same System
    // module update function is forced to depend on an update function from a
    // different module. This allows us to test that both dependencies are
    // correctly recorded.
    'update_test_1' => 7000,
  );
  $dependencies['system'][7001] = array(
    // Compare to update_test_2_update_dependencies(), where the same System
    // module update function is forced to depend on a different update
    // function within the same module. This allows us to test that only the
    // dependency on the higher-numbered update function is recorded.
    'update_test_1' => 7002,
  );
  return $dependencies;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/update_test_1.install](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update_test_1.install) · Licensed GPL-2.0-or-later (see LICENSE)._
