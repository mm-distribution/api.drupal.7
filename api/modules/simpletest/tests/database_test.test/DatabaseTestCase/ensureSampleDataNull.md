# DatabaseTestCase::ensureSampleDataNull()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 62–81 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L62-L81)
- **Class:** [DatabaseTestCase](../DatabaseTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function ensureSampleDataNull()
```

## Documentation

```text
Set up tables for NULL handling.
```

## Code

```php
  function ensureSampleDataNull() {
    $schema['test_null'] = drupal_get_schema('test_null');
    $this->installTables($schema);

    db_insert('test_null')
    ->fields(array('name', 'age'))
    ->values(array(
      'name' => 'Kermit',
      'age' => 25,
    ))
    ->values(array(
      'name' => 'Fozzie',
      'age' => NULL,
    ))
    ->values(array(
      'name' => 'Gonzo',
      'age' => 27,
    ))
    ->execute();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
