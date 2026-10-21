# shortcut_set_assign_user()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 441–447 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L441-L447)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_assign_user($shortcut_set, $account)
```

## Documentation

```text
Assigns a user to a particular shortcut set.

@param $shortcut_set
  An object representing the shortcut set.
@param $account
  A user account that will be assigned to use the set.
```

## Code

```php
function shortcut_set_assign_user($shortcut_set, $account) {
  db_merge('shortcut_set_users')
    ->key(array('uid' => $account->uid))
    ->fields(array('set_name' => $shortcut_set->set_name))
    ->execute();
  drupal_static_reset('shortcut_current_displayed_set');
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
