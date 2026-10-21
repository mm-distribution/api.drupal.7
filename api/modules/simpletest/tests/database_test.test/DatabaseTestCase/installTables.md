# DatabaseTestCase::installTables()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 45–57 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L45-L57)
- **Class:** [DatabaseTestCase](../DatabaseTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function installTables($schema)
```

## Documentation

```text
Set up several tables needed by a certain test.

@param $schema
  An array of table definitions to install.
```

## Code

```php
  function installTables($schema) {
    // This ends up being a test for table drop and create, too, which is nice.
    foreach ($schema as $name => $data) {
      if (db_table_exists($name)) {
        db_drop_table($name);
      }
      db_create_table($name, $data);
    }

    foreach ($schema as $name => $data) {
      $this->assertTrue(db_table_exists($name), format_string('Table @name created successfully.', array('@name' => $name)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
