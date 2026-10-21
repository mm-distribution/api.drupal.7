# update_test_3_update_dependencies()

- **Type:** Function
- **File:** [`modules/simpletest/tests/update_test_3.install`](_file.md), lines 13–18 · [local source](../../../../../source/modules/simpletest/tests/update_test_3.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update_test_3.install#L13-L18)
- **Module/theme:** batch_test
- **Implements:** [hook_update_dependencies()](../../../system/system.api.php/hook_update_dependencies.md)

## Signature

```php
function update_test_3_update_dependencies()
```

## Documentation

```text
Implements hook_update_dependencies().

@see update_test_2_update_dependencies()
```

## Code

```php
function update_test_3_update_dependencies() {
  $dependencies['update_test_3'][7000] = array(
    'update_test_2' => 7000,
  );
  return $dependencies;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/update_test_3.install](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update_test_3.install) · Licensed GPL-2.0-or-later (see LICENSE)._
