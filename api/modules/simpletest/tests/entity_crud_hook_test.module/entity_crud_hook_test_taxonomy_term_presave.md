# entity_crud_hook_test_taxonomy_term_presave()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 39–41 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L39-L41)
- **Module/theme:** batch_test
- **Implements:** [hook_taxonomy_term_presave()](../../../taxonomy/taxonomy.api.php/hook_taxonomy_term_presave.md)

## Signature

```php
function entity_crud_hook_test_taxonomy_term_presave()
```

## Documentation

```text
Implements hook_taxonomy_term_presave().
```

## Code

```php
function entity_crud_hook_test_taxonomy_term_presave() {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
