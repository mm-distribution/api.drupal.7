# database_test_even_pager_query()

- **Type:** Function
- **File:** [`modules/simpletest/tests/database_test.module`](_file.md), lines 98–114 · [local source](../../../../../source/modules/simpletest/tests/database_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.module#L98-L114)
- **Module/theme:** batch_test

## Signature

```php
function database_test_even_pager_query($limit)
```

## Documentation

```text
Run a pager query and return the results.

This function does care about the page GET parameter, as set by the
simpletest HTTP call.
```

## Code

```php
function database_test_even_pager_query($limit) {

  $query = db_select('test', 't');
  $query
    ->fields('t', array('name'))
    ->orderBy('age');

  // This should result in 2 pages of results.
  $query = $query->extend('PagerDefault')->limit($limit);

  $names = $query->execute()->fetchCol();

  drupal_json_output(array(
    'names' => $names,
  ));
  exit;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
