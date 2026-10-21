# entity_crud_hook_test_taxonomy_vocabulary_insert()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 95–97 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L95-L97)
- **Module/theme:** batch_test
- **Implements:** [hook_taxonomy_vocabulary_insert()](../../../taxonomy/taxonomy.api.php/hook_taxonomy_vocabulary_insert.md)

## Signature

```php
function entity_crud_hook_test_taxonomy_vocabulary_insert()
```

## Documentation

```text
Implements hook_taxonomy_vocabulary_insert().
```

## Code

```php
function entity_crud_hook_test_taxonomy_vocabulary_insert() {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
