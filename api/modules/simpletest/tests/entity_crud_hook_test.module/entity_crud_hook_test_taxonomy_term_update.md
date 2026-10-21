# entity_crud_hook_test_taxonomy_term_update()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 186–188 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L186-L188)
- **Module/theme:** batch_test
- **Implements:** [hook_taxonomy_term_update()](../../../taxonomy/taxonomy.api.php/hook_taxonomy_term_update.md)

## Signature

```php
function entity_crud_hook_test_taxonomy_term_update()
```

## Documentation

```text
Implements hook_taxonomy_term_update().
```

## Code

```php
function entity_crud_hook_test_taxonomy_term_update() {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
