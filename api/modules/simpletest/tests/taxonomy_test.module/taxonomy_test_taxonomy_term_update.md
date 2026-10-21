# taxonomy_test_taxonomy_term_update()

- **Type:** Function
- **File:** [`modules/simpletest/tests/taxonomy_test.module`](_file.md), lines 39–48 · [local source](../../../../../source/modules/simpletest/tests/taxonomy_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module#L39-L48)
- **Module/theme:** batch_test
- **Implements:** [hook_taxonomy_term_update()](../../../taxonomy/taxonomy.api.php/hook_taxonomy_term_update.md)

## Signature

```php
function taxonomy_test_taxonomy_term_update($term)
```

## Documentation

```text
Implements hook_taxonomy_term_update().
```

## Code

```php
function taxonomy_test_taxonomy_term_update($term) {
  if (!empty($term->antonym)) {
    db_merge('taxonomy_term_antonym')
      ->key(array('tid' => $term->tid))
      ->fields(array(
        'name' => trim($term->antonym)
      ))
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/taxonomy_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
