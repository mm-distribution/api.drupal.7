# node_access_grants()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3215–3227 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3215-L3227)
- **Module/theme:** node
- **Topics:** [node_access](../../../topics/node_access.md)

## Signature

```php
function node_access_grants($op, $account = NULL)
```

## Documentation

```text
Fetches an array of permission IDs granted to the given user ID.

The implementation here provides only the universal "all" grant. A node
access module should implement hook_node_grants() to provide a grant list for
the user.

After the default grants have been loaded, we allow modules to alter the
grants array by reference. This hook allows for complex business logic to be
applied when integrating multiple node access modules.

@param $op
  The operation that the user is trying to perform.
@param $account
  The user object for the user performing the operation. If omitted, the
  current user is used.

@return
  An associative array in which the keys are realms, and the values are
  arrays of grants for those realms.
```

## Code

```php
function node_access_grants($op, $account = NULL) {

  if (!isset($account)) {
    $account = $GLOBALS['user'];
  }

  // Fetch node access grants from other modules.
  $grants = module_invoke_all('node_grants', $account, $op);
  // Allow modules to alter the assigned grants.
  drupal_alter('node_grants', $grants, $account, $op);

  return array_merge(array('all' => array(0)), $grants);
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
