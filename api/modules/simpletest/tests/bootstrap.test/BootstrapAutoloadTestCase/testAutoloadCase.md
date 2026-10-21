# BootstrapAutoloadTestCase::testAutoloadCase()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 352–361 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L352-L361)
- **Class:** [BootstrapAutoloadTestCase](../BootstrapAutoloadTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAutoloadCase()
```

## Documentation

```text
Tests that autoloader name matching is not case sensitive.
```

## Code

```php
  function testAutoloadCase() {
    // Test interface autoloader.
    $this->assertTrue(drupal_autoload_interface('drupalautoloadtestinterface'), 'drupal_autoload_interface() recognizes <em>DrupalAutoloadTestInterface</em> in lower case.');
    // Test class autoloader.
    $this->assertTrue(drupal_autoload_class('drupalautoloadtestclass'), 'drupal_autoload_class() recognizes <em>DrupalAutoloadTestClass</em> in lower case.');
    // Test trait autoloader.
    if (version_compare(PHP_VERSION, '5.4') >= 0) {
      $this->assertTrue(drupal_autoload_trait('drupalautoloadtesttrait'), 'drupal_autoload_trait() recognizes <em>DrupalAutoloadTestTrait</em> in lower case.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
