# user_delete()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2613–2615 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2613-L2615)
- **Module/theme:** user

## Signature

```php
function user_delete($uid)
```

## Documentation

```text
Delete a user.

@param $uid
  A user ID.
```

## Code

```php
function user_delete($uid) {
  user_delete_multiple(array($uid));
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
