# user_user_categories()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1345–1351 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1345-L1351)
- **Module/theme:** user
- **Implements:** [hook_user_categories()](../user.api.php/hook_user_categories.md)

## Signature

```php
function user_user_categories()
```

## Documentation

```text
Implements hook_user_categories().
```

## Code

```php
function user_user_categories() {
  return array(array(
    'name' => 'account',
    'title' => t('Account settings'),
    'weight' => 1,
  ));
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
