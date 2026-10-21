# user_action_info()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3768–3783 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3768-L3783)
- **Module/theme:** user
- **Implements:** [hook_action_info()](../../system/system.api.php/hook_action_info.md)

## Signature

```php
function user_action_info()
```

## Documentation

```text
Implements hook_action_info().
```

## Code

```php
function user_action_info() {
  return array(
    'user_block_user_action' => array(
      'label' => t('Block current user'),
      'type' => 'user',
      'configurable' => FALSE,
      'triggers' => array('any'),
    ),
    'user_unblock_user_action' => array(
      'label' => t('Unblock current user'),
      'type' => 'user',
      'configurable' => FALSE,
      'triggers' => array('any'),
     ),
  );
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
