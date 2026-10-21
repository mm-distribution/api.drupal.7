# database_test_schema()

- **Type:** Function
- **File:** [`modules/simpletest/tests/database_test.install`](_file.md), lines 16–300 · [local source](../../../../../source/modules/simpletest/tests/database_test.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.install#L16-L300)
- **Module/theme:** batch_test
- **Implements:** [hook_schema()](../../../system/system.api.php/hook_schema.md)

## Signature

```php
function database_test_schema()
```

## Documentation

```text
Implements hook_schema().

The database tests use the database API which depends on schema
information for certain operations on certain databases.
Therefore, the schema must actually be declared in a normal module
like any other, not directly in the test file.
```

## Code

```php
function database_test_schema() {
  $schema['test'] = array(
    'description' => 'Basic test table for the database unit tests.',
    'fields' => array(
      'id' => array(
        'type' => 'serial',
        'unsigned' => TRUE,
        'not null' => TRUE,
      ),
      'name' => array(
        'description' => "A person's name",
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'binary' => TRUE,
      ),
      'age' => array(
        'description' => "The person's age",
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
      'job' => array(
        'description' => "The person's job",
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => 'Undefined',
      ),
    ),
    'primary key' => array('id'),
    'unique keys' => array(
      'name' => array('name')
    ),
    'indexes' => array(
      'ages' => array('age'),
    ),
  );

  $schema['test_classtype'] = array(
    'description' => 'A duplicate version of the test table, used for fetch_style PDO::FETCH_CLASSTYPE tests.',
    'fields' => array(
      'classname' => array(
        'description' => "A custom class name",
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
      ),
      'name' => array(
        'description' => "A person's name",
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
      ),
      'age' => array(
        'description' => "The person's age",
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
      'job' => array(
        'description' => "The person's job",
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
      ),
    ),
    'primary key' => array('job'),
    'indexes' => array(
      'ages' => array('age'),
    ),
  );

  // This is an alternate version of the same table that is structured the same
  // but has a non-serial Primary Key.
  $schema['test_people'] = array(
    'description' => 'A duplicate version of the test table, used for additional tests.',
    'fields' => array(
      'name' => array(
        'description' => "A person's name",
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
      ),
      'age' => array(
        'description' => "The person's age",
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
      'job' => array(
        'description' => "The person's job",
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
      ),
    ),
    'primary key' => array('job'),
    'indexes' => array(
      'ages' => array('age'),
    ),
  );

  $schema['test_people_copy'] = $schema['test_people'];
  $schema['test_people_copy']['description'] = 'A duplicate version of the test_people table, used for additional tests.';

  $schema['test_one_blob'] = array(
    'description' => 'A simple table including a BLOB field for testing BLOB behavior.',
    'fields' => array(
      'id' => array(
        'description' => 'Simple unique ID.',
        'type' => 'serial',
        'not null' => TRUE,
      ),
      'blob1' => array(
        'description' => 'A BLOB field.',
        'type' => 'blob',
      ),
    ),
    'primary key' => array('id'),
    );

  $schema['test_two_blobs'] = array(
    'description' => 'A simple test table with two BLOB fields.',
    'fields' => array(
      'id' => array(
        'description' => 'Simple unique ID.',
        'type' => 'serial',
        'not null' => TRUE,
      ),
      'blob1' => array(
        'description' => 'A dummy BLOB field.',
        'type' => 'blob',
      ),
      'blob2' => array(
        'description' => 'A second BLOB field.',
        'type' => 'blob'
      ),
    ),
    'primary key' => array('id'),
    );

  $schema['test_task'] = array(
    'description' => 'A task list for people in the test table.',
    'fields' => array(
      'tid' => array(
        'description' => 'Task ID, primary key.',
        'type' => 'serial',
        'not null' => TRUE,
      ),
      'pid' => array(
        'description' => 'The {test_people}.pid, foreign key for the test table.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
      'task' => array(
        'description' => 'The task to be completed.',
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
      ),
      'priority' => array(
        'description' => 'The priority of the task.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
    ),
    'primary key' => array('tid'),
  );

  $schema['test_null'] = array(
    'description' => 'Basic test table for NULL value handling.',
    'fields' => array(
      'id' => array(
        'type' => 'serial',
        'unsigned' => TRUE,
        'not null' => TRUE,
      ),
      'name' => array(
        'description' => "A person's name.",
        'type' => 'varchar',
        'length' => 255,
        'not null' => FALSE,
        'default' => '',
      ),
      'age' => array(
        'description' => "The person's age.",
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => FALSE,
        'default' => 0),
    ),
    'primary key' => array('id'),
    'unique keys' => array(
      'name' => array('name')
    ),
    'indexes' => array(
      'ages' => array('age'),
    ),
  );

  $schema['test_serialized'] = array(
    'description' => 'Basic test table for NULL value handling.',
    'fields' => array(
      'id' => array(
        'type' => 'serial',
        'unsigned' => TRUE,
        'not null' => TRUE,
      ),
      'name' => array(
        'description' => "A person's name.",
        'type' => 'varchar',
        'length' => 255,
        'not null' => FALSE,
        'default' => '',
      ),
      'info' => array(
        'description' => "The person's data in serialized form.",
        'type' => 'blob',
        'serialize' => TRUE,
      ),
    ),
    'primary key' => array('id'),
    'unique keys' => array(
      'name' => array('name')
    ),
  );

  $schema['virtual'] = array(
    'description' => 'Basic test table with a reserved name.',
    'fields' => array(
      'id' => array(
        'type' => 'serial',
        'unsigned' => TRUE,
        'not null' => TRUE,
      ),
      'function' => array(
        'description' => "A column with a reserved name.",
        'type' => 'varchar',
        'length' => 255,
        'not null' => FALSE,
        'default' => '',
      ),
    ),
    'primary key' => array('id'),
  );

  $schema['TEST_UPPERCASE'] = $schema['test'];

  $schema['test_db_specific_datatype'] = array(
    'description' => 'Schema with database specific data type.',
    'fields' => array(
      'id' => array(
        'type' => 'serial',
        'unsigned' => TRUE,
        'not null' => TRUE,
      ),
      'age' => array(
        'description' => "The person's age.",
        'mysql_type' => 'tinyint',
        'pgsql_type' => 'smallint',
        'sqlite_type' => 'tinyint',
        'not null' => FALSE,
        'default' => 0,
      ),
    ),
    'primary key' => array('id'),
  );

  return $schema;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.install](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.install) · Licensed GPL-2.0-or-later (see LICENSE)._
