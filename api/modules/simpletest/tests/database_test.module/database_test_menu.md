# database_test_menu()

- **Type:** Function
- **File:** [`modules/simpletest/tests/database_test.module`](_file.md), lines 47–74 · [local source](../../../../../source/modules/simpletest/tests/database_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.module#L47-L74)
- **Module/theme:** batch_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function database_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function database_test_menu() {
  $items['database_test/db_query_temporary'] = array(
    'access callback' => TRUE,
    'page callback' => 'database_test_db_query_temporary',
  );
  $items['database_test/pager_query_even'] = array(
    'access callback' => TRUE,
    'page callback' => 'database_test_even_pager_query',
  );
  $items['database_test/pager_query_odd'] = array(
    'access callback' => TRUE,
    'page callback' => 'database_test_odd_pager_query',
  );
  $items['database_test/tablesort'] = array(
    'access callback' => TRUE,
    'page callback' => 'database_test_tablesort',
  );
  $items['database_test/tablesort_first'] = array(
    'access callback' => TRUE,
    'page callback' => 'database_test_tablesort_first',
  );
  $items['database_test/tablesort_default_sort'] = array(
    'access callback' => TRUE,
    'page callback' => 'drupal_get_form',
    'page arguments' => array('database_test_theme_tablesort'),
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
