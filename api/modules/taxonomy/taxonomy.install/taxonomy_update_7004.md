# taxonomy_update_7004()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.install`](_file.md), lines 331–519 · [local source](../../../../source/modules/taxonomy/taxonomy.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install#L331-L519)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_update_7004()
```

## Documentation

```text
Move taxonomy vocabulary associations for nodes to fields and field instances.
```

## Code

```php
function taxonomy_update_7004() {
  $taxonomy_index = array(
    'description' => 'Maintains denormalized information about node/term relationships.',
    'fields' => array(
      'nid' => array(
        'description' => 'The {node}.nid this record tracks.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
      'tid' => array(
         'description' => 'The term ID.',
         'type' => 'int',
         'unsigned' => TRUE,
         'not null' => TRUE,
         'default' => 0,
      ),
      'sticky' => array(
        'description' => 'Boolean indicating whether the node is sticky.',
        'type' => 'int',
        'not null' => FALSE,
        'default' => 0,
        'size' => 'tiny',
      ),
      'created' => array(
        'description' => 'The Unix timestamp when the node was created.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default'=> 0,
      ),
    ),
    'indexes' => array(
      'term_node' => array('tid', 'sticky', 'created'),
      'nid' => array('nid'),
    ),
    'foreign keys' => array(
      'tracked_node' => array(
        'table' => 'node',
        'columns' => array('nid' => 'nid'),
      ),
      'term' => array(
        'table' => 'taxonomy_term_data',
        'columns' => array('tid' => 'tid'),
      ),
    ),
  );
  db_create_table('taxonomy_index', $taxonomy_index);

  // Use an inline version of Drupal 6 taxonomy_get_vocabularies() here since
  // we can no longer rely on $vocabulary->nodes from the API function.
  $result = db_query('SELECT v.*, n.type FROM {taxonomy_vocabulary} v LEFT JOIN {taxonomy_vocabulary_node_type} n ON v.vid = n.vid ORDER BY v.weight, v.name');
  $vocabularies = array();
  foreach ($result as $record) {
    // If no node types are associated with a vocabulary, the LEFT JOIN will
    // return a NULL value for type.
    if (isset($record->type)) {
      $node_types[$record->vid][$record->type] = $record->type;
      unset($record->type);
      $record->nodes = $node_types[$record->vid];
    }
    elseif (!isset($record->nodes)) {
      $record->nodes = array();
    }
    $vocabularies[$record->vid] = $record;
  }

  foreach ($vocabularies as $vocabulary) {
    $field_name = 'taxonomy_' . $vocabulary->machine_name;
    $field = array(
      'field_name' => $field_name,
      'module' => 'taxonomy',
      'type' => 'taxonomy_term_reference',
      'cardinality' => $vocabulary->multiple || $vocabulary->tags ? FIELD_CARDINALITY_UNLIMITED : 1,
      'settings' => array(
        'required' => $vocabulary->required ? TRUE : FALSE,
        'allowed_values' => array(
          array(
            'vocabulary' => $vocabulary->machine_name,
            'parent' => 0,
          ),
        ),
      ),
    );
    _update_7000_field_create_field($field);

    foreach ($vocabulary->nodes as $bundle) {
      $instance = array(
        'label' => $vocabulary->name,
        'field_name' => $field_name,
        'bundle' => $bundle,
        'entity_type' => 'node',
        'settings' => array(),
        'description' => $vocabulary->help,
        'required' => $vocabulary->required,
        'widget' => array(),
        'display' => array(
          'default' => array(
            'type' => 'taxonomy_term_reference_link',
            'weight' => 10,
          ),
          'teaser' => array(
            'type' => 'taxonomy_term_reference_link',
            'weight' => 10,
          ),
        ),
      );
      if ($vocabulary->tags) {
        $instance['widget'] = array(
          'type' => 'taxonomy_autocomplete',
          'module' => 'taxonomy',
          'settings' => array(
            'size' => 60,
            'autocomplete_path' => 'taxonomy/autocomplete',
          ),
        );
      }
      else {
        $instance['widget'] = array(
          'type' => 'options_select',
          'module' => 'options',
          'settings' => array(),
        );
      }
      _update_7000_field_create_instance($field, $instance);
    }
  }

  // Some contrib projects stored term node associations without regard for the
  // selections in the taxonomy_vocabulary_node_types table, or have more terms
  // for a single node than the vocabulary allowed. We construct the
  // taxonomyextra field to store all the extra stuff.

  // Allowed values for this extra vocabs field is every vocabulary.
  $allowed_values = array();
  foreach (_update_7002_taxonomy_get_vocabularies() as $vocabulary) {
    $allowed_values[] = array(
      'vocabulary' => $vocabulary->machine_name,
      'parent' => 0,
    );
  }

  $field_name = 'taxonomyextra';
  $field = array(
    'field_name' => $field_name,
    'module' => 'taxonomy',
    'type' => 'taxonomy_term_reference',
    'cardinality' => FIELD_CARDINALITY_UNLIMITED,
    'settings' => array(
      'required' => FALSE,
      'allowed_values' => $allowed_values,
    ),
  );
  _update_7000_field_create_field($field);

  foreach (_update_7000_node_get_types() as $bundle) {
    $instance = array(
      'label' => 'Taxonomy upgrade extras',
      'field_name' => $field_name,
      'entity_type' => 'node',
      'bundle' => $bundle->type,
      'settings' => array(),
      'description' => 'Debris left over after upgrade from Drupal 6',
      'required' => FALSE,
      'widget' => array(
        'type' => 'taxonomy_autocomplete',
        'module' => 'taxonomy',
        'settings' => array(),
      ),
      'display' => array(
        'default' => array(
          'type' => 'taxonomy_term_reference_link',
          'weight' => 10,
        ),
        'teaser' => array(
          'type' => 'taxonomy_term_reference_link',
          'weight' => 10,
        ),
      ),
    );
    _update_7000_field_create_instance($field, $instance);
  }

  $fields = array('help', 'multiple', 'required', 'tags');
  foreach ($fields as $field) {
    db_drop_field('taxonomy_vocabulary', $field);
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.install](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install) · Licensed GPL-2.0-or-later (see LICENSE)._
