# SchemaTestCase::assertFieldAdditionRemoval()

- **Type:** Method
- **File:** [`modules/simpletest/tests/schema.test`](../_file.md), lines 304–350 · [local source](../../../../../../source/modules/simpletest/tests/schema.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test#L304-L350)
- **Class:** [SchemaTestCase](../SchemaTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function assertFieldAdditionRemoval($field_spec)
```

## Documentation

```text
Assert that a given field can be added and removed from a table.

The addition test covers both defining a field of a given specification
when initially creating at table and extending an existing table.

@param $field_spec
  The schema specification of the field.
```

## Code

```php
  protected function assertFieldAdditionRemoval($field_spec) {
    // Try creating the field on a new table.
    $table_name = 'test_table_' . ($this->counter++);
    $table_spec = array(
      'fields' => array(
        'serial_column' => array('type' => 'serial', 'unsigned' => TRUE, 'not null' => TRUE),
        'test_field' => $field_spec,
      ),
      'primary key' => array('serial_column'),
    );
    db_create_table($table_name, $table_spec);
    $this->pass(format_string('Table %table created.', array('%table' => $table_name)));

    // Check the characteristics of the field.
    $this->assertFieldCharacteristics($table_name, 'test_field', $field_spec);

    // Clean-up.
    db_drop_table($table_name);

    // Try adding a field to an existing table.
    $table_name = 'test_table_' . ($this->counter++);
    $table_spec = array(
      'fields' => array(
        'serial_column' => array('type' => 'serial', 'unsigned' => TRUE, 'not null' => TRUE),
      ),
      'primary key' => array('serial_column'),
    );
    db_create_table($table_name, $table_spec);
    $this->pass(format_string('Table %table created.', array('%table' => $table_name)));

    // Insert some rows to the table to test the handling of initial values.
    for ($i = 0; $i < 3; $i++) {
      db_insert($table_name)
        ->useDefaults(array('serial_column'))
        ->execute();
    }

    db_add_field($table_name, 'test_field', $field_spec);
    $this->pass(format_string('Column %column created.', array('%column' => 'test_field')));

    // Check the characteristics of the field.
    $this->assertFieldCharacteristics($table_name, 'test_field', $field_spec);

    // Clean-up.
    db_drop_field($table_name, 'test_field');
    db_drop_table($table_name);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/schema.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test) · Licensed GPL-2.0-or-later (see LICENSE)._
