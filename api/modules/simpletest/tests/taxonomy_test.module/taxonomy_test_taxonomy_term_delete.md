# taxonomy_test_taxonomy_term_delete()

- **Type:** Function
- **File:** [`modules/simpletest/tests/taxonomy_test.module`](_file.md), lines 53–57 · [local source](../../../../../source/modules/simpletest/tests/taxonomy_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module#L53-L57)
- **Module/theme:** batch_test
- **Implements:** [hook_taxonomy_term_delete()](../../../taxonomy/taxonomy.api.php/hook_taxonomy_term_delete.md)

## Signature

```php
function taxonomy_test_taxonomy_term_delete($term)
```

## Documentation

```text
Implements hook_taxonomy_term_delete().
```

## Code

```php
function taxonomy_test_taxonomy_term_delete($term) {
  db_delete('taxonomy_term_antonym')
    ->condition('tid', $term->tid)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/taxonomy_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
