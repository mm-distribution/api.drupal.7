# DatabaseSelectTestCase::makeCommentsProvider()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1504–1530 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1504-L1530)
- **Class:** [DatabaseSelectTestCase](../DatabaseSelectTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function makeCommentsProvider()
```

## Documentation

```text
Provides expected and input values for testVulnerableComment().
```

## Code

```php
  function makeCommentsProvider() {
    return array(
      array(
        '/*  */ ',
        array(''),
      ),
      // Try and close the comment early.
      array(
        '/* Exploit  * / DROP TABLE node; -- */ ',
        array('Exploit */ DROP TABLE node; --'),
      ),
      // Variations on comment closing.
      array(
        '/* Exploit  * / * / DROP TABLE node; -- */ ',
        array('Exploit */*/ DROP TABLE node; --'),
      ),
      array(
        '/* Exploit  *  * // DROP TABLE node; -- */ ',
        array('Exploit **// DROP TABLE node; --'),
      ),
      // Try closing the comment in the second string which is appended.
      array(
        '/* Exploit  * / DROP TABLE node; --; Another try  * / DROP TABLE node; -- */ ',
        array('Exploit */ DROP TABLE node; --', 'Another try */ DROP TABLE node; --'),
      ),
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
