# _trigger_normalize_node_context()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 244–253 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L244-L253)
- **Module/theme:** trigger

## Signature

```php
function _trigger_normalize_node_context($type, $node)
```

## Documentation

```text
Loads associated objects for node triggers.

When an action is called in a context that does not match its type, the
object that the action expects must be retrieved. For example, when an action
that works on users is called during a node hook implementation, the user
object is not available since the node hook call doesn't pass it. So here we
load the object the action expects.

@param $type
  The type of action that is about to be called.
@param $node
  The node that was passed via the node hook.

@return
  The object expected by the action that is about to be called.
```

## Code

```php
function _trigger_normalize_node_context($type, $node) {
  // Note that comment-type actions are not supported in node contexts,
  // because we wouldn't know which comment to choose.
  switch ($type) {
    // An action that works on users is being called in a node context.
    // Load the user object of the node's author.
    case 'user':
      return user_load($node->uid);
  }
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
