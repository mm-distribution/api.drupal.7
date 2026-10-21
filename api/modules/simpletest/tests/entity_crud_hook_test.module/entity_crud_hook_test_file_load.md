# entity_crud_hook_test_file_load()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 123–125 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L123-L125)
- **Module/theme:** batch_test
- **Implements:** [hook_file_load()](../../../system/system.api.php/hook_file_load.md)

## Signature

```php
function entity_crud_hook_test_file_load()
```

## Documentation

```text
Implements hook_file_load().
```

## Code

```php
function entity_crud_hook_test_file_load() {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
