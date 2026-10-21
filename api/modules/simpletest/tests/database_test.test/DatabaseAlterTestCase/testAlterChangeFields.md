# DatabaseAlterTestCase::testAlterChangeFields()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3003–3013 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3003-L3013)
- **Class:** [DatabaseAlterTestCase](../DatabaseAlterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAlterChangeFields()
```

## Documentation

```text
Test that we can alter the fields of a query.
```

## Code

```php
  function testAlterChangeFields() {
    $query = db_select('test');
    $name_field = $query->addField('test', 'name');
    $age_field = $query->addField('test', 'age', 'age');
    $query->orderBy('name');
    $query->addTag('database_test_alter_change_fields');

    $record = $query->execute()->fetch();
    $this->assertEqual($record->$name_field, 'George', 'Correct data retrieved.');
    $this->assertFalse(isset($record->$age_field), 'Age field not found, as intended.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
