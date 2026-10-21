# user_form_test_menu()

- **Type:** Function
- **File:** [`modules/user/tests/user_form_test.module`](_file.md), lines 13–23 · [local source](../../../../../source/modules/user/tests/user_form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_form_test.module#L13-L23)
- **Module/theme:** user_flood_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function user_form_test_menu()
```

## Documentation

```text
Implements hook_menu().

Sets up a form that allows a user to validate password.
```

## Code

```php
function user_form_test_menu() {
  $items = array();
  $items['user_form_test_current_password/%user'] = array(
    'title' => 'User form test for current password validation',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('user_form_test_current_password',1),
    'access arguments' => array('administer users'),
    'type' => MENU_SUGGESTED_ITEM,
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/user/tests/user_form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
