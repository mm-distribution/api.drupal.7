# node_query_entity_field_access_alter()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3307–3309 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3307-L3309)
- **Module/theme:** node
- **Topics:** [node_access](../../../topics/node_access.md)
- **Implements:** [hook_query_TAG_alter()](../../system/system.api.php/hook_query_TAG_alter.md)

## Signature

```php
function node_query_entity_field_access_alter(QueryAlterableInterface $query)
```

## Documentation

```text
Implements hook_query_TAG_alter().

This function implements the same functionality as
node_query_node_access_alter() for the SQL field storage engine. Node access
conditions are added for field values belonging to nodes only.
```

## Code

```php
function node_query_entity_field_access_alter(QueryAlterableInterface $query) {
  _node_query_node_access_alter($query, 'entity');
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
