# DatabaseSelectOrderedTestCase::testOrderByEscaping()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2122–2126 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2122-L2126)
- **Class:** [DatabaseSelectOrderedTestCase](../DatabaseSelectOrderedTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testOrderByEscaping()
```

## Documentation

```text
Tests that the sort direction is sanitized properly.
```

## Code

```php
  function testOrderByEscaping() {
    $query = db_select('test')->orderBy('name', 'invalid direction');
    $order_bys = $query->getOrderBy();
    $this->assertEqual($order_bys['name'], 'ASC', 'Invalid order by direction is converted to ASC.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
