# SimpleTestOtherInstallationProfileModuleTestsTestCase

- **Type:** Class
- **File:** [`modules/simpletest/simpletest.test`](_file.md), lines 697–732 · [local source](../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L697-L732)
- **Module/theme:** simpletest

## Signature

```php
class SimpleTestOtherInstallationProfileModuleTestsTestCase extends DrupalWebTestCase
```

## Documentation

```text
Verifies that tests in other installation profiles are not found.

@see SimpleTestInstallationProfileModuleTestsTestCase
```

## Properties

### $profile

```php
protected $profile = 'minimal';
```

```text
Use the Minimal profile.

The Testing profile contains drupal_system_listing_compatible_test.test,
which should not be found.

@see SimpleTestInstallationProfileModuleTestsTestCase
@see DrupalSystemListingCompatibleTestCase
```

### $admin_user

```php
protected $admin_user;
```

## Methods (derived index)

- [getInfo()](SimpleTestOtherInstallationProfileModuleTestsTestCase/getInfo.md)
- [setUp()](SimpleTestOtherInstallationProfileModuleTestsTestCase/setUp.md)
- [testOtherInstallationProfile()](SimpleTestOtherInstallationProfileModuleTestsTestCase/testOtherInstallationProfile.md) — Tests that tests located in another installation profile do not appear.

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
