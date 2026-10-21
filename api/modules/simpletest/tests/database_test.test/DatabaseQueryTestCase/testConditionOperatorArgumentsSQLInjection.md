# DatabaseQueryTestCase::testConditionOperatorArgumentsSQLInjection()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3640–3696 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3640-L3696)
- **Class:** [DatabaseQueryTestCase](../DatabaseQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testConditionOperatorArgumentsSQLInjection()
```

## Documentation

```text
Tests SQL injection via condition operator.
```

## Code

```php
  public function testConditionOperatorArgumentsSQLInjection() {

    $injection = "IS NOT NULL); INSERT INTO {test} (name) VALUES ('test12345678'); -- ";
    try {
      $result = db_select('test', 't')
        ->fields('t')
        ->condition('name', 1, $injection)
        ->execute();
      $this->fail('Should not be able to attempt SQL injection via condition operator.');
    }
    catch (InvalidQueryConditionOperatorException $e) {
      $this->pass('SQL injection attempt via condition arguments should result in a database exception.');
    }

    // Test that the insert query that was used in the SQL injection attempt did
    // not result in a row being inserted in the database.
    $result = db_select('test')
      ->condition('name', 'test12345678')
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertFalse($result, 'SQL injection attempt did not result in a row being inserted in the database table.');

    // Attempt SQLi via union query with no unsafe characters.
    db_insert('test')
      ->fields(array('name' => '123456'))
      ->execute();

    $injection = "= 1 UNION ALL SELECT password FROM user WHERE uid =";
    try {
      $result = db_select('test', 't')
        ->fields('t', array('name', 'name'))
        ->condition('name', 1, $injection)
        ->execute();
      $this->fail('Should not be able to attempt SQL injection via operator.');
    }
    catch (InvalidQueryConditionOperatorException $e) {
      $this->pass('SQL injection attempt via condition arguments should result in a database exception.');
    }

    // Attempt SQLi via union query - uppercase tablename.
    db_insert('TEST_UPPERCASE')
      ->fields(array('name' => 'secrets'))
      ->execute();

    $injection = "IS NOT NULL) UNION ALL SELECT name FROM {TEST_UPPERCASE} -- ";
    try {
      $result = db_select('test', 't')
        ->fields('t', array('name'))
        ->condition('name', 1, $injection)
        ->execute();
      $this->fail('Should not be able to attempt SQL injection via operator.');
    }
    catch (InvalidQueryConditionOperatorException $e) {
      $this->pass('SQL injection attempt via condition arguments should result in a database exception.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
