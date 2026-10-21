# SchemaTestCase::testFindTables()

- **Type:** Method
- **File:** [`modules/simpletest/tests/schema.test`](../_file.md), lines 388–439 · [local source](../../../../../../source/modules/simpletest/tests/schema.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test#L388-L439)
- **Class:** [SchemaTestCase](../SchemaTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testFindTables()
```

## Documentation

```text
Tests the findTables() method.
```

## Code

```php
  public function testFindTables() {
    // We will be testing with three tables, two of them using the default
    // prefix and the third one with an individually specified prefix.

    // Set up a new connection with different connection info.
    $connection_info = Database::getConnectionInfo();

    // Add per-table prefix to the second table.
    $new_connection_info = $connection_info['default'];
    $new_connection_info['prefix']['test_2_table'] = $new_connection_info['prefix']['default'] . '_shared_';
    Database::addConnectionInfo('test', 'default', $new_connection_info);

    Database::setActiveConnection('test');

    // Create the tables.
    $table_specification = array(
      'description' => 'Test table.',
      'fields' => array(
        'id'  => array(
          'type' => 'int',
          'default' => NULL,
        ),
      ),
    );
    Database::getConnection()->schema()->createTable('test_1_table', $table_specification);
    Database::getConnection()->schema()->createTable('test_2_table', $table_specification);
    Database::getConnection()->schema()->createTable('the_third_table', $table_specification);

    // Check the "all tables" syntax.
    $tables = Database::getConnection()->schema()->findTablesD8('%');
    sort($tables);
    $expected = array(
      'test_1_table',
      // This table uses a per-table prefix, yet it is returned as un-prefixed.
      'test_2_table',
      'the_third_table',
    );

    $this->assertTrue(!array_diff($expected, $tables), 'All tables were found.');

    // Check the restrictive syntax.
    $tables = Database::getConnection()->schema()->findTablesD8('test_%');
    sort($tables);
    $expected = array(
      'test_1_table',
      'test_2_table',
    );
    $this->assertEqual($tables, $expected, 'Two tables were found.');

    // Go back to the initial connection.
    Database::setActiveConnection('default');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/schema.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test) · Licensed GPL-2.0-or-later (see LICENSE)._
