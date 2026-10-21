# taxonomy_select_nodes()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 204–236 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L204-L236)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_select_nodes($tid, $pager = TRUE, $limit = FALSE, $order = array('t.sticky' => 'DESC', 't.created' => 'DESC'))
```

## Documentation

```text
Return nodes attached to a term across all field instances.

This function requires taxonomy module to be maintaining its own tables,
and will return an empty array if it is not. If using other field storage
methods alternatives methods for listing terms will need to be used.

@param $tid
  The term ID.
@param $pager
  Boolean to indicate whether a pager should be used.
@param $limit
  Integer. The maximum number of nodes to find.
  Set to FALSE for no limit.
@param $order
  An array of fields and directions.

@return
  An array of nids matching the query.
```

## Code

```php
function taxonomy_select_nodes($tid, $pager = TRUE, $limit = FALSE, $order = array('t.sticky' => 'DESC', 't.created' => 'DESC')) {
  if (!variable_get('taxonomy_maintain_index_table', TRUE)) {
    return array();
  }
  $query = db_select('taxonomy_index', 't');
  $query->addTag('node_access');
  $query->condition('t.tid', $tid);
  if ($pager) {
    $count_query = clone $query;
    $count_query->addExpression('COUNT(t.nid)');

    $query = $query->extend('PagerDefault');
    if ($limit !== FALSE) {
      $query = $query->limit($limit);
    }
    $query->setCountQuery($count_query);
  }
  else {
    if ($limit !== FALSE) {
      $query->range(0, $limit);
    }
  }
  $query->addField('t', 'nid');
  $query->addField('t', 'tid');
  foreach ($order as $field => $direction) {
    $query->orderBy($field, $direction);
    // ORDER BY fields need to be loaded too, assume they are in the form
    // table_alias.name
    list($table_alias, $name) = explode('.', $field);
    $query->addField($table_alias, $name);
  }
  return $query->execute()->fetchCol();
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
