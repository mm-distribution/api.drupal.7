# SimpleTestOtherInstallationProfileModuleTestsTestCase::testOtherInstallationProfile()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 728–731 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L728-L731)
- **Class:** [SimpleTestOtherInstallationProfileModuleTestsTestCase](../SimpleTestOtherInstallationProfileModuleTestsTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
function testOtherInstallationProfile()
```

## Documentation

```text
Tests that tests located in another installation profile do not appear.
```

## Code

```php
  function testOtherInstallationProfile() {
    $this->drupalGet('admin/config/development/testing');
    $this->assertNoText('Installation profile module tests helper');
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
