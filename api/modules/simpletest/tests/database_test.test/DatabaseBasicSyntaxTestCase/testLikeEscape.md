# DatabaseBasicSyntaxTestCase::testLikeEscape()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3424–3445 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3424-L3445)
- **Class:** [DatabaseBasicSyntaxTestCase](../DatabaseBasicSyntaxTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testLikeEscape()
```

## Documentation

```text
Test escaping of LIKE wildcards.
```

## Code

```php
  function testLikeEscape() {
    db_insert('test')
      ->fields(array(
        'name' => 'Ring_',
      ))
      ->execute();

    // Match both "Ringo" and "Ring_".
    $num_matches = db_select('test', 't')
      ->condition('name', 'Ring_', 'LIKE')
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertIdentical($num_matches, '2', 'Found 2 records.');
    // Match only "Ring_" using a LIKE expression with no wildcards.
    $num_matches = db_select('test', 't')
      ->condition('name', db_like('Ring_'), 'LIKE')
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertIdentical($num_matches, '1', 'Found 1 record.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
