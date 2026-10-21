# user_edit_access()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1632–1634 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1632-L1634)
- **Module/theme:** user

## Signature

```php
function user_edit_access($account)
```

## Documentation

```text
Access callback for user account editing.
```

## Code

```php
function user_edit_access($account) {
  return (($GLOBALS['user']->uid == $account->uid) || user_access('administer users')) && $account->uid > 0;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
