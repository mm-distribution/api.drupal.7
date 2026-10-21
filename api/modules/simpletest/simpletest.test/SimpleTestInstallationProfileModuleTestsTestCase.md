# SimpleTestInstallationProfileModuleTestsTestCase

- **Type:** Class
- **File:** [`modules/simpletest/simpletest.test`](_file.md), lines 647–690 · [local source](../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L647-L690)
- **Module/theme:** simpletest

## Signature

```php
class SimpleTestInstallationProfileModuleTestsTestCase extends DrupalWebTestCase
```

## Documentation

```text
Verifies that tests bundled with installation profile modules are found.
```

## Properties

### $profile

```php
protected $profile = 'testing';
```

```text
Use the Testing profile.

The Testing profile contains drupal_system_listing_compatible_test.test,
which attempts to:
- run tests using the Minimal profile (which does not contain the
  drupal_system_listing_compatible_test.module)
- but still install the drupal_system_listing_compatible_test.module
  contained in the Testing profile.

@see DrupalSystemListingCompatibleTestCase
```

### $admin_user

```php
protected $admin_user;
```

## Methods (derived index)

- [getInfo()](SimpleTestInstallationProfileModuleTestsTestCase/getInfo.md)
- [setUp()](SimpleTestInstallationProfileModuleTestsTestCase/setUp.md)
- [testInstallationProfileTests()](SimpleTestInstallationProfileModuleTestsTestCase/testInstallationProfileTests.md) — Tests existence of test case located in an installation profile module.

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
