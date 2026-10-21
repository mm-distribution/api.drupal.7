# DatabaseAlterTestCase::testSimpleAlter()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2935–2949 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2935-L2949)
- **Class:** [DatabaseAlterTestCase](../DatabaseAlterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSimpleAlter()
```

## Documentation

```text
Test that we can do basic alters.
```

## Code

```php
  function testSimpleAlter() {
    $query = db_select('test');
    $query->addField('test', 'name');
    $query->addField('test', 'age', 'age');
    $query->addTag('database_test_alter_add_range');

    $result = $query->execute();

    $num_records = 0;
    foreach ($result as $record) {
      $num_records++;
    }

    $this->assertEqual($num_records, 2, 'Returned the correct number of rows.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
