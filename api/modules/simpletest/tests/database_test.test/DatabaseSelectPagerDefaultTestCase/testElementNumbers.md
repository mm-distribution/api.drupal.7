# DatabaseSelectPagerDefaultTestCase::testElementNumbers()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2677–2709 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2677-L2709)
- **Class:** [DatabaseSelectPagerDefaultTestCase](../DatabaseSelectPagerDefaultTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testElementNumbers()
```

## Documentation

```text
Confirm that every pager gets a valid non-overlaping element ID.
```

## Code

```php
  function testElementNumbers() {
    $_GET['page'] = '3, 2, 1, 0';

    $query = db_select('test', 't')->extend('PagerDefault');
    $query->element(2)
      ->fields('t', array('name'))
      ->orderBy('age')
      ->limit(1);
    $this->assertEqual(2, $query->getElement());
    $name = $query->execute()->fetchField();
    $this->assertEqual($name, 'Paul', 'Pager query #1 with a specified element ID returned the correct results.');

    // Setting an element smaller than the previous one
    // should not overwrite the pager $maxElement with a smaller value.
    $query = db_select('test', 't')->extend('PagerDefault');
    $query->element(1)
      ->fields('t', array('name'))
      ->orderBy('age')
      ->limit(1);
    $this->assertEqual(1, $query->getElement());
    $name = $query->execute()->fetchField();
    $this->assertEqual($name, 'George', 'Pager query #2 with a specified element ID returned the correct results.');

    $query = db_select('test', 't')->extend('PagerDefault');
    $query->fields('t', array('name'))
      ->orderBy('age')
      ->limit(1);
    $this->assertEqual(3, $query->getElement());
    $name = $query->execute()->fetchField();
    $this->assertEqual($name, 'John', 'Pager query #3 with a generated element ID returned the correct results.');

    unset($_GET['page']);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
