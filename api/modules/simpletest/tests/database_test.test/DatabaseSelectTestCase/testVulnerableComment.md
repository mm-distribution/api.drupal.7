# DatabaseSelectTestCase::testVulnerableComment()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1477–1499 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1477-L1499)
- **Class:** [DatabaseSelectTestCase](../DatabaseSelectTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testVulnerableComment()
```

## Documentation

```text
Test query COMMENT system against vulnerabilities.
```

## Code

```php
  function testVulnerableComment() {
    $query = db_select('test')->comment('Testing query comments */ SELECT nid FROM {node}; --');
    $name_field = $query->addField('test', 'name');
    $age_field = $query->addField('test', 'age', 'age');
    $result = $query->execute();

    $num_records = 0;
    foreach ($result as $record) {
      $num_records++;
    }

    $query = (string)$query;
    $expected = "/* Testing query comments  * / SELECT nid FROM {node}; -- */ SELECT test.name AS name, test.age AS age\nFROM \n{test} test";

    $this->assertEqual($num_records, 4, 'Returned the correct number of rows.');
    $this->assertEqual($query, $expected, 'The flattened query contains the sanitised comment string.');

    $connection = Database::getConnection();
    foreach ($this->makeCommentsProvider() as $test_set) {
      list($expected, $comments) = $test_set;
      $this->assertEqual($expected, $connection->makeComment($comments));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
