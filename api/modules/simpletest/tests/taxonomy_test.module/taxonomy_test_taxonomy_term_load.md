# taxonomy_test_taxonomy_term_load()

- **Type:** Function
- **File:** [`modules/simpletest/tests/taxonomy_test.module`](_file.md), lines 13–20 · [local source](../../../../../source/modules/simpletest/tests/taxonomy_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module#L13-L20)
- **Module/theme:** batch_test
- **Implements:** [hook_taxonomy_term_load()](../../../taxonomy/taxonomy.api.php/hook_taxonomy_term_load.md)

## Signature

```php
function taxonomy_test_taxonomy_term_load($terms)
```

## Documentation

```text
Implements hook_taxonomy_term_load().
```

## Code

```php
function taxonomy_test_taxonomy_term_load($terms) {
  foreach ($terms as $term) {
    $antonym = taxonomy_test_get_antonym($term->tid);
    if ($antonym) {
      $term->antonym = $antonym;
    }
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/taxonomy_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
