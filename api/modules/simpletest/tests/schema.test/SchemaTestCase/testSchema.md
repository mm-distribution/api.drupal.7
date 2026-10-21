# SchemaTestCase::testSchema()

- **Type:** Method
- **File:** [`modules/simpletest/tests/schema.test`](../_file.md), lines 28–138 · [local source](../../../../../../source/modules/simpletest/tests/schema.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test#L28-L138)
- **Class:** [SchemaTestCase](../SchemaTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSchema()
```

## Documentation

_No docblock in source._

## Code

```php
  function testSchema() {
    // Try creating a table.
    $table_specification = array(
      'description' => 'Schema table description.',
      'fields' => array(
        'id'  => array(
          'type' => 'int',
          'default' => NULL,
        ),
        'test_field'  => array(
          'type' => 'int',
          'not null' => TRUE,
          'description' => 'Schema column description.',
        ),
      ),
    );
    db_create_table('test_table', $table_specification);

    // Assert that the table exists.
    $this->assertTrue(db_table_exists('test_table'), 'The table exists.');

    // Assert that the table comment has been set.
    $this->checkSchemaComment($table_specification['description'], 'test_table');

    // Assert that the column comment has been set.
    $this->checkSchemaComment($table_specification['fields']['test_field']['description'], 'test_table', 'test_field');

    // An insert without a value for the column 'test_table' should fail.
    $this->assertFalse($this->tryInsert(), 'Insert without a default failed.');

    // Add a default value to the column.
    db_field_set_default('test_table', 'test_field', 0);
    // The insert should now succeed.
    $this->assertTrue($this->tryInsert(), 'Insert with a default succeeded.');

    // Remove the default.
    db_field_set_no_default('test_table', 'test_field');
    // The insert should fail again.
    $this->assertFalse($this->tryInsert(), 'Insert without a default failed.');

    // Test for fake index and test for the boolean result of indexExists().
    $index_exists = Database::getConnection()->schema()->indexExists('test_table', 'test_field');
    $this->assertIdentical($index_exists, FALSE, 'Fake index does not exists');
    // Add index.
    db_add_index('test_table', 'test_field', array('test_field'));
    // Test for created index and test for the boolean result of indexExists().
    $index_exists = Database::getConnection()->schema()->indexExists('test_table', 'test_field');
    $this->assertIdentical($index_exists, TRUE, 'Index created.');

    // Rename the table.
    db_rename_table('test_table', 'test_table2');

    // Index should be renamed.
    $index_exists = Database::getConnection()->schema()->indexExists('test_table2', 'test_field');
    $this->assertTrue($index_exists, 'Index was renamed.');

    // We need the default so that we can insert after the rename.
    db_field_set_default('test_table2', 'test_field', 0);
    $this->assertFalse($this->tryInsert(), 'Insert into the old table failed.');
    $this->assertTrue($this->tryInsert('test_table2'), 'Insert into the new table succeeded.');

    // We should have successfully inserted exactly two rows.
    $count = db_query('SELECT COUNT(*) FROM {test_table2}')->fetchField();
    $this->assertEqual($count, 2, 'Two fields were successfully inserted.');

    // Try to drop the table.
    db_drop_table('test_table2');
    $this->assertFalse(db_table_exists('test_table2'), 'The dropped table does not exist.');

    // Recreate the table.
    db_create_table('test_table', $table_specification);
    db_field_set_default('test_table', 'test_field', 0);
    db_add_field('test_table', 'test_serial', array('type' => 'int', 'not null' => TRUE, 'default' => 0, 'description' => 'Added column description.'));

    // Assert that the column comment has been set.
    $this->checkSchemaComment('Added column description.', 'test_table', 'test_serial');

    // Change the new field to a serial column.
    db_change_field('test_table', 'test_serial', 'test_serial', array('type' => 'serial', 'not null' => TRUE, 'description' => 'Changed column description.'), array('primary key' => array('test_serial')));

    // Assert that the column comment has been set.
    $this->checkSchemaComment('Changed column description.', 'test_table', 'test_serial');

    $this->assertTrue($this->tryInsert(), 'Insert with a serial succeeded.');
    $max1 = db_query('SELECT MAX(test_serial) FROM {test_table}')->fetchField();
    $this->assertTrue($this->tryInsert(), 'Insert with a serial succeeded.');
    $max2 = db_query('SELECT MAX(test_serial) FROM {test_table}')->fetchField();
    $this->assertTrue($max2 > $max1, 'The serial is monotone.');

    $count = db_query('SELECT COUNT(*) FROM {test_table}')->fetchField();
    $this->assertEqual($count, 2, 'There were two rows.');

    // Use database specific data type and ensure that table is created.
    $table_specification = array(
      'description' => 'Schema table description.',
      'fields' => array(
        'timestamp'  => array(
          'mysql_type' => 'timestamp',
          'pgsql_type' => 'timestamp',
          'sqlite_type' => 'datetime',
          'not null' => FALSE,
          'default' => NULL,
        ),
      ),
    );
    try {
      db_create_table('test_timestamp', $table_specification);
    }
    catch (Exception $e) {}
    $this->assertTrue(db_table_exists('test_timestamp'), 'Table with database specific datatype was created.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/schema.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test) · Licensed GPL-2.0-or-later (see LICENSE)._
