# hook_node_access_records()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 271–303 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L271-L303)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_access](../../../topics/node_access.md)

## Signature

```php
function hook_node_access_records($node)
```

## Documentation

```text
Set permissions for a node to be written to the database.

When a node is saved, a module implementing hook_node_access_records() will
be asked if it is interested in the access permissions for a node. If it is
interested, it must respond with an array of permissions arrays for that
node.

Node access grants apply regardless of the published or unpublished status
of the node. Implementations must make sure not to grant access to
unpublished nodes if they don't want to change the standard access control
behavior. Your module may need to create a separate access realm to handle
access to unpublished nodes.

Note that the grant values in the return value from your hook must be
integers and not boolean TRUE and FALSE.

Each permissions item in the array is an array with the following elements:
- 'realm': The name of a realm that the module has defined in
  hook_node_grants().
- 'gid': A 'grant ID' from hook_node_grants().
- 'grant_view': If set to 1 a user that has been identified as a member
  of this gid within this realm can view this node. This should usually be
  set to $node->status. Failure to do so may expose unpublished content
  to some users.
- 'grant_update': If set to 1 a user that has been identified as a member
  of this gid within this realm can edit this node.
- 'grant_delete': If set to 1 a user that has been identified as a member
  of this gid within this realm can delete this node.
- 'priority': If multiple modules seek to set permissions on a node, the
  realms that have the highest priority will win out, and realms with a lower
  priority will not be written. If there is any doubt, it is best to
  leave this 0.


When an implementation is interested in a node but want to deny access to
everyone, it may return a "deny all" grant:

@code
$grants[] = array(
  'realm' => 'all',
  'gid' => 0,
  'grant_view' => 0,
  'grant_update' => 0,
  'grant_delete' => 0,
  'priority' => 1,
);
@endcode

Setting the priority should cancel out other grants. In the case of a
conflict between modules, it is safer to use hook_node_access_records_alter()
to return only the deny grant.

Note: a deny all grant is not written to the database; denies are implicit.

@see node_access_write_grants()

@param $node
  The node that has just been saved.

@return
  An array of grants as defined above.

@see hook_node_access_records_alter()
@ingroup node_access
```

## Code

```php
function hook_node_access_records($node) {
  // We only care about the node if it has been marked private. If not, it is
  // treated just like any other node and we completely ignore it.
  if ($node->private) {
    $grants = array();
    // Only published nodes should be viewable to all users. If we allow access
    // blindly here, then all users could view an unpublished node.
    if ($node->status) {
      $grants[] = array(
        'realm' => 'example',
        'gid' => 1,
        'grant_view' => 1,
        'grant_update' => 0,
        'grant_delete' => 0,
        'priority' => 0,
      );
    }
    // For the example_author array, the GID is equivalent to a UID, which
    // means there are many groups of just 1 user.
    // Note that an author can always view his or her nodes, even if they
    // have status unpublished.
    $grants[] = array(
      'realm' => 'example_author',
      'gid' => $node->uid,
      'grant_view' => 1,
      'grant_update' => 1,
      'grant_delete' => 1,
      'priority' => 0,
    );

    return $grants;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_access_records()".

- [node_access_test_node_access_records()](../tests/node_access_test.module/node_access_test_node_access_records.md) — `modules/node/tests/node_access_test.module`
- [node_test_node_access_records()](../tests/node_test.module/node_test_node_access_records.md) — `modules/node/tests/node_test.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
