# SimpleTestMissingDependentModuleUnitTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 560–567 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L560-L567)
- **Class:** [SimpleTestMissingDependentModuleUnitTest](../SimpleTestMissingDependentModuleUnitTest.md)
- **Module/theme:** simpletest

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
      'name' => 'Testing dependent module test',
      'description' => 'This test should not load since it requires a module that is not found.',
      'group' => 'SimpleTest',
      'dependencies' => array('simpletest_missing_module'),
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
