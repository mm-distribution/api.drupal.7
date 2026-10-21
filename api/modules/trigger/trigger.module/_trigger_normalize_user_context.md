# _trigger_normalize_user_context()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 475–488 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L475-L488)
- **Module/theme:** trigger

## Signature

```php
function _trigger_normalize_user_context($type, $account)
```

## Documentation

```text
Loads associated objects for user triggers.

When an action is called in a context that does not match its type, the
object that the action expects must be retrieved. For example, when an action
that works on nodes is called during the user hook, the node object is not
available since the user hook doesn't pass it. So here we load the object the
action expects.

@param $type
  The type of action that is about to be called.
@param $account
  The account object that was passed via the user hook.

@return
  The object expected by the action that is about to be called.
```

## Code

```php
function _trigger_normalize_user_context($type, $account) {
  // Note that comment-type actions are not supported in user contexts,
  // because we wouldn't know which comment to choose.
  switch ($type) {
    // An action that works with nodes is being called in a user context.
    // If a single node is being viewed, return the node.
    case 'node':
      // If we are viewing an individual node, return the node.
      if (arg(0) == 'node' && is_numeric(arg(1)) && arg(2) == NULL) {
        return node_load(array('nid' => arg(1)));
      }
      break;
  }
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
