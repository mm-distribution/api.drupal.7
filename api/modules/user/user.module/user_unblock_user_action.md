# user_unblock_user_action()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3827–3850 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3827-L3850)
- **Module/theme:** user
- **Topics:** [actions](../../../topics/actions.md)

## Signature

```php
function user_unblock_user_action(&$entity, $context = array())
```

## Documentation

```text
Unblocks a specific user or the current user, if one is not specified.

@param $entity
  (optional) An entity object; if it is provided and it has a uid property,
  the user with that ID is unblocked.
@param $context
  (optional) An associative array; if no user ID is found in $entity, the
  'uid' element of this array determines the user to unblock.

@ingroup actions
```

## Code

```php
function user_unblock_user_action(&$entity, $context = array()) {
  // First priority: If there is a $entity->uid, unblock that user.
  // This is most likely a user object or the author if a node or comment.
  if (isset($entity->uid)) {
    $uid = $entity->uid;
  }
  elseif (isset($context['uid'])) {
    $uid = $context['uid'];
  }
  // If neither of those are valid, then unblock the current user.
  else {
    $uid = $GLOBALS['user']->uid;
  }

  // The anonymous user should not be unblocked.
  if ($uid == 0) {
    watchdog('action', 'Anonymous user should not be unblocked.', array(), WATCHDOG_WARNING);
    return;
  }

  $account = user_load($uid);
  $account = user_save($account, array('status' => 1));
  watchdog('action', 'Unblocked user %name.', array('%name' => $account->name));
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
