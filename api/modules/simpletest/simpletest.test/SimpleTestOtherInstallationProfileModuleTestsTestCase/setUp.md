# SimpleTestOtherInstallationProfileModuleTestsTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 718–723 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L718-L723)
- **Class:** [SimpleTestOtherInstallationProfileModuleTestsTestCase](../SimpleTestOtherInstallationProfileModuleTestsTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp(array('simpletest'));

    $this->admin_user = $this->drupalCreateUser(array('administer unit tests'));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
