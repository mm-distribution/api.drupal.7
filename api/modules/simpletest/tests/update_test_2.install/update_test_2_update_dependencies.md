# update_test_2_update_dependencies()

- **Type:** Function
- **File:** [`modules/simpletest/tests/update_test_2.install`](_file.md), lines 14–35 · [local source](../../../../../source/modules/simpletest/tests/update_test_2.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update_test_2.install#L14-L35)
- **Module/theme:** batch_test
- **Implements:** [hook_update_dependencies()](../../../system/system.api.php/hook_update_dependencies.md)

## Signature

```php
function update_test_2_update_dependencies()
```

## Documentation

```text
Implements hook_update_dependencies().

@see update_test_1_update_dependencies()
@see update_test_3_update_dependencies()
```

## Code

```php
function update_test_2_update_dependencies() {
  // Combined with update_test_3_update_dependencies(), we are declaring here
  // that these two modules run updates in the following order:
  // 1. update_test_2_update_7000()
  // 2. update_test_3_update_7000()
  // 3. update_test_2_update_7001()
  // 4. update_test_2_update_7002()
  $dependencies['update_test_2'][7001] = array(
    'update_test_3' => 7000,
  );

  // These are coordinated with the corresponding dependencies declared in
  // update_test_1_update_dependencies().
  $dependencies['system'][7000] = array(
    'update_test_2' => 7001,
  );
  $dependencies['system'][7001] = array(
    'update_test_1' => 7001,
  );

  return $dependencies;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/update_test_2.install](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update_test_2.install) · Licensed GPL-2.0-or-later (see LICENSE)._
