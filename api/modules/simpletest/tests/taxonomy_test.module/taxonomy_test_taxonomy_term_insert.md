# taxonomy_test_taxonomy_term_insert()

- **Type:** Function
- **File:** [`modules/simpletest/tests/taxonomy_test.module`](_file.md), lines 25–34 · [local source](../../../../../source/modules/simpletest/tests/taxonomy_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module#L25-L34)
- **Module/theme:** batch_test
- **Implements:** [hook_taxonomy_term_insert()](../../../taxonomy/taxonomy.api.php/hook_taxonomy_term_insert.md)

## Signature

```php
function taxonomy_test_taxonomy_term_insert($term)
```

## Documentation

```text
Implements hook_taxonomy_term_insert().
```

## Code

```php
function taxonomy_test_taxonomy_term_insert($term) {
  if (!empty($term->antonym)) {
    db_insert('taxonomy_term_antonym')
      ->fields(array(
        'tid' => $term->tid,
        'name' => trim($term->antonym)
      ))
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/taxonomy_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
