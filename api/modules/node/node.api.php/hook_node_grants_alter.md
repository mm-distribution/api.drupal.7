# hook_node_grants_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 385–402 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L385-L402)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_access](../../../topics/node_access.md)

## Signature

```php
function hook_node_grants_alter(&$grants, $account, $op)
```

## Documentation

```text
Alter user access rules when trying to view, edit or delete a node.

Node access modules establish rules for user access to content.
hook_node_grants() defines permissions for a user to view, edit or delete
nodes by building a $grants array that indicates the permissions assigned to
the user by each node access module. This hook is called to allow modules to
modify the $grants array by reference, so the interaction of multiple node
access modules can be altered or advanced business logic can be applied.

@see hook_node_grants()

The resulting grants are then checked against the records stored in the
{node_access} table to determine if the operation may be completed.

A module may deny all access to a user by setting $grants to an empty array.

@see hook_node_access_records()
@see hook_node_access_records_alter()

@param $grants
  The $grants array returned by hook_node_grants().
@param $account
  The user account requesting access to content.
@param $op
  The operation being performed, 'view', 'update' or 'delete'.

Developers may use this hook to either add additional grants to a user or to
remove existing grants. These rules are typically based on either the
permissions assigned to a user role, or specific attributes of a user
account.

@ingroup node_access
```

## Code

```php
function hook_node_grants_alter(&$grants, $account, $op) {
  // Our sample module never allows certain roles to edit or delete
  // content. Since some other node access modules might allow this
  // permission, we expressly remove it by returning an empty $grants
  // array for roles specified in our variable setting.

  // Get our list of banned roles.
  $restricted = variable_get('example_restricted_roles', array());

  if ($op != 'view' && !empty($restricted)) {
    // Now check the roles for this account against the restrictions.
    foreach ($restricted as $role_id) {
      if (isset($account->roles[$role_id])) {
        $grants = array();
      }
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_grants_alter()".

- [node_test_node_grants_alter()](../tests/node_test.module/node_test_node_grants_alter.md) — `modules/node/tests/node_test.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
