# SimpleTestDiscoveryTestCase

- **Type:** Class
- **File:** [`modules/simpletest/simpletest.test`](_file.md), lines 739–829 · [local source](../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L739-L829)
- **Module/theme:** simpletest

## Signature

```php
class SimpleTestDiscoveryTestCase extends DrupalWebTestCase
```

## Documentation

```text
Verifies that tests in other installation profiles are not found.

@see SimpleTestInstallationProfileModuleTestsTestCase
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

- [getInfo()](SimpleTestDiscoveryTestCase/getInfo.md)
- [setUp()](SimpleTestDiscoveryTestCase/setUp.md)
- [testDiscoveryFunctions()](SimpleTestDiscoveryTestCase/testDiscoveryFunctions.md) — Test discovery of PSR-0 test classes.
- [testDiscovery()](SimpleTestDiscoveryTestCase/testDiscovery.md) — Tests existence of test cases.

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
