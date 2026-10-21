# database_test_odd_pager_query()

- **Type:** Function
- **File:** [`modules/simpletest/tests/database_test.module`](_file.md), lines 122–138 · [local source](../../../../../source/modules/simpletest/tests/database_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.module#L122-L138)
- **Module/theme:** batch_test

## Signature

```php
function database_test_odd_pager_query($limit)
```

## Documentation

```text
Run a pager query and return the results.

This function does care about the page GET parameter, as set by the
simpletest HTTP call.
```

## Code

```php
function database_test_odd_pager_query($limit) {

  $query = db_select('test_task', 't');
  $query
    ->fields('t', array('task'))
    ->orderBy('pid');

  // This should result in 4 pages of results.
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
