# _user_cancel_session_regenerate()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2601–2605 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2601-L2605)
- **Module/theme:** user

## Signature

```php
function _user_cancel_session_regenerate()
```

## Documentation

```text
Implements callback_batch_finished().

Finished batch processing callback for cancelling a user account.

@see user_cancel()
```

## Code

```php
function _user_cancel_session_regenerate() {
  // Regenerate the users session instead of calling session_destroy() as we
  // want to preserve any messages that might have been set.
  drupal_session_regenerate();
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
