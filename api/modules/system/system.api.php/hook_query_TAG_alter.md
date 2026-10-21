# hook_query_TAG_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3335–3366 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3335-L3366)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_query_TAG_alter(QueryAlterableInterface $query)
```

## Documentation

```text
Perform alterations to a structured query for a given tag.

@param $query
  An Query object describing the composite parts of a SQL query.

@see hook_query_alter()
@see node_query_node_access_alter()
@see QueryAlterableInterface
@see SelectQueryInterface
```

## Code

```php
function hook_query_TAG_alter(QueryAlterableInterface $query) {
  // Skip the extra expensive alterations if site has no node access control modules.
  if (!node_access_view_all_nodes()) {
    // Prevent duplicates records.
    $query->distinct();
    // The recognized operations are 'view', 'update', 'delete'.
    if (!$op = $query->getMetaData('op')) {
      $op = 'view';
    }
    // Skip the extra joins and conditions for node admins.
    if (!user_access('bypass node access')) {
      // The node_access table has the access grants for any given node.
      $access_alias = $query->join('node_access', 'na', '%alias.nid = n.nid');
      $or = db_or();
      // If any grant exists for the specified user, then user has access to the node for the specified operation.
      foreach (node_access_grants($op, $query->getMetaData('account')) as $realm => $gids) {
        foreach ($gids as $gid) {
          $or->condition(db_and()
            ->condition($access_alias . '.gid', $gid)
            ->condition($access_alias . '.realm', $realm)
          );
        }
      }

      if (count($or->conditions())) {
        $query->condition($or);
      }

      $query->condition($access_alias . 'grant_' . $op, 1, '>=');
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_query_TAG_alter()".

- [database_test_query_database_test_alter_remove_range_alter()](../../simpletest/tests/database_test.module/database_test_query_database_test_alter_remove_range_alter.md) — `modules/simpletest/tests/database_test.module`
- [taxonomy_nodes_test_query_node_access_alter()](../../simpletest/tests/taxonomy_nodes_test.module/taxonomy_nodes_test_query_node_access_alter.md) — `modules/simpletest/tests/taxonomy_nodes_test.module`
- [taxonomy_test_query_taxonomy_term_access_alter()](../../simpletest/tests/taxonomy_test.module/taxonomy_test_query_taxonomy_term_access_alter.md) — `modules/simpletest/tests/taxonomy_test.module`
- [taxonomy_test_query_term_access_alter()](../../simpletest/tests/taxonomy_test.module/taxonomy_test_query_term_access_alter.md) — `modules/simpletest/tests/taxonomy_test.module`
- [field_test_query_efq_table_prefixing_test_alter()](../../field/tests/field_test.module/field_test_query_efq_table_prefixing_test_alter.md) — `modules/field/tests/field_test.module`
- [field_test_query_store_global_test_query_alter()](../../field/tests/field_test.module/field_test_query_store_global_test_query_alter.md) — `modules/field/tests/field_test.module`
- [node_query_entity_field_access_alter()](../../node/node.module/node_query_entity_field_access_alter.md) — `modules/node/node.module`
- [node_query_node_access_alter()](../../node/node.module/node_query_node_access_alter.md) — `modules/node/node.module`
- [search_node_tags_query_search_node_alter()](../../search/tests/search_node_tags.module/search_node_tags_query_search_node_alter.md) — `modules/search/tests/search_node_tags.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
