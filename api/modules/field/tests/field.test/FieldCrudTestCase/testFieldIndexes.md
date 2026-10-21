# FieldCrudTestCase::testFieldIndexes()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2598–2636 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2598-L2636)
- **Class:** [FieldCrudTestCase](../FieldCrudTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldIndexes()
```

## Documentation

```text
Test creation of indexes on data column.
```

## Code

```php
  function testFieldIndexes() {
    // Check that indexes specified by the field type are used by default.
    $field_definition = array(
      'field_name' => 'field_1',
      'type' => 'test_field',
    );
    field_create_field($field_definition);
    $field = field_read_field($field_definition['field_name']);
    $expected_indexes = array('value' => array('value'));
    $this->assertEqual($field['indexes'], $expected_indexes, 'Field type indexes saved by default');

    // Check that indexes specified by the field definition override the field
    // type indexes.
    $field_definition = array(
      'field_name' => 'field_2',
      'type' => 'test_field',
      'indexes' => array(
        'value' => array(),
      ),
    );
    field_create_field($field_definition);
    $field = field_read_field($field_definition['field_name']);
    $expected_indexes = array('value' => array());
    $this->assertEqual($field['indexes'], $expected_indexes, 'Field definition indexes override field type indexes');

    // Check that indexes specified by the field definition add to the field
    // type indexes.
    $field_definition = array(
      'field_name' => 'field_3',
      'type' => 'test_field',
      'indexes' => array(
        'value_2' => array('value'),
      ),
    );
    field_create_field($field_definition);
    $field = field_read_field($field_definition['field_name']);
    $expected_indexes = array('value' => array('value'), 'value_2' => array('value'));
    $this->assertEqual($field['indexes'], $expected_indexes, 'Field definition indexes are merged with field type indexes');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
