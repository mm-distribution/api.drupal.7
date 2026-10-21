# DatabaseRegressionTestCase::testRegression_310447()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3093–3105 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3093-L3105)
- **Class:** [DatabaseRegressionTestCase](../DatabaseRegressionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRegression_310447()
```

## Documentation

```text
Regression test for #310447.

Tries to insert non-ascii UTF-8 data in a database column and checks
if its stored properly.
```

## Code

```php
  function testRegression_310447() {
    // That's a 255 character UTF-8 string.
    $name = str_repeat("é", 255);
    db_insert('test')
      ->fields(array(
        'name' => $name,
        'age' => 20,
        'job' => 'Dancer',
      ))->execute();

    $from_database = db_query('SELECT name FROM {test} WHERE name = :name', array(':name' => $name))->fetchField();
    $this->assertIdentical($name, $from_database, "The database handles UTF-8 characters cleanly.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
