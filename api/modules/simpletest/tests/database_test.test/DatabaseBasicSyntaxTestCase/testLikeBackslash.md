# DatabaseBasicSyntaxTestCase::testLikeBackslash()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3450–3476 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3450-L3476)
- **Class:** [DatabaseBasicSyntaxTestCase](../DatabaseBasicSyntaxTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testLikeBackslash()
```

## Documentation

```text
Test LIKE query containing a backslash.
```

## Code

```php
  function testLikeBackslash() {
    db_insert('test')
      ->fields(array('name'))
      ->values(array(
        'name' => 'abcde\f',
      ))
      ->values(array(
        'name' => 'abc%\_',
      ))
      ->execute();

    // Match both rows using a LIKE expression with two wildcards and a verbatim
    // backslash.
    $num_matches = db_select('test', 't')
      ->condition('name', 'abc%\\\\_', 'LIKE')
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertIdentical($num_matches, '2', 'Found 2 records.');
    // Match only the former using a LIKE expression with no wildcards.
    $num_matches = db_select('test', 't')
      ->condition('name', db_like('abc%\_'), 'LIKE')
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertIdentical($num_matches, '1', 'Found 1 record.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
