# SimpleTestDiscoveryTestCase::testDiscovery()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 793–828 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L793-L828)
- **Class:** [SimpleTestDiscoveryTestCase](../SimpleTestDiscoveryTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
function testDiscovery()
```

## Documentation

```text
Tests existence of test cases.
```

## Code

```php
  function testDiscovery() {
    $this->drupalGet('admin/config/development/testing');
    // Tests within enabled modules.
    // (without these, this test wouldn't happen in the first place, so this is
    // a bit pointless. We still run it for proof-of-concept.)
    // This one is defined in system module.
    $this->assertText('Drupal error handlers');
    // This one is defined in simpletest module.
    $this->assertText('Discovery of test classes');
    // Tests within disabled modules.
    if (version_compare(PHP_VERSION, '5.3') < 0) {
      // Don't expect PSR-0 tests to be discovered on older PHP versions.
      return;
    }
    // These are provided by simpletest itself via PSR-0 and PSR-4.
    $this->assertText('PSR0 web test');
    $this->assertText('PSR4 web test');
    $this->assertText('PSR0 example test: PSR-0 in disabled modules.');
    $this->assertText('PSR4 example test: PSR-4 in disabled modules.');
    $this->assertText('PSR0 example test: PSR-0 in nested subfolders.');
    $this->assertText('PSR4 example test: PSR-4 in nested subfolders.');

    // Test each test individually.
    foreach (array(
      'Drupal\\psr_0_test\\Tests\\ExampleTest',
      'Drupal\\psr_0_test\\Tests\\Nested\\NestedExampleTest',
      'Drupal\\psr_4_test\\Tests\\ExampleTest',
      'Drupal\\psr_4_test\\Tests\\Nested\\NestedExampleTest',
    ) as $class) {
      $this->drupalGet('admin/config/development/testing');
      $edit = array($class => TRUE);
      $this->drupalPost(NULL, $edit, t('Run tests'));
      $this->assertText('The test run finished', t('Test @class must finish.', array('@class' => $class)));
      $this->assertText('1 pass, 0 fails, and 0 exceptions', t('Test @class must pass.', array('@class' => $class)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
