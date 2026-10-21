# taxonomy_update_7005()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.install`](_file.md), lines 527–824 · [local source](../../../../source/modules/taxonomy/taxonomy.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install#L527-L824)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_update_7005(&$sandbox)
```

## Documentation

```text
Migrate {taxonomy_term_node} table to field storage.

@todo: This function can possibly be made much faster by wrapping a
transaction around all the inserts.
```

## Code

```php
function taxonomy_update_7005(&$sandbox) {
  // $sandbox contents:
  // - total: The total number of term_node relationships to migrate.
  // - count: The number of term_node relationships that have been
  //   migrated so far.
  // - last: The db_query_range() offset to use when querying
  //   term_node; this field is incremented in quantities of $batch
  //   (1000) but at the end of each call to this function, last and
  //   count are the same.
  // - vocabularies: An associative array mapping vocabulary id and node
  //   type to field name. If a voc id/node type pair does not appear
  //   in this array but a term_node relationship exists mapping a
  //   term in voc id to node of that type, the relationship is
  //   assigned to the taxonomymyextra field which allows terms of all
  //   vocabularies.
  // - cursor[values], cursor[deltas]: The contents of $values and
  //   $deltas at the end of the previous call to this function. These
  //   need to be preserved across calls because a single batch of
  //   1000 rows from term_node may end in the middle of the terms for
  //   a single node revision.
  //
  // $values is the array of values about to be/most recently inserted
  // into the SQL data table for the taxonomy_term_reference
  // field. Before $values is constructed for each record, the
  // $values from the previous insert is checked to see if the two
  // records are for the same node revision id; this enables knowing
  // when to reset the delta counters which are incremented across all
  // terms for a single field on a single revision, but reset for each
  // new field and revision.
  //
  // $deltas is an associative array mapping field name to the number
  // of term references stored so far for the current revision, which
  // provides the delta value for each term reference data insert. The
  // deltas are reset for each new revision.

  $conditions = array(
    'type' => 'taxonomy_term_reference',
    'deleted' => 0,
  );
  $field_info = _update_7000_field_read_fields($conditions, 'field_name');

  // This is a multi-pass update. On the first call we need to initialize some
  // variables.
  if (!isset($sandbox['total'])) {
    $sandbox['last'] = 0;
    $sandbox['count'] = 0;

    // Run the same joins as the query that is used later to retrieve the
    // term_node data, this ensures that bad records in that table - for
    // tids which aren't in taxonomy_term_data or nids which aren't in {node}
    // are not included in the count.
    $sandbox['total'] = db_query('SELECT COUNT(*) FROM {taxonomy_term_data} td INNER JOIN {taxonomy_term_node} tn ON td.tid = tn.tid INNER JOIN {node} n ON tn.nid = n.nid LEFT JOIN {node} n2 ON tn.vid = n2.vid')->fetchField();

    // Use an inline version of Drupal 6 taxonomy_get_vocabularies() here since
    // we can no longer rely on $vocabulary->nodes from the API function.
    $result = db_query('SELECT v.vid, v.machine_name, n.type FROM {taxonomy_vocabulary} v INNER JOIN {taxonomy_vocabulary_node_type} n ON v.vid = n.vid');
    $vocabularies = array();
    foreach ($result as $record) {

      // If no node types are associated with a vocabulary, the LEFT JOIN will
      // return a NULL value for type.
      if (isset($record->type)) {
        $vocabularies[$record->vid][$record->type] = 'taxonomy_'. $record->machine_name;
      }
    }

    if (!empty($vocabularies)) {
      $sandbox['vocabularies'] = $vocabularies;
    }

    db_create_table('taxonomy_update_7005', array(
      'description' => 'Stores temporary data for taxonomy_update_7005.',
      'fields' => array(
        'n' => array(
          'description' => 'Preserve order.',
          'type' => 'serial',
          'unsigned' => TRUE,
          'not null' => TRUE,
        ),
        'vocab_id' => array(
          'type' => 'int',
          'unsigned' => TRUE,
          'not null' => TRUE,
          'default' => 0,
        ),
        'tid' => array(
          'type' => 'int',
          'unsigned' => TRUE,
          'not null' => TRUE,
        ),
        'nid' => array(
          'type' => 'int',
          'unsigned' => TRUE,
          'not null' => TRUE,
        ),
        'vid' => array(
          'type' => 'int',
          'unsigned' => TRUE,
          'not null' => FALSE,
          'default' => NULL,
        ),
        'type' => array(
          'type' => 'varchar',
          'length' => 32,
          'not null' => TRUE,
          'default' => '',
        ),
        'created' => array(
          'type' => 'int',
          'not null' => FALSE,
        ),
        'sticky' => array(
          'type' => 'int',
          'not null' => FALSE,
        ),
        'status' => array(
          'type' => 'int',
          'not null' => FALSE,
        ),
        'is_current' => array(
          'type' => 'int',
          'unsigned' => TRUE,
          'not null' => FALSE,
        ),
      ),
      'primary key' => array('n'),
    ));

    // Query selects all revisions at once and processes them in revision and
    // term weight order.
    $query = db_select('taxonomy_term_data', 'td');
    // We are migrating term-node relationships. If there are none for a
    // term, we do not need the term_data row.
    $query->join('taxonomy_term_node', 'tn', 'td.tid = tn.tid');
    // If a term-node relationship exists for a nid that does not exist, we
    // cannot migrate it as we have no node to relate it to; thus we do not
    // need that row from term_node.
    $query->join('node', 'n', 'tn.nid = n.nid');
    // If the current term-node relationship is for the current revision of
    // the node, this left join will match and is_current will be non-NULL
    // (we also get the current sticky and created in this case). This
    // tells us whether to insert into the current data tables in addition
    // to the revision data tables.
    $query->leftJoin('node', 'n2', 'tn.vid = n2.vid');
    $query->addField('td', 'vid', 'vocab_id');
    $query->addField('td', 'tid');
    $query->addField('tn', 'nid');
    $query->addField('tn', 'vid');
    $query->addField('n', 'type');
    $query->addField('n2', 'created');
    $query->addField('n2', 'sticky');
    $query->addField('n2', 'status');
    $query->addField('n2', 'nid', 'is_current');
    // This query must return a consistent ordering across multiple calls.
    // We need them ordered by node vid (since we use that to decide when
    // to reset the delta counters) and by term weight so they appear
    // within each node in weight order. However, tn.vid,td.weight is not
    // guaranteed to be unique, so we add tn.tid as an additional sort key
    // because tn.tid,tn.vid is the primary key of the D6 term_node table
    // and so is guaranteed unique. Unfortunately it also happens to be in
    // the wrong order which is less efficient, but c'est la vie.
    $query->orderBy('tn.vid');
    $query->orderBy('td.weight');
    $query->orderBy('tn.tid');

    // Work around a bug in the PostgreSQL driver that would result in fatal
    // errors when this subquery is used in the insert query below. See
    // https://drupal.org/node/2057693.
    $fields = &$query->getFields();
    unset($fields['td.weight']);
    unset($fields['tn.tid']);

    db_insert('taxonomy_update_7005')
      ->from($query)
      ->execute();
  }
  else {
    // We do each pass in batches of 1000.
    $batch = 1000;

    $result = db_query_range('SELECT vocab_id, tid, nid, vid, type, created, sticky, status, is_current FROM {taxonomy_update_7005} ORDER BY n', $sandbox['last'], $batch);
    if (isset($sandbox['cursor'])) {
      $values = $sandbox['cursor']['values'];
      $deltas = $sandbox['cursor']['deltas'];
    }
    else {
      $deltas = array();
    }
    foreach ($result as $record) {
      $sandbox['count'] += 1;

      // Use the valid field for this vocabulary and node type or use the
      // overflow vocabulary if there is no valid field.
      $field_name = isset($sandbox['vocabularies'][$record->vocab_id][$record->type]) ? $sandbox['vocabularies'][$record->vocab_id][$record->type] : 'taxonomyextra';
      $field = $field_info[$field_name];

      // Start deltas from 0, and increment by one for each term attached to a
      // node.
      if (!isset($deltas[$field_name])) {
        $deltas[$field_name] = 0;
      }

      if (isset($values)) {

        // If the last inserted revision_id is the same as the current record,
        // use the previous deltas to calculate the next delta.
        if ($record->vid == $values[2]) {

          // For limited cardinality fields, the delta must not be allowed to
          // exceed the cardinality during the update. So ensure that the
          // delta about to be inserted is within this limit.
          // @see field_default_validate().
          if ($field['cardinality'] != FIELD_CARDINALITY_UNLIMITED && ($deltas[$field_name] + 1) > $field['cardinality']) {

            // For excess values of a single-term vocabulary, switch over to
            // the overflow field.
            $field_name = 'taxonomyextra';
            $field = $field_info[$field_name];
            if (!isset($deltas[$field_name])) {
              $deltas[$field_name] = 0;
            }
          }
        }
        else {

          // When the record is a new revision, empty the deltas array.
          $deltas = array($field_name => 0);
        }
      }

      // Table and column found in the field's storage details. During upgrades,
      // it's always SQL.
      $table_name = "field_data_{$field_name}";
      $revision_name = "field_revision_{$field_name}";
      $value_column = $field_name . '_tid';

      // Column names and values in field storage are the same for current and
      // revision.
      $columns = array('entity_type', 'entity_id', 'revision_id', 'bundle', 'language', 'delta', $value_column);
      $values = array('node', $record->nid, $record->vid, $record->type, LANGUAGE_NONE, $deltas[$field_name]++, $record->tid);

      // Insert rows into the revision table.
      db_insert($revision_name)->fields($columns)->values($values)->execute();

      // is_current column is a node ID if this revision is also current.
      if ($record->is_current) {
        db_insert($table_name)->fields($columns)->values($values)->execute();
        // Only insert a record in the taxonomy index if the node is published.
        if ($record->status) {
          // Update the {taxonomy_index} table.
          db_insert('taxonomy_index')
            ->fields(array('nid', 'tid', 'sticky', 'created',))
            ->values(array($record->nid, $record->tid, $record->sticky, $record->created))
            ->execute();
        }
      }
    }

    // Store the set of inserted values and the current revision's deltas in the
    // sandbox.
    $sandbox['cursor'] = array(
      'values' => $values,
      'deltas' => $deltas,
    );
    $sandbox['last'] += $batch;
  }

  if ($sandbox['count'] < $sandbox['total']) {
    $sandbox['#finished'] = FALSE;
  }
  else {
    db_drop_table('taxonomy_vocabulary_node_type');
    db_drop_table('taxonomy_term_node');

    // If there are no vocabs, we're done.
    db_drop_table('taxonomy_update_7005');
    $sandbox['#finished'] = TRUE;

    // Determine necessity of taxonomyextras field.
    $field = $field_info['taxonomyextra'];
    $revision_name = 'field_revision_' . $field['field_name'];
    $node_types = db_select($revision_name)->distinct()->fields($revision_name, array('bundle'))
      ->execute()->fetchCol();

    if (empty($node_types)) {
      // Delete the overflow field if there are no rows in the revision table.
      _update_7000_field_delete_field('taxonomyextra');
    }
    else {
      // Remove instances which are not actually used.
      $bundles = db_query('SELECT bundle FROM {field_config_instance} WHERE field_name = :field_name', array(':field_name' => 'taxonomyextra'))->fetchCol();
      $bundles = array_diff($bundles, $node_types);
      foreach ($bundles as $bundle) {
        _update_7000_field_delete_instance('taxonomyextra', 'node', $bundle);
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.install](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install) · Licensed GPL-2.0-or-later (see LICENSE)._
