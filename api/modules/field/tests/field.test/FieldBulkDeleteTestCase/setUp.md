# FieldBulkDeleteTestCase::setUp()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3584–3634 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3584-L3634)
- **Class:** [FieldBulkDeleteTestCase](../FieldBulkDeleteTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('field_test');

    $this->fields = array();
    $this->instances = array();
    $this->entities = array();
    $this->entities_by_bundles = array();

    // Create two bundles.
    $this->bundles = array('bb_1' => 'bb_1', 'bb_2' => 'bb_2');
    foreach ($this->bundles as $name => $desc) {
      field_test_create_bundle($name, $desc);
    }

    // Create two fields.
    $field = array('field_name' => 'bf_1', 'type' => 'test_field', 'cardinality' => 1);
    $this->fields[] = field_create_field($field);
    $field = array('field_name' => 'bf_2', 'type' => 'test_field', 'cardinality' => 4);
    $this->fields[] = field_create_field($field);

    // For each bundle, create an instance of each field, and 10
    // entities with values for each field.
    $id = 0;
    $this->entity_type = 'test_entity';
    foreach ($this->bundles as $bundle) {
      foreach ($this->fields as $field) {
        $instance = array(
          'field_name' => $field['field_name'],
          'entity_type' => $this->entity_type,
          'bundle' => $bundle,
          'widget' => array(
            'type' => 'test_field_widget',
          )
        );
        $this->instances[] = field_create_instance($instance);
      }

      for ($i = 0; $i < 10; $i++) {
        $entity = field_test_create_stub_entity($id, $id, $bundle);
        foreach ($this->fields as $field) {
          $entity->{$field['field_name']}[LANGUAGE_NONE] = $this->_generateTestFieldValues($field['cardinality']);
        }

        $this->entities[$id] = $entity;
        // Also keep track of the entities per bundle.
        $this->entities_by_bundles[$bundle][$id] = $entity;
        field_attach_insert($this->entity_type, $entity);
        $id++;
      }
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
