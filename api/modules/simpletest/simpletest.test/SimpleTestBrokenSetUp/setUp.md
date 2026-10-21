# SimpleTestBrokenSetUp::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 595–608 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L595-L608)
- **Class:** [SimpleTestBrokenSetUp](../SimpleTestBrokenSetUp.md)
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
    // If the test is being run from the main site, set up normally.
    if (!drupal_valid_test_ua()) {
      parent::setUp('simpletest');
      // Create and log in user.
      $admin_user = $this->drupalCreateUser(array('administer unit tests'));
      $this->drupalLogin($admin_user);
    }
    // If the test is being run from within simpletest, set up the broken test.
    else {
      $this->pass(t('The test setUp() method has been run.'));
      // Don't call parent::setUp(). This should trigger an error message.
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
