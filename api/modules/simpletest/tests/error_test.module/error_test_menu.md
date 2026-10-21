# error_test_menu()

- **Type:** Function
- **File:** [`modules/simpletest/tests/error_test.module`](_file.md), lines 6–34 · [local source](../../../../../source/modules/simpletest/tests/error_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error_test.module#L6-L34)
- **Module/theme:** batch_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function error_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function error_test_menu() {
  $items['error-test/generate-warnings'] = array(
    'title' => 'Generate warnings',
    'page callback' => 'error_test_generate_warnings',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['error-test/generate-warnings-with-report'] = array(
    'title' => 'Generate warnings with Simpletest reporting',
    'page callback' => 'error_test_generate_warnings',
    'page arguments' => array(TRUE),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['error-test/trigger-exception'] = array(
    'title' => 'Trigger an exception',
    'page callback' => 'error_test_trigger_exception',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['error-test/trigger-pdo-exception'] = array(
    'title' => 'Trigger a PDO exception',
    'page callback' => 'error_test_trigger_pdo_exception',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/error_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
