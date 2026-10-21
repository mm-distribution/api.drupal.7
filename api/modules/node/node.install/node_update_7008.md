# node_update_7008()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 799–804 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L799-L804)
- **Module/theme:** node
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function node_update_7008()
```

## Documentation

```text
Split the 'administer nodes' permission from 'access content overview'.
```

## Code

```php
function node_update_7008() {
  $roles = user_roles(FALSE, 'administer nodes');
  foreach ($roles as $rid => $role) {
    _update_7000_user_role_grant_permissions($rid, array('access content overview'), 'node');
  }
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
