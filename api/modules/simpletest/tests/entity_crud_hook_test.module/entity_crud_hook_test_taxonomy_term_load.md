# entity_crud_hook_test_taxonomy_term_load()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 137–139 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L137-L139)
- **Module/theme:** batch_test
- **Implements:** [hook_taxonomy_term_load()](../../../taxonomy/taxonomy.api.php/hook_taxonomy_term_load.md)

## Signature

```php
function entity_crud_hook_test_taxonomy_term_load()
```

## Documentation

```text
Implements hook_taxonomy_term_load().
```

## Code

```php
function entity_crud_hook_test_taxonomy_term_load() {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
