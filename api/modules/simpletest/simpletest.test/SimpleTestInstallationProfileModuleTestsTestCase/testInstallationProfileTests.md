# SimpleTestInstallationProfileModuleTestsTestCase::testInstallationProfileTests()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 681–689 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L681-L689)
- **Class:** [SimpleTestInstallationProfileModuleTestsTestCase](../SimpleTestInstallationProfileModuleTestsTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
function testInstallationProfileTests()
```

## Documentation

```text
Tests existence of test case located in an installation profile module.
```

## Code

```php
  function testInstallationProfileTests() {
    $this->drupalGet('admin/config/development/testing');
    $this->assertText('Installation profile module tests helper');
    $edit = array(
      'DrupalSystemListingCompatibleTestCase' => TRUE,
    );
    $this->drupalPost(NULL, $edit, t('Run tests'));
    $this->assertText('DrupalSystemListingCompatibleTestCase test executed.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
