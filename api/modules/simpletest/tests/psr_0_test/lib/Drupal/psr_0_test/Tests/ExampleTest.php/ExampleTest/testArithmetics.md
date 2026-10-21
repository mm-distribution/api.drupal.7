# ExampleTest::testArithmetics()

- **Type:** Method
- **File:** [`modules/simpletest/tests/psr_0_test/lib/Drupal/psr_0_test/Tests/ExampleTest.php`](../_file.md), lines 15–17 · [local source](../../../../../../../../../../../source/modules/simpletest/tests/psr_0_test/lib/Drupal/psr_0_test/Tests/ExampleTest.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/psr_0_test/lib/Drupal/psr_0_test/Tests/ExampleTest.php#L15-L17)
- **Class:** [ExampleTest](../ExampleTest.md)
- **Module/theme:** psr_0_test

## Signature

```php
function testArithmetics()
```

## Documentation

_No docblock in source._

## Code

```php
  function testArithmetics() {
    $this->assert(1 + 1 == 2, '1 + 1 == 2');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/psr_0_test/lib/Drupal/psr_0_test/Tests/ExampleTest.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/psr_0_test/lib/Drupal/psr_0_test/Tests/ExampleTest.php) · Licensed GPL-2.0-or-later (see LICENSE)._
