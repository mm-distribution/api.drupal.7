# node_assign_owner_action()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3983–3987 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3983-L3987)
- **Module/theme:** node
- **Topics:** [actions](../../../topics/actions.md)

## Signature

```php
function node_assign_owner_action($node, $context)
```

## Documentation

```text
Assigns ownership of a node to a user.

@param $node
  A node object to modify.
@param $context
  Array with the following elements:
  - 'owner_uid': User ID to assign to the node.

@see node_assign_owner_action_form()
@see node_assign_owner_action_validate()
@see node_assign_owner_action_submit()
@ingroup actions
```

## Code

```php
function node_assign_owner_action($node, $context) {
  $node->uid = $context['owner_uid'];
  $owner_name = db_query("SELECT name FROM {users} WHERE uid = :uid", array(':uid' => $context['owner_uid']))->fetchField();
  watchdog('action', 'Changed owner of @type %title to uid %name.', array('@type' =>  node_type_get_name($node), '%title' => $node->title, '%name' => $owner_name));
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
