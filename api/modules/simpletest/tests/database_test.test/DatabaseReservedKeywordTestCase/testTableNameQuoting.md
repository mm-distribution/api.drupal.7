# DatabaseReservedKeywordTestCase::testTableNameQuoting()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4513–4539 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4513-L4539)
- **Class:** [DatabaseReservedKeywordTestCase](../DatabaseReservedKeywordTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testTableNameQuoting()
```

## Documentation

_No docblock in source._

## Code

```php
  public function testTableNameQuoting() {
    // Test db_query with {table} pattern.
    $record = db_query('SELECT * FROM {system} LIMIT 1')->fetchObject();
    $this->assertTrue(isset($record->filename), 'Successfully queried the {system} table.');

    $connection = Database::getConnection()->getConnectionOptions();
    if ($connection['driver'] === 'sqlite') {
      // In SQLite simpletest's prefixed db tables exist in their own schema
      // (e.g. simpletest124904.system), so we cannot test the schema.{table}
      // syntax here as the table name will have the schema name prepended to it
      // when prefixes are processed.
      $this->assert(TRUE, 'Skipping schema.{system} test for SQLite.');
    }
    else {
      $database = $connection['database'];

      if ($connection['driver'] === 'pgsql') {
        // database.scheme.table for PostgreSQL
        // @see https://www.postgresql.org/docs/14/ddl-schemas.html
        $database .= '.public';
      }

      // Test db_query with schema.{table} pattern
      db_query('SELECT * FROM ' . $database . '.{system} LIMIT 1')->fetchObject();
      $this->assertTrue(isset($record->filename), 'Successfully queried the schema.{system} table.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
