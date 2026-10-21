# shortcut_current_displayed_set()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 481–508 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L481-L508)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_current_displayed_set($account = NULL)
```

## Documentation

```text
Returns the current displayed shortcut set for the provided user account.

@param $account
  (optional) The user account whose shortcuts will be returned. Defaults to
  the currently logged-in user.

@return
  An object representing the shortcut set that should be displayed to the
  current user. If the user does not have an explicit shortcut set defined,
  the default set is returned.
```

## Code

```php
function shortcut_current_displayed_set($account = NULL) {
  $shortcut_sets = &drupal_static(__FUNCTION__, array());
  global $user;
  if (!isset($account)) {
    $account = $user;
  }
  // Try to return a shortcut set from the static cache.
  if (isset($shortcut_sets[$account->uid])) {
    return $shortcut_sets[$account->uid];
  }
  // If none was found, try to find a shortcut set that is explicitly assigned
  // to this user.
  $query = db_select('shortcut_set', 's');
  $query->addField('s', 'set_name');
  $query->join('shortcut_set_users', 'u', 's.set_name = u.set_name');
  $query->condition('u.uid', $account->uid);
  $shortcut_set_name = $query->execute()->fetchField();
  if ($shortcut_set_name) {
    $shortcut_set = shortcut_set_load($shortcut_set_name);
  }
  // Otherwise, use the default set.
  else {
    $shortcut_set = shortcut_default_set($account);
  }

  $shortcut_sets[$account->uid] = $shortcut_set;
  return $shortcut_set;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
