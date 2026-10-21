# ExampleTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/psr_0_test/lib/Drupal/psr_0_test/Tests/ExampleTest.php`](../_file.md), lines 7–13 · [local source](../../../../../../../../../../../source/modules/simpletest/tests/psr_0_test/lib/Drupal/psr_0_test/Tests/ExampleTest.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/psr_0_test/lib/Drupal/psr_0_test/Tests/ExampleTest.php#L7-L13)
- **Class:** [ExampleTest](../ExampleTest.md)
- **Module/theme:** psr_0_test

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'PSR0 example test: PSR-0 in disabled modules.',
      'description' => 'We want to assert that this test case is being discovered.',
      'group' => 'SimpleTest',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/psr_0_test/lib/Drupal/psr_0_test/Tests/ExampleTest.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/psr_0_test/lib/Drupal/psr_0_test/Tests/ExampleTest.php) · Licensed GPL-2.0-or-later (see LICENSE)._
