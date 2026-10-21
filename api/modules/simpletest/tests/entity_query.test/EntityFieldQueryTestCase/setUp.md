# EntityFieldQueryTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_query.test`](../_file.md), lines 25–163 · [local source](../../../../../../source/modules/simpletest/tests/entity_query.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test#L25-L163)
- **Class:** [EntityFieldQueryTestCase](../EntityFieldQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp(array('node', 'field_test', 'entity_query_access_test', 'node_access_test'));

    field_test_create_bundle('bundle1');
    field_test_create_bundle('bundle2');
    field_test_create_bundle('test_bundle');
    field_test_create_bundle('test_entity_bundle');

    $instances = array();
    $this->fields = array();
    $this->field_names[0] = $field_name = drupal_strtolower($this->randomName() . '_field_name');
    $field = array('field_name' => $field_name, 'type' => 'test_field', 'cardinality' => 4);
    $field = field_create_field($field);
    $this->fields[0] = $field;
    $instance = array(
      'field_name' => $field_name,
      'entity_type' => '',
      'bundle' => '',
      'label' => $this->randomName() . '_label',
      'description' => $this->randomName() . '_description',
      'weight' => mt_rand(0, 127),
      'settings' => array(
        'test_instance_setting' => $this->randomName(),
      ),
      'widget' => array(
        'type' => 'test_field_widget',
        'label' => 'Test Field',
        'settings' => array(
          'test_widget_setting' => $this->randomName(),
        )
      )
    );

    $instances[0] = $instance;

    // Add an instance to that bundle.
    $instances[0]['bundle'] = 'bundle1';
    $instances[0]['entity_type'] = 'test_entity_bundle_key';
    field_create_instance($instances[0]);
    $instances[0]['bundle'] = 'bundle2';
    field_create_instance($instances[0]);
    $instances[0]['bundle'] = $instances[0]['entity_type'] = 'test_entity_bundle';
    field_create_instance($instances[0]);

    $this->field_names[1] = $field_name = drupal_strtolower($this->randomName() . '_field_name');
    $field = array('field_name' => $field_name, 'type' => 'shape', 'cardinality' => 4);
    $field = field_create_field($field);
    $this->fields[1] = $field;
    $instance = array(
      'field_name' => $field_name,
      'entity_type' => '',
      'bundle' => '',
      'label' => $this->randomName() . '_label',
      'description' => $this->randomName() . '_description',
      'weight' => mt_rand(0, 127),
      'settings' => array(
        'test_instance_setting' => $this->randomName(),
      ),
      'widget' => array(
        'type' => 'test_field_widget',
        'label' => 'Test Field',
        'settings' => array(
          'test_widget_setting' => $this->randomName(),
        )
      )
    );

    $instances[1] = $instance;

    // Add a field instance to the bundles.
    $instances[1]['bundle'] = 'bundle1';
    $instances[1]['entity_type'] = 'test_entity_bundle_key';
    field_create_instance($instances[1]);
    $instances[1]['bundle'] = $instances[1]['entity_type'] = 'test_entity_bundle';
    field_create_instance($instances[1]);

    $this->instances = $instances;
    // Write entity base table if there is one.
    $entities = array();

    // Create entities which have a 'bundle key' defined.
    for ($i = 1; $i < 7; $i++) {
      $entity = new stdClass();
      $entity->ftid = $i;
      $entity->fttype = ($i < 5) ? 'bundle1' : 'bundle2';

      $entity->{$this->field_names[0]}[LANGUAGE_NONE][0]['value'] = $i;
      drupal_write_record('test_entity_bundle_key', $entity);
      field_attach_insert('test_entity_bundle_key', $entity);
    }

    $entity = new stdClass();
    $entity->ftid = 5;
    $entity->fttype = 'test_entity_bundle';
    $entity->{$this->field_names[1]}[LANGUAGE_NONE][0]['shape'] = 'square';
    $entity->{$this->field_names[1]}[LANGUAGE_NONE][0]['color'] = 'red';
    $entity->{$this->field_names[1]}[LANGUAGE_NONE][1]['shape'] = 'circle';
    $entity->{$this->field_names[1]}[LANGUAGE_NONE][1]['color'] = 'blue';
    drupal_write_record('test_entity_bundle', $entity);
    field_attach_insert('test_entity_bundle', $entity);

    $instances[2] = $instance;
    $instances[2]['bundle'] = 'test_bundle';
    $instances[2]['field_name'] = $this->field_names[0];
    $instances[2]['entity_type'] = 'test_entity';
    field_create_instance($instances[2]);

    // Create entities with support for revisions.
    for ($i = 1; $i < 5; $i++) {
      $entity = new stdClass();
      $entity->ftid = $i;
      $entity->ftvid = $i;
      $entity->fttype = 'test_bundle';
      $entity->{$this->field_names[0]}[LANGUAGE_NONE][0]['value'] = $i;

      drupal_write_record('test_entity', $entity);
      field_attach_insert('test_entity', $entity);
      drupal_write_record('test_entity_revision', $entity);
    }

    // Add two revisions to an entity.
    for ($i = 100; $i < 102; $i++) {
      $entity = new stdClass();
      $entity->ftid = 4;
      $entity->ftvid = $i;
      $entity->fttype = 'test_bundle';
      $entity->{$this->field_names[0]}[LANGUAGE_NONE][0]['value'] = $i;

      drupal_write_record('test_entity', $entity, 'ftid');
      drupal_write_record('test_entity_revision', $entity);

      db_update('test_entity')
       ->fields(array('ftvid' => $entity->ftvid))
       ->condition('ftid', $entity->ftid)
       ->execute();

      field_attach_update('test_entity', $entity);
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_query.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test) · Licensed GPL-2.0-or-later (see LICENSE)._
