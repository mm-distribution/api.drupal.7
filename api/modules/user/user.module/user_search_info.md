# user_search_info()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 950–954 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L950-L954)
- **Module/theme:** user
- **Implements:** [hook_search_info()](../../search/search.api.php/hook_search_info.md)

## Signature

```php
function user_search_info()
```

## Documentation

```text
Implements hook_search_info().
```

## Code

```php
function user_search_info() {
  return array(
    'title' => 'Users',
  );
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
