# database_test_tablesort()

- **Type:** Function
- **File:** [`modules/simpletest/tests/database_test.module`](_file.md), lines 146–167 · [local source](../../../../../source/modules/simpletest/tests/database_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.module#L146-L167)
- **Module/theme:** batch_test

## Signature

```php
function database_test_tablesort()
```

## Documentation

```text
Run a tablesort query and return the results.

This function does care about the page GET parameter, as set by the
simpletest HTTP call.
```

## Code

```php
function database_test_tablesort() {
  $header = array(
    'tid' => array('data' => t('Task ID'), 'field' => 'tid', 'sort' => 'desc'),
    'pid' => array('data' => t('Person ID'), 'field' => 'pid'),
    'task' => array('data' => t('Task'), 'field' => 'task'),
    'priority' => array('data' => t('Priority'), 'field' => 'priority', ),
  );

  $query = db_select('test_task', 't');
  $query
    ->fields('t', array('tid', 'pid', 'task', 'priority'));

  $query = $query->extend('TableSort')->orderByHeader($header);

  // We need all the results at once to check the sort.
  $tasks = $query->execute()->fetchAll();

  drupal_json_output(array(
    'tasks' => $tasks,
  ));
  exit;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
