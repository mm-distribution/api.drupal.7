# taxonomy_build_node_index()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1930–1988 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1930-L1988)
- **Module/theme:** taxonomy
- **Topics:** [taxonomy_index](../../../topics/taxonomy_index.md)

## Signature

```php
function taxonomy_build_node_index($node)
```

## Documentation

```text
Builds and inserts taxonomy index entries for a given node.

The index lists all terms that are related to a given node entity, and is
therefore maintained at the entity level.

@param $node
  The node object.
```

## Code

```php
function taxonomy_build_node_index($node) {
  // We maintain a denormalized table of term/node relationships, containing
  // only data for current, published nodes.
  $status = NULL;
  if (variable_get('taxonomy_maintain_index_table', TRUE)) {
    // If a node property is not set in the node object when node_save() is
    // called, the old value from $node->original is used.
    if (!empty($node->original)) {
      $status = (int)(!empty($node->status) || (!isset($node->status) && !empty($node->original->status)));
      $sticky = (int)(!empty($node->sticky) || (!isset($node->sticky) && !empty($node->original->sticky)));
    }
    else {
      $status = (int)(!empty($node->status));
      $sticky = (int)(!empty($node->sticky));
    }
  }
  // We only maintain the taxonomy index for published nodes.
  if ($status) {
    // Collect a unique list of all the term IDs from all node fields.
    $tid_all = array();
    foreach (field_info_instances('node', $node->type) as $instance) {
      $field_name = $instance['field_name'];
      $field = field_info_field($field_name);
      if ($field['module'] == 'taxonomy' && $field['storage']['type'] == 'field_sql_storage') {
        // If a field value is not set in the node object when node_save() is
        // called, the old value from $node->original is used.
        if (isset($node->{$field_name})) {
          $items = $node->{$field_name};
        }
        elseif (isset($node->original->{$field_name})) {
          $items = $node->original->{$field_name};
        }
        else {
          continue;
        }
        foreach (field_available_languages('node', $field) as $langcode) {
          if (!empty($items[$langcode])) {
            foreach ($items[$langcode] as $item) {
              $tid_all[$item['tid']] = $item['tid'];
            }
          }
        }
      }
    }
    // Insert index entries for all the node's terms.
    if (!empty($tid_all)) {
      $query = db_insert('taxonomy_index')->fields(array('nid', 'tid', 'sticky', 'created'));
      foreach ($tid_all as $tid) {
        $query->values(array(
          'nid' => $node->nid,
          'tid' => $tid,
          'sticky' => $sticky,
          'created' => $node->created,
        ));
      }
      $query->execute();
    }
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
