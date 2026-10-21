# update_test_menu()

- **Type:** Function
- **File:** [`modules/update/tests/update_test.module`](_file.md), lines 21–38 · [local source](../../../../../source/modules/update/tests/update_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module#L21-L38)
- **Module/theme:** aaa_update_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function update_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function update_test_menu() {
  $items = array();

  $items['update-test'] = array(
    'title' => t('Update test'),
    'page callback' => 'update_test_mock_page',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['503-error'] = array(
    'title' => t('503 Service unavailable'),
    'page callback' => 'update_callback_service_unavailable',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/update/tests/update_test.module](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
