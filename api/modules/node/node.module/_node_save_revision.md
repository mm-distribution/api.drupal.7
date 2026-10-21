# _node_save_revision()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1215–1226 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1215-L1226)
- **Module/theme:** node

## Signature

```php
function _node_save_revision($node, $uid, $update = NULL)
```

## Documentation

```text
Helper function to save a revision with the uid of the current user.

The resulting revision ID is available afterward in $node->vid.

@param $node
  A node object.
@param $uid
  The current user's UID.
@param $update
  (optional) An array of primary keys' field names to update.
```

## Code

```php
function _node_save_revision($node, $uid, $update = NULL) {
  $temp_uid = $node->uid;
  $node->uid = $uid;
  if (isset($update)) {
    drupal_write_record('node_revision', $node, $update);
  }
  else {
    drupal_write_record('node_revision', $node);
  }
  // Have node object still show node owner's uid, not revision author's.
  $node->uid = $temp_uid;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
