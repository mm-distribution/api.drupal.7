# entity_query_access_test_menu()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_query_access_test.module`](_file.md), lines 11–21 · [local source](../../../../../source/modules/simpletest/tests/entity_query_access_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query_access_test.module#L11-L21)
- **Module/theme:** batch_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function entity_query_access_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function entity_query_access_test_menu() {
  $items['entity-query-access/test/%'] = array(
    'title' => "Retrieve a sample of entity query access data",
    'page callback' => 'entity_query_access_test_sample_query',
    'page arguments' => array(2),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_query_access_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query_access_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
