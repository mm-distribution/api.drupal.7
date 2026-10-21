# DatabaseTransactionTestCase::executeDDLStatement()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4033–4046 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4033-L4046)
- **Class:** [DatabaseTransactionTestCase](../DatabaseTransactionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function executeDDLStatement()
```

## Documentation

```text
Execute a DDL statement.
```

## Code

```php
  protected function executeDDLStatement() {
    static $count = 0;
    $table = array(
      'fields' => array(
        'id' => array(
          'type' => 'serial',
          'unsigned' => TRUE,
          'not null' => TRUE,
        ),
      ),
      'primary key' => array('id'),
    );
    db_create_table('database_test_' . ++$count, $table);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
