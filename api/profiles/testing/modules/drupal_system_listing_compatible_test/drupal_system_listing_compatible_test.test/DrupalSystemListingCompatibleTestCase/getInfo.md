# DrupalSystemListingCompatibleTestCase::getInfo()

- **Type:** Method
- **File:** [`profiles/testing/modules/drupal_system_listing_compatible_test/drupal_system_listing_compatible_test.test`](../_file.md), lines 17–23 · [local source](../../../../../../../source/profiles/testing/modules/drupal_system_listing_compatible_test/drupal_system_listing_compatible_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/profiles/testing/modules/drupal_system_listing_compatible_test/drupal_system_listing_compatible_test.test#L17-L23)
- **Class:** [DrupalSystemListingCompatibleTestCase](../DrupalSystemListingCompatibleTestCase.md)
- **Module/theme:** drupal_system_listing_compatible_test

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Installation profile module tests helper',
      'description' => 'Verifies that tests in installation profile modules are found and may use another profile for running tests.',
      'group' => 'Installation profile',
    );
  }
```

---
_Drupal 7.103 · [profiles/testing/modules/drupal_system_listing_compatible_test/drupal_system_listing_compatible_test.test](https://github.com/drupal/drupal/blob/7.103/profiles/testing/modules/drupal_system_listing_compatible_test/drupal_system_listing_compatible_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
