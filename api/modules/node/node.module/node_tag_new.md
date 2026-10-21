# node_tag_new()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 305–316 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L305-L316)
- **Module/theme:** node

## Signature

```php
function node_tag_new($node)
```

## Documentation

```text
Updates the 'last viewed' timestamp of the specified node for current user.

@param $node
  A node object.
```

## Code

```php
function node_tag_new($node) {
  global $user;
  if ($user->uid) {
    db_merge('history')
      ->key(array(
        'uid' => $user->uid,
        'nid' => $node->nid,
      ))
      ->fields(array('timestamp' => REQUEST_TIME))
      ->execute();
   }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
