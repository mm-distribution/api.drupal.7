# session_test_user_login()

- **Type:** Function
- **File:** [`modules/simpletest/tests/session_test.module`](_file.md), lines 169–175 · [local source](../../../../../source/modules/simpletest/tests/session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module#L169-L175)
- **Module/theme:** batch_test

## Signature

```php
function session_test_user_login($edit = array(), $user = NULL)
```

## Documentation

```text
Implements hook_user().
```

## Code

```php
function session_test_user_login($edit = array(), $user = NULL) {
  if ($user->name == 'session_test_user') {
    // Exit so we can verify that the session was regenerated
    // before hook_user() was called.
    exit;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/session_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
