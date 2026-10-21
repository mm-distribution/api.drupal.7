# user_user_view()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1025–1044 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1025-L1044)
- **Module/theme:** user
- **Implements:** [hook_user_view()](../user.api.php/hook_user_view.md)

## Signature

```php
function user_user_view($account)
```

## Documentation

```text
Implements hook_user_view().
```

## Code

```php
function user_user_view($account) {
  $account->content['user_picture'] = array(
    '#markup' => theme('user_picture', array('account' => $account)),
    '#weight' => -10,
  );
  if (!isset($account->content['summary'])) {
    $account->content['summary'] = array();
  }
  $account->content['summary'] += array(
    '#type' => 'user_profile_category',
    '#attributes' => array('class' => array('user-member')),
    '#weight' => 5,
    '#title' => t('History'),
  );
  $account->content['summary']['member_for'] = array(
    '#type' => 'user_profile_item',
    '#title' => t('Member for'),
    '#markup' => format_interval(REQUEST_TIME - $account->created),
  );
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
