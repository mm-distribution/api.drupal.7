# node_assign_owner_action_submit()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 4056–4060 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L4056-L4060)
- **Module/theme:** node

## Signature

```php
function node_assign_owner_action_submit($form, $form_state)
```

## Documentation

```text
Saves settings form for node_assign_owner_action().

@see node_assign_owner_action_validate()
```

## Code

```php
function node_assign_owner_action_submit($form, $form_state) {
  // Username can change, so we need to store the ID, not the username.
  $uid = db_query('SELECT uid from {users} WHERE name = :name', array(':name' => $form_state['values']['owner_name']))->fetchField();
  return array('owner_uid' => $uid);
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
