# anonymous_user_unblock_test_user_load()

- **Type:** Function
- **File:** [`modules/user/tests/anonymous_user_unblock_test.module`](_file.md), lines 11–20 · [local source](../../../../../source/modules/user/tests/anonymous_user_unblock_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/anonymous_user_unblock_test.module#L11-L20)
- **Module/theme:** user_flood_test
- **Implements:** [hook_user_load()](../../user.api.php/hook_user_load.md)

## Signature

```php
function anonymous_user_unblock_test_user_load($users)
```

## Documentation

```text
Implements hook_user_load().
```

## Code

```php
function anonymous_user_unblock_test_user_load($users) {
  foreach ($users as $user) {
    if ($user->uid == 0) {
      // Try to fool user_save() into unblocking the anonymous user.
      // See https://www.drupal.org/comment/14722637.
      $user->is_new = FALSE;
      $user->original = clone $user;
    }
  }
}
```

---
_Drupal 7.103 · [modules/user/tests/anonymous_user_unblock_test.module](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/anonymous_user_unblock_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
