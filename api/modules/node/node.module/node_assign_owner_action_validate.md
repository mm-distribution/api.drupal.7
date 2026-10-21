# node_assign_owner_action_validate()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 4044–4049 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L4044-L4049)
- **Module/theme:** node

## Signature

```php
function node_assign_owner_action_validate($form, $form_state)
```

## Documentation

```text
Validates settings form for node_assign_owner_action().

@see node_assign_owner_action_submit()
```

## Code

```php
function node_assign_owner_action_validate($form, $form_state) {
  $exists = (bool) db_query_range('SELECT 1 FROM {users} WHERE name = :name', 0, 1, array(':name' => $form_state['values']['owner_name']))->fetchField();
  if (!$exists) {
    form_set_error('owner_name', t('Enter a valid username.'));
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
