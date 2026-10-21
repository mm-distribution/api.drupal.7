# user_get_authmaps()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2074–2077 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2074-L2077)
- **Module/theme:** user

## Signature

```php
function user_get_authmaps($authname = NULL)
```

## Documentation

```text
Discover which external authentication module(s) authenticated a username.

@param $authname
  A username used by an external authentication module.
@return
  An associative array with module as key and username as value.
```

## Code

```php
function user_get_authmaps($authname = NULL) {
  $authmaps = db_query("SELECT module, authname FROM {authmap} WHERE authname = :authname", array(':authname' => $authname))->fetchAllKeyed();
  return count($authmaps) ? $authmaps : 0;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
