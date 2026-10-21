# entity_crud_hook_test_taxonomy_vocabulary_update()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 193–195 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L193-L195)
- **Module/theme:** batch_test
- **Implements:** [hook_taxonomy_vocabulary_update()](../../../taxonomy/taxonomy.api.php/hook_taxonomy_vocabulary_update.md)

## Signature

```php
function entity_crud_hook_test_taxonomy_vocabulary_update()
```

## Documentation

```text
Implements hook_taxonomy_vocabulary_update().
```

## Code

```php
function entity_crud_hook_test_taxonomy_vocabulary_update() {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
