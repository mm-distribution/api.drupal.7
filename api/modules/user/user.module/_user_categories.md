# _user_categories()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3481–3486 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3481-L3486)
- **Module/theme:** user

## Signature

```php
function _user_categories()
```

## Documentation

```text
Retrieve a list of all user setting/information categories and sort them by weight.
```

## Code

```php
function _user_categories() {
  $categories = module_invoke_all('user_categories');
  usort($categories, '_user_sort');

  return $categories;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
