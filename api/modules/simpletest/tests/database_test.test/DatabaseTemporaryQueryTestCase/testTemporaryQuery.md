# DatabaseTemporaryQueryTestCase::testTemporaryQuery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3345–3371 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3345-L3371)
- **Class:** [DatabaseTemporaryQueryTestCase](../DatabaseTemporaryQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testTemporaryQuery()
```

## Documentation

```text
Confirm that temporary tables work and are limited to one request.
```

## Code

```php
  function testTemporaryQuery() {
    $this->drupalGet('database_test/db_query_temporary');
    $data = json_decode($this->drupalGetContent());
    if ($data) {
      $this->assertEqual($this->countTableRows("system"), $data->row_count, 'The temporary table contains the correct amount of rows.');
      $this->assertFalse(db_table_exists($data->table_name), 'The temporary table is, indeed, temporary.');
    }
    else {
      $this->fail("The creation of the temporary table failed.");
    }

    // Now try to run two db_query_temporary() in the same request.
    $table_name_system = db_query_temporary('SELECT status FROM {system}', array());
    $table_name_users = db_query_temporary('SELECT uid FROM {users}', array());

    $this->assertEqual($this->countTableRows($table_name_system), $this->countTableRows("system"), 'A temporary table was created successfully in this request.');
    $this->assertEqual($this->countTableRows($table_name_users), $this->countTableRows("users"), 'A second temporary table was created successfully in this request.');

    // Check that leading whitespace and comments do not cause problems
    // in the modified query.
    $sql = "
      -- Let's select some rows into a temporary table
      SELECT name FROM {test}
    ";
    $table_name_test = db_query_temporary($sql, array());
    $this->assertEqual($this->countTableRows($table_name_test), $this->countTableRows('test'), 'Leading white space and comments do not interfere with temporary table creation.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
