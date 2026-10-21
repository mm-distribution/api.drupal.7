# modules/simpletest/tests/session_test.module

- **Source:** [local](../../../../../source/modules/simpletest/tests/session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module) · 206 lines
- **Module/theme:** batch_test

## Functions (derived index)

- [session_test_menu()](session_test_menu.md) — Implements hook_menu().
- [session_test_boot()](session_test_boot.md) — Implements hook_boot().
- [_session_test_get()](_session_test_get.md) — Page callback, prints the stored session value to the screen.
- [_session_test_set()](_session_test_set.md) — Page callback, stores a value in $_SESSION['session_test_value'].
- [_session_test_no_set()](_session_test_no_set.md) — Menu callback: turns off session saving and then tries to save a value anyway.
- [_session_test_id()](_session_test_id.md) — Menu callback: print the current session ID.
- [_session_test_id_from_cookie()](_session_test_id_from_cookie.md) — Menu callback: print the current session ID as read from the cookie.
- [_session_test_set_message()](_session_test_set_message.md) — Menu callback, sets a message to me displayed on the following page.
- [_session_test_set_message_but_dont_save()](_session_test_set_message_but_dont_save.md) — Menu callback, sets a message but call drupal_save_session(FALSE).
- [_session_test_set_not_started()](_session_test_set_not_started.md) — Menu callback, stores a value in $_SESSION['session_test_value'] without having started the session in advance.
- [session_test_user_login()](session_test_user_login.md) — Implements hook_user().
- [session_test_form_user_login_alter()](session_test_form_user_login_alter.md) — Implements hook_form_FORM_ID_alter().
- [session_test_drupal_goto_alter()](session_test_drupal_goto_alter.md) — Implements hook_drupal_goto_alter().
- [_session_test_is_logged_in()](_session_test_is_logged_in.md) — Menu callback, only available if current user is logged in.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
