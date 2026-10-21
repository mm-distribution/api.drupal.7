# DatabaseQueryTestCase::testArrayArgumentsSQLInjection()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3613–3635 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3613-L3635)
- **Class:** [DatabaseQueryTestCase](../DatabaseQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testArrayArgumentsSQLInjection()
```

## Documentation

```text
Test SQL injection via database query array arguments.
```

## Code

```php
  public function testArrayArgumentsSQLInjection() {
    // Attempt SQL injection and verify that it does not work.
    $condition = array(
      "1 ;INSERT INTO {test} (name) VALUES ('test12345678'); -- " => '',
      '1' => '',
    );
    try {
      db_query("SELECT * FROM {test} WHERE name = :name", array(':name' => $condition))->fetchObject();
      $this->fail('SQL injection attempt via array arguments should result in a PDOException.');
    }
    catch (PDOException $e) {
      $this->pass('SQL injection attempt via array arguments should result in a PDOException.');
    }

    // Test that the insert query that was used in the SQL injection attempt did
    // not result in a row being inserted in the database.
    $result = db_select('test')
      ->condition('name', 'test12345678')
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertFalse($result, 'SQL injection attempt did not result in a row being inserted in the database table.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
