# DatabaseNextIdCase::testDbNextId()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4218–4227 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4218-L4227)
- **Class:** [DatabaseNextIdCase](../DatabaseNextIdCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDbNextId()
```

## Documentation

```text
Test that the sequences API work.
```

## Code

```php
  function testDbNextId() {
    $first = db_next_id();
    $second = db_next_id();
    // We can test for exact increase in here because we know there is no
    // other process operating on these tables -- normally we could only
    // expect $second > $first.
    $this->assertEqual($first + 1, $second, 'The second call from a sequence provides a number increased by one.');
    $result = db_next_id(1000);
    $this->assertEqual($result, 1001, 'Sequence provides a larger number than the existing ID.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
