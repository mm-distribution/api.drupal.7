# DatabaseInsertDefaultsTestCase::testDefaultInsert()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 781–789 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L781-L789)
- **Class:** [DatabaseInsertDefaultsTestCase](../DatabaseInsertDefaultsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDefaultInsert()
```

## Documentation

```text
Test that we can run a query that is "default values for everything".
```

## Code

```php
  function testDefaultInsert() {
    $query = db_insert('test')->useDefaults(array('job'));
    $id = $query->execute();

    $schema = drupal_get_schema('test');

    $job = db_query('SELECT job FROM {test} WHERE id = :id', array(':id' => $id))->fetchField();
    $this->assertEqual($job, $schema['fields']['job']['default'], 'Default field value is set.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
