# DatabaseCaseSensitivityTestCase::testCaseSensitiveInsert()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3494–3509 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3494-L3509)
- **Class:** [DatabaseCaseSensitivityTestCase](../DatabaseCaseSensitivityTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCaseSensitiveInsert()
```

## Documentation

```text
Test BINARY collation in MySQL.
```

## Code

```php
  function testCaseSensitiveInsert() {
    $num_records_before = db_query('SELECT COUNT(*) FROM {test}')->fetchField();

    $john = db_insert('test')
      ->fields(array(
        'name' => 'john', // <- A record already exists with name 'John'.
        'age' => 2,
        'job' => 'Baby',
      ))
      ->execute();

    $num_records_after = db_query('SELECT COUNT(*) FROM {test}')->fetchField();
    $this->assertIdentical($num_records_before + 1, (int) $num_records_after, 'Record inserts correctly.');
    $saved_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'john'))->fetchField();
    $this->assertIdentical($saved_age, '2', 'Can retrieve after inserting.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
