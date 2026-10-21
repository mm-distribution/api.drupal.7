# node_query_node_access_alter()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3296–3298 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3296-L3298)
- **Module/theme:** node
- **Topics:** [node_access](../../../topics/node_access.md)
- **Implements:** [hook_query_TAG_alter()](../../system/system.api.php/hook_query_TAG_alter.md)

## Signature

```php
function node_query_node_access_alter(QueryAlterableInterface $query)
```

## Documentation

```text
Implements hook_query_TAG_alter().

This is the hook_query_alter() for queries tagged with 'node_access'. It adds
node access checks for the user account given by the 'account' meta-data (or
global $user if not provided), for an operation given by the 'op' meta-data
(or 'view' if not provided; other possible values are 'update' and 'delete').
```

## Code

```php
function node_query_node_access_alter(QueryAlterableInterface $query) {
  _node_query_node_access_alter($query, 'node');
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
