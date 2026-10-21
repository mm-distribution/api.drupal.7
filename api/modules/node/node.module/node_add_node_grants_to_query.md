# node_add_node_grants_to_query()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3092–3104 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3092-L3104)
- **Module/theme:** node
- **Topics:** [node_access](../../../topics/node_access.md)

## Signature

```php
function node_add_node_grants_to_query($node_access_grants, $table_alias = '')
```

## Documentation

```text
Helper function to create the or condition for a node grants check.

@param $account
  The grants to add to the query, usually gotten via node_access_grants().
@param $table_alias
  Optional, the alias to the node access table.

@return
  TRUE if the operation may be performed, FALSE otherwise.
```

## Code

```php
function node_add_node_grants_to_query($node_access_grants, $table_alias = '') {
  $grants = db_or();
  $prefix = $table_alias ? $table_alias . '.' : '';
  foreach ($node_access_grants as $realm => $gids) {
    if (!empty($gids)) {
      $grants->condition(db_and()
        ->condition($prefix . 'gid', $gids, 'IN')
        ->condition($prefix . 'realm', $realm)
      );
    }
  }
  return $grants;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
