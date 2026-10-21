# DrupalSystemListingCompatibleTestCase

- **Type:** Class
- **File:** [`profiles/testing/modules/drupal_system_listing_compatible_test/drupal_system_listing_compatible_test.test`](_file.md), lines 6–37 · [local source](../../../../../../source/profiles/testing/modules/drupal_system_listing_compatible_test/drupal_system_listing_compatible_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/profiles/testing/modules/drupal_system_listing_compatible_test/drupal_system_listing_compatible_test.test#L6-L37)
- **Module/theme:** drupal_system_listing_compatible_test

## Signature

```php
class DrupalSystemListingCompatibleTestCase extends DrupalWebTestCase
```

## Documentation

```text
Helper to verify tests in installation profile modules.
```

## Properties

### $profile

```php
protected $profile = 'minimal';
```

```text
Use the Minimal profile.

This test needs to use a different installation profile than the test which
asserts that this test is found.

@see SimpleTestInstallationProfileModuleTestsTestCase
```

## Methods (derived index)

- [getInfo()](DrupalSystemListingCompatibleTestCase/getInfo.md)
- [setUp()](DrupalSystemListingCompatibleTestCase/setUp.md)
- [testDrupalSystemListing()](DrupalSystemListingCompatibleTestCase/testDrupalSystemListing.md) — Non-empty test* method required to executed the test case class.

---
_Drupal 7.103 · [profiles/testing/modules/drupal_system_listing_compatible_test/drupal_system_listing_compatible_test.test](https://github.com/drupal/drupal/blob/7.103/profiles/testing/modules/drupal_system_listing_compatible_test/drupal_system_listing_compatible_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
