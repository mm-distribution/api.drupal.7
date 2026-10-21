# taxonomy_test_get_antonym()

- **Type:** Function
- **File:** [`modules/simpletest/tests/taxonomy_test.module`](_file.md), lines 105–111 · [local source](../../../../../source/modules/simpletest/tests/taxonomy_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module#L105-L111)
- **Module/theme:** batch_test

## Signature

```php
function taxonomy_test_get_antonym($tid)
```

## Documentation

```text
Return the antonym of the given term ID.
```

## Code

```php
function taxonomy_test_get_antonym($tid) {
  return db_select('taxonomy_term_antonym', 'ta')
    ->fields('ta', array('name'))
    ->condition('tid', $tid)
    ->execute()
    ->fetchField();
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/taxonomy_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
