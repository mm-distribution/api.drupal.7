# user_element_info()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1012–1020 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1012-L1020)
- **Module/theme:** user
- **Implements:** [hook_element_info()](../../system/system.api.php/hook_element_info.md)

## Signature

```php
function user_element_info()
```

## Documentation

```text
Implements hook_element_info().
```

## Code

```php
function user_element_info() {
  $types['user_profile_category'] = array(
    '#theme_wrappers' => array('user_profile_category'),
  );
  $types['user_profile_item'] = array(
    '#theme' => 'user_profile_item',
  );
  return $types;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
