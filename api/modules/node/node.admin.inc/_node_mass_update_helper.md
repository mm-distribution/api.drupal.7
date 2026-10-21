# _node_mass_update_helper()

- **Type:** Function
- **File:** [`modules/node/node.admin.inc`](_file.md), lines 315–324 · [local source](../../../../source/modules/node/node.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc#L315-L324)
- **Module/theme:** node

## Signature

```php
function _node_mass_update_helper($nid, $updates)
```

## Documentation

```text
Updates individual nodes when fewer than 10 are queued.

@param $nid
  ID of node to update.
@param $updates
  Associative array of updates.

@return object
  An updated node object.

@see node_mass_update()
```

## Code

```php
function _node_mass_update_helper($nid, $updates) {
  $node = node_load($nid, NULL, TRUE);
  // For efficiency manually save the original node before applying any changes.
  $node->original = clone $node;
  foreach ($updates as $name => $value) {
    $node->$name = $value;
  }
  node_save($node);
  return $node;
}
```

---
_Drupal 7.103 · [modules/node/node.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
