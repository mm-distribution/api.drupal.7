# DrupalSystemListingCompatibleTestCase::setUp()

- **Type:** Method
- **File:** [`profiles/testing/modules/drupal_system_listing_compatible_test/drupal_system_listing_compatible_test.test`](../_file.md), lines 25–29 · [local source](../../../../../../../source/profiles/testing/modules/drupal_system_listing_compatible_test/drupal_system_listing_compatible_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/profiles/testing/modules/drupal_system_listing_compatible_test/drupal_system_listing_compatible_test.test#L25-L29)
- **Class:** [DrupalSystemListingCompatibleTestCase](../DrupalSystemListingCompatibleTestCase.md)
- **Module/theme:** drupal_system_listing_compatible_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    // Attempt to install a module in Testing profile, while this test runs with
    // a different profile.
    parent::setUp(array('drupal_system_listing_compatible_test'));
  }
```

---
_Drupal 7.103 · [profiles/testing/modules/drupal_system_listing_compatible_test/drupal_system_listing_compatible_test.test](https://github.com/drupal/drupal/blob/7.103/profiles/testing/modules/drupal_system_listing_compatible_test/drupal_system_listing_compatible_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
