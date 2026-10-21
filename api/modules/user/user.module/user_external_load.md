# user_external_load()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 249–258 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L249-L258)
- **Module/theme:** user

## Signature

```php
function user_external_load($authname)
```

## Documentation

```text
Fetches a user object based on an external authentication source.

@param string $authname
  The external authentication username.

@return
  A fully-loaded user object if the user is found or FALSE if not found.
```

## Code

```php
function user_external_load($authname) {
  $uid = db_query("SELECT uid FROM {authmap} WHERE authname = :authname", array(':authname' => $authname))->fetchField();

  if ($uid) {
    return user_load($uid);
  }
  else {
    return FALSE;
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
