# _trigger_normalize_comment_context()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 361–371 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L361-L371)
- **Module/theme:** trigger

## Signature

```php
function _trigger_normalize_comment_context($type, $comment)
```

## Documentation

```text
Loads associated objects for comment triggers.

When an action is called in a context that does not match its type, the
object that the action expects must be retrieved. For example, when an action
that works on nodes is called during the comment hook, the node object is not
available since the comment hook doesn't pass it. So here we load the object
the action expects.

@param $type
  The type of action that is about to be called.
@param $comment
  The comment that was passed via the comment hook.

@return
  The object expected by the action that is about to be called.
```

## Code

```php
function _trigger_normalize_comment_context($type, $comment) {
  switch ($type) {
    // An action that works with nodes is being called in a comment context.
    case 'node':
      return node_load(is_array($comment) ? $comment['nid'] : $comment->nid);

    // An action that works on users is being called in a comment context.
    case 'user':
      return user_load(is_array($comment) ? $comment['uid'] : $comment->uid);
  }
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
