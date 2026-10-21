# entity_crud_hook_test_taxonomy_vocabulary_delete()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 242–244 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L242-L244)
- **Module/theme:** batch_test
- **Implements:** [hook_taxonomy_vocabulary_delete()](../../../taxonomy/taxonomy.api.php/hook_taxonomy_vocabulary_delete.md)

## Signature

```php
function entity_crud_hook_test_taxonomy_vocabulary_delete()
```

## Documentation

```text
Implements hook_taxonomy_vocabulary_delete().
```

## Code

```php
function entity_crud_hook_test_taxonomy_vocabulary_delete() {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
