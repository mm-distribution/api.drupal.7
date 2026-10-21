# user_session_test_anon_session()

- **Type:** Function
- **File:** [`modules/user/tests/user_session_test.module`](_file.md), lines 25–29 · [local source](../../../../../source/modules/user/tests/user_session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_session_test.module#L25-L29)
- **Module/theme:** user_flood_test

## Signature

```php
function user_session_test_anon_session()
```

## Documentation

```text
Page callback.

Creates an anonymous user session.
```

## Code

```php
function user_session_test_anon_session() {
  $data = 'This dummy data will be stored in a user session.';
  $_SESSION[__FUNCTION__] = $data;
  return $data;
}
```

---
_Drupal 7.103 · [modules/user/tests/user_session_test.module](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_session_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
