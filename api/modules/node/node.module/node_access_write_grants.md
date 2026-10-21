# node_access_write_grants()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3546–3570 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3546-L3570)
- **Module/theme:** node
- **Topics:** [node_access](../../../topics/node_access.md)

## Signature

```php
function node_access_write_grants($node, $grants, $realm = NULL, $delete = TRUE)
```

## Documentation

```text
Writes a list of grants to the database, deleting any previously saved ones.

If a realm is provided, it will only delete grants from that realm, but it
will always delete a grant from the 'all' realm. Modules that utilize
node_access() can use this function when doing mass updates due to widespread
permission changes.

Note: Don't call this function directly from a contributed module. Call
node_access_acquire_grants() instead.

@param $node
  The node whose grants are being written.
@param $grants
  A list of grants to write. Each grant is an array that must contain the
  following keys: realm, gid, grant_view, grant_update, grant_delete.
  The realm is specified by a particular module; the gid is as well, and
  is a module-defined id to define grant privileges. each grant_* field
  is a boolean value.
@param $realm
  (optional) If provided, read/write grants for that realm only. Defaults to
  NULL.
@param $delete
  (optional) If false, does not delete records. This is only for optimization
  purposes, and assumes the caller has already performed a mass delete of
  some form. Defaults to TRUE.

@see node_access_acquire_grants()
```

## Code

```php
function node_access_write_grants($node, $grants, $realm = NULL, $delete = TRUE) {
  if ($delete) {
    $query = db_delete('node_access')->condition('nid', $node->nid);
    if ($realm) {
      $query->condition('realm', array($realm, 'all'), 'IN');
    }
    $query->execute();
  }

  // Only perform work when node_access modules are active.
  if (!empty($grants) && count(module_implements('node_grants'))) {
    $query = db_insert('node_access')->fields(array('nid', 'realm', 'gid', 'grant_view', 'grant_update', 'grant_delete'));
    foreach ($grants as $grant) {
      if ($realm && $realm != $grant['realm']) {
        continue;
      }
      // Only write grants; denies are implicit.
      if ($grant['grant_view'] || $grant['grant_update'] || $grant['grant_delete']) {
        $grant['nid'] = $node->nid;
        $query->values($grant);
      }
    }
    $query->execute();
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
