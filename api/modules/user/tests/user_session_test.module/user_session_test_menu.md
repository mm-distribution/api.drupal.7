# user_session_test_menu()

- **Type:** Function
- **File:** [`modules/user/tests/user_session_test.module`](_file.md), lines 11–18 · [local source](../../../../../source/modules/user/tests/user_session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_session_test.module#L11-L18)
- **Module/theme:** user_flood_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function user_session_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function user_session_test_menu() {
  $items = array();
  $items['user_session_test_anon_session'] = array(
    'page callback' => 'user_session_test_anon_session',
    'access callback' => TRUE,
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/user/tests/user_session_test.module](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_session_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
