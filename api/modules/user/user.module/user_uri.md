# user_uri()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 192–196 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L192-L196)
- **Module/theme:** user

## Signature

```php
function user_uri($user)
```

## Documentation

```text
Implements callback_entity_info_uri().
```

## Code

```php
function user_uri($user) {
  return array(
    'path' => 'user/' . $user->uid,
  );
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
