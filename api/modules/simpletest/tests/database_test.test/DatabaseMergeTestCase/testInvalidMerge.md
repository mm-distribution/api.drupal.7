# DatabaseMergeTestCase::testInvalidMerge()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1405–1420 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1405-L1420)
- **Class:** [DatabaseMergeTestCase](../DatabaseMergeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testInvalidMerge()
```

## Documentation

```text
Test that an invalid merge query throws an exception like it is supposed to.
```

## Code

```php
  function testInvalidMerge() {
    try {
      // This query should die because there is no key field specified.
      db_merge('test_people')
        ->fields(array(
          'age' => 31,
          'name' => 'Tiffany',
        ))
        ->execute();
    }
    catch (InvalidMergeQueryException $e) {
      $this->pass('InvalidMergeQueryException thrown for invalid query.');
      return;
    }
    $this->fail('No InvalidMergeQueryException thrown');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
