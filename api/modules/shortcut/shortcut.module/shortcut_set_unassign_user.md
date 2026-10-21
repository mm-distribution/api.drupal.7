# shortcut_set_unassign_user()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 462–467 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L462-L467)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_unassign_user($account)
```

## Documentation

```text
Unassigns a user from any shortcut set they may have been assigned to.

The user will go back to using whatever default set applies.

@param $account
  A user account that will be removed from the shortcut set assignment.

@return
  TRUE if the user was previously assigned to a shortcut set and has been
  successfully removed from it. FALSE if the user was already not assigned
  to any set.
```

## Code

```php
function shortcut_set_unassign_user($account) {
  $deleted = db_delete('shortcut_set_users')
    ->condition('uid', $account->uid)
    ->execute();
  return (bool) $deleted;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
