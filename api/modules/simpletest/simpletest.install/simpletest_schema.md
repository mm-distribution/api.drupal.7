# simpletest_schema()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.install`](_file.md), lines 64–151 · [local source](../../../../source/modules/simpletest/simpletest.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.install#L64-L151)
- **Module/theme:** simpletest
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function simpletest_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function simpletest_schema() {
  $schema['simpletest'] = array(
    'description' => 'Stores simpletest messages',
    'fields' => array(
      'message_id'  => array(
        'type' => 'serial',
        'not null' => TRUE,
        'description' => 'Primary Key: Unique simpletest message ID.',
      ),
      'test_id' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Test ID, messages belonging to the same ID are reported together',
      ),
      'test_class' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'description' => 'The name of the class that created this message.',
      ),
      'status' => array(
        'type' => 'varchar',
        'length' => 9,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Message status. Core understands pass, fail, exception.',
      ),
      'message' => array(
        'type' => 'text',
        'not null' => TRUE,
        'description' => 'The message itself.',
      ),
      'message_group' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'description' => 'The message group this message belongs to. For example: warning, browser, user.',
      ),
      'function' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Name of the assertion function or method that created this message.',
      ),
      'line' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Line number on which the function is called.',
      ),
      'file' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Name of the file where the function is called.',
      ),
    ),
    'primary key' => array('message_id'),
    'indexes' => array(
      'reporter' => array('test_class', 'message_id'),
    ),
  );
  $schema['simpletest_test_id'] = array(
    'description' => 'Stores simpletest test IDs, used to auto-incrament the test ID so that a fresh test ID is used.',
    'fields' => array(
      'test_id'  => array(
        'type' => 'serial',
        'not null' => TRUE,
        'description' => 'Primary Key: Unique simpletest ID used to group test results together. Each time a set of tests
                            are run a new test ID is used.',
      ),
      'last_prefix' => array(
        'type' => 'varchar',
        'length' => 60,
        'not null' => FALSE,
        'default' => '',
        'description' => 'The last database prefix used during testing.',
      ),
    ),
    'primary key' => array('test_id'),
  );
  return $schema;
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.install](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.install) · Licensed GPL-2.0-or-later (see LICENSE)._
