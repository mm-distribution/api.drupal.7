# DatabaseTablePrefixTestCase::testSchemaDotTablePrefixes()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4644–4682 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4644-L4682)
- **Class:** [DatabaseTablePrefixTestCase](../DatabaseTablePrefixTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testSchemaDotTablePrefixes()
```

## Documentation

_No docblock in source._

## Code

```php
  public function testSchemaDotTablePrefixes() {
    // Get a copy of the default connection options.
    $db = Database::getConnection('default', 'default');
    $connection_options = $db->getConnectionOptions();

    if ($connection_options['driver'] === 'sqlite') {
      // In SQLite simpletest's prefixed db tables exist in their own schema
      // (e.g. simpletest124904.system), so we cannot test the schema.table
      // prefix syntax here.
      $this->assert(TRUE, 'Skipping schema.table prefixed tables test for SQLite.');
      return;
    }

    $db_name = $connection_options['database'];

    if ($connection_options['driver'] === 'pgsql') {
      // database.scheme.table for PostgreSQL
      // @see https://www.postgresql.org/docs/14/ddl-schemas.html
      $db_name .= '.public';
    }

    // This prefix is usually something like simpletest12345
    $test_prefix = $connection_options['prefix']['default'];

    // Set up a new connection with table prefixes in the form "schema.table"
    $prefixed = $connection_options;
    $prefixed['prefix'] = array(
      'default' => $test_prefix,
      'users' => $db_name . '.' . $test_prefix,
      'role' => $db_name . '.' . $test_prefix,
    );
    Database::addConnectionInfo('default', 'prefixed', $prefixed);

    // Test that the prefixed database connection can query the prefixed tables.
    $num_users_prefixed = Database::getConnection('prefixed', 'default')->query('SELECT COUNT(1) FROM {users}')->fetchField();
    $this->assertTrue((int) $num_users_prefixed > 0, 'Successfully queried the users table using a schema.table prefix');
    $num_users_default = Database::getConnection('default', 'default')->query('SELECT COUNT(1) FROM {users}')->fetchField();
    $this->assertEqual($num_users_default, $num_users_prefixed, 'Verified results of query using a connection with schema.table prefixed tables');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
