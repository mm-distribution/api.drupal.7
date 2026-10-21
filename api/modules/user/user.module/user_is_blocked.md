# user_is_blocked()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 850–856 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L850-L856)
- **Module/theme:** user

## Signature

```php
function user_is_blocked($name)
```

## Documentation

```text
Checks for usernames blocked by user administration.

@param $name
  A string containing a name of the user.

@return
  Object with property 'name' (the user name), if the user is blocked;
  FALSE if the user is not blocked.
```

## Code

```php
function user_is_blocked($name) {
  return db_select('users')
    ->fields('users', array('name'))
    ->condition('name', db_like($name), 'LIKE')
    ->condition('status', 0)
    ->execute()->fetchObject();
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
