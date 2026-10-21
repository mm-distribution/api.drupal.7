# user_search_access()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 959–961 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L959-L961)
- **Module/theme:** user
- **Implements:** [hook_search_access()](../../search/search.api.php/hook_search_access.md)

## Signature

```php
function user_search_access()
```

## Documentation

```text
Implements hook_search_access().
```

## Code

```php
function user_search_access() {
  return user_access('access user profiles');
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
