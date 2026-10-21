# SchemaTestCase::testUnsignedColumns()

- **Type:** Method
- **File:** [`modules/simpletest/tests/schema.test`](../_file.md), lines 172–199 · [local source](../../../../../../source/modules/simpletest/tests/schema.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test#L172-L199)
- **Class:** [SchemaTestCase](../SchemaTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testUnsignedColumns()
```

## Documentation

```text
Tests creating unsigned columns and data integrity thereof.
```

## Code

```php
  function testUnsignedColumns() {
    // First create the table with just a serial column.
    $table_name = 'unsigned_table';
    $table_spec = array(
      'fields' => array('serial_column' => array('type' => 'serial', 'unsigned' => TRUE, 'not null' => TRUE)),
      'primary key' => array('serial_column'),
    );
    $ret = array();
    db_create_table($table_name, $table_spec);

    // Now set up columns for the other types.
    $types = array('int', 'float', 'numeric');
    foreach ($types as $type) {
      $column_spec = array('type' => $type, 'unsigned'=> TRUE);
      if ($type == 'numeric') {
        $column_spec += array('precision' => 10, 'scale' => 0);
      }
      $column_name = $type . '_column';
      $table_spec['fields'][$column_name] = $column_spec;
      db_add_field($table_name, $column_name, $column_spec);
    }

    // Finally, check each column and try to insert invalid values into them.
    foreach ($table_spec['fields'] as $column_name => $column_spec) {
      $this->assertTrue(db_field_exists($table_name, $column_name), format_string('Unsigned @type column was created.', array('@type' => $column_spec['type'])));
      $this->assertFalse($this->tryUnsignedInsert($table_name, $column_name), format_string('Unsigned @type column rejected a negative value.', array('@type' => $column_spec['type'])));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/schema.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test) · Licensed GPL-2.0-or-later (see LICENSE)._
