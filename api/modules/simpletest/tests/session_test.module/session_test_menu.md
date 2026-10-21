# session_test_menu()

- **Type:** Function
- **File:** [`modules/simpletest/tests/session_test.module`](_file.md), lines 6–65 · [local source](../../../../../source/modules/simpletest/tests/session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module#L6-L65)
- **Module/theme:** batch_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function session_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function session_test_menu() {
  $items['session-test/get'] = array(
    'title' => 'Session value',
    'page callback' => '_session_test_get',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['session-test/id'] = array(
    'title' => 'Session ID',
    'page callback' => '_session_test_id',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['session-test/id-from-cookie'] = array(
    'title' => 'Session ID from cookie',
    'page callback' => '_session_test_id_from_cookie',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['session-test/set/%'] = array(
    'title' => 'Set session value',
    'page callback' => '_session_test_set',
    'page arguments' => array(2),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['session-test/no-set/%'] = array(
    'title' => 'Set session value but do not save session',
    'page callback' => '_session_test_no_set',
    'page arguments' => array(2),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['session-test/set-message'] = array(
    'title' => 'Set message',
    'page callback' => '_session_test_set_message',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['session-test/set-message-but-dont-save'] = array(
    'title' => 'Set message but do not save session',
    'page callback' => '_session_test_set_message_but_dont_save',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['session-test/set-not-started'] = array(
    'title' => 'Set message when session is not started',
    'page callback' => '_session_test_set_not_started',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['session-test/is-logged-in'] = array(
    'title' => 'Check if user is logged in',
    'page callback' => '_session_test_is_logged_in',
    'access callback' => 'user_is_logged_in',
    'type' => MENU_CALLBACK,
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/session_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
