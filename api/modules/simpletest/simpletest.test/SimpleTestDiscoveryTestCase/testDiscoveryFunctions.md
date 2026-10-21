# SimpleTestDiscoveryTestCase::testDiscoveryFunctions()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 773–788 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L773-L788)
- **Class:** [SimpleTestDiscoveryTestCase](../SimpleTestDiscoveryTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
function testDiscoveryFunctions()
```

## Documentation

```text
Test discovery of PSR-0 test classes.
```

## Code

```php
  function testDiscoveryFunctions() {
    if (version_compare(PHP_VERSION, '5.3') < 0) {
      // Don't expect PSR-0 tests to be discovered on older PHP versions.
      return;
    }
    // TODO: What if we have cached values? Do we need to force a cache refresh?
    $classes_all = simpletest_test_get_all();
    foreach (array(
      'Drupal\\simpletest\\Tests\\PSR0WebTest',
      'Drupal\\simpletest\\Tests\\PSR4WebTest',
      'Drupal\\psr_0_test\\Tests\\ExampleTest',
      'Drupal\\psr_4_test\\Tests\\ExampleTest',
    ) as $class) {
      $this->assert(!empty($classes_all['SimpleTest'][$class]), t('Class @class must be discovered by simpletest_test_get_all().', array('@class' => $class)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
