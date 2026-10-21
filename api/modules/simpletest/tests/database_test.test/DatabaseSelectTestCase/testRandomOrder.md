# DatabaseSelectTestCase::testRandomOrder()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1794–1839 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1794-L1839)
- **Class:** [DatabaseSelectTestCase](../DatabaseSelectTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRandomOrder()
```

## Documentation

```text
Test that random ordering of queries works.

We take the approach of testing the Drupal layer only, rather than trying
to test that the database's random number generator actually produces
random queries (which is very difficult to do without an unacceptable risk
of the test failing by accident).

Therefore, in this test we simply run the same query twice and assert that
the two results are reordered versions of each other (as well as of the
same query without the random ordering). It is reasonable to assume that
if we run the same select query twice and the results are in a different
order each time, the only way this could happen is if we have successfully
triggered the database's random ordering functionality.
```

## Code

```php
  function testRandomOrder() {
    // Use 52 items, so the chance that this test fails by accident will be the
    // same as the chance that a deck of cards will come out in the same order
    // after shuffling it (in other words, nearly impossible).
    $number_of_items = 52;
    while (db_query("SELECT MAX(id) FROM {test}")->fetchField() < $number_of_items) {
      db_insert('test')->fields(array('name' => $this->randomName()))->execute();
    }

    // First select the items in order and make sure we get an ordered list.
    $expected_ids = range(1, $number_of_items);
    $ordered_ids = db_select('test', 't')
      ->fields('t', array('id'))
      ->range(0, $number_of_items)
      ->orderBy('id')
      ->execute()
      ->fetchCol();
    $this->assertEqual($ordered_ids, $expected_ids, 'A query without random ordering returns IDs in the correct order.');

    // Now perform the same query, but instead choose a random ordering. We
    // expect this to contain a differently ordered version of the original
    // result.
    $randomized_ids = db_select('test', 't')
      ->fields('t', array('id'))
      ->range(0, $number_of_items)
      ->orderRandom()
      ->execute()
      ->fetchCol();
    $this->assertNotEqual($randomized_ids, $ordered_ids, 'A query with random ordering returns an unordered set of IDs.');
    $sorted_ids = $randomized_ids;
    sort($sorted_ids);
    $this->assertEqual($sorted_ids, $ordered_ids, 'After sorting the random list, the result matches the original query.');

    // Now perform the exact same query again, and make sure the order is
    // different.
    $randomized_ids_second_set = db_select('test', 't')
      ->fields('t', array('id'))
      ->range(0, $number_of_items)
      ->orderRandom()
      ->execute()
      ->fetchCol();
    $this->assertNotEqual($randomized_ids_second_set, $randomized_ids, 'Performing the query with random ordering a second time returns IDs in a different order.');
    $sorted_ids_second_set = $randomized_ids_second_set;
    sort($sorted_ids_second_set);
    $this->assertEqual($sorted_ids_second_set, $sorted_ids, 'After sorting the second random list, the result matches the sorted version of the first random list.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
