# node_revision_delete()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1297–1314 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1297-L1314)
- **Module/theme:** node

## Signature

```php
function node_revision_delete($revision_id)
```

## Documentation

```text
Deletes a node revision.

@param $revision_id
  The revision ID to delete.
```

## Code

```php
function node_revision_delete($revision_id) {
  if ($revision = node_load(NULL, $revision_id)) {
    // Prevent deleting the current revision.
    $node = node_load($revision->nid);
    if ($revision_id == $node->vid) {
      return FALSE;
    }

    db_delete('node_revision')
      ->condition('nid', $revision->nid)
      ->condition('vid', $revision->vid)
      ->execute();
    module_invoke_all('node_revision_delete', $revision);
    field_attach_delete_revision('node', $revision);
    return TRUE;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
