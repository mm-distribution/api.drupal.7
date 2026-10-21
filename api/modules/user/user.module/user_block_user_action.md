# user_block_user_action()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3797–3813 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3797-L3813)
- **Module/theme:** user
- **Topics:** [actions](../../../topics/actions.md)

## Signature

```php
function user_block_user_action(&$entity, $context = array())
```

## Documentation

```text
Blocks a specific user or the current user, if one is not specified.

@param $entity
  (optional) An entity object; if it is provided and it has a uid property,
  the user with that ID is blocked.
@param $context
  (optional) An associative array; if no user ID is found in $entity, the
  'uid' element of this array determines the user to block.

@ingroup actions
```

## Code

```php
function user_block_user_action(&$entity, $context = array()) {
  // First priority: If there is a $entity->uid, block that user.
  // This is most likely a user object or the author if a node or comment.
  if (isset($entity->uid)) {
    $uid = $entity->uid;
  }
  elseif (isset($context['uid'])) {
    $uid = $context['uid'];
  }
  // If neither of those are valid, then block the current user.
  else {
    $uid = $GLOBALS['user']->uid;
  }
  $account = user_load($uid);
  $account = user_save($account, array('status' => 0));
  watchdog('action', 'Blocked user %name.', array('%name' => $account->name));
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
