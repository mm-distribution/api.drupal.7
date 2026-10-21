# NestedExampleTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/psr_4_test/src/Tests/Nested/NestedExampleTest.php`](../_file.md), lines 7–13 · [local source](../../../../../../../../../../source/modules/simpletest/tests/psr_4_test/src/Tests/Nested/NestedExampleTest.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/psr_4_test/src/Tests/Nested/NestedExampleTest.php#L7-L13)
- **Class:** [NestedExampleTest](../NestedExampleTest.md)
- **Module/theme:** psr_4_test

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
      'name' => 'PSR4 example test: PSR-4 in nested subfolders.',
      'description' => 'We want to assert that this PSR-4 test case is being discovered.',
      'group' => 'SimpleTest',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/psr_4_test/src/Tests/Nested/NestedExampleTest.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/psr_4_test/src/Tests/Nested/NestedExampleTest.php) · Licensed GPL-2.0-or-later (see LICENSE)._
