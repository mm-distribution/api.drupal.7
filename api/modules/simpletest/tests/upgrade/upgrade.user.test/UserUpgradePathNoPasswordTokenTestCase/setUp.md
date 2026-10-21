# UserUpgradePathNoPasswordTokenTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.user.test`](../_file.md), lines 50–57 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.user.test#L50-L57)
- **Class:** [UserUpgradePathNoPasswordTokenTestCase](../UserUpgradePathNoPasswordTokenTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  public function setUp() {
    // Path to the database dump files.
    $this->databaseDumpFiles = array(
      drupal_get_path('module', 'simpletest') . '/tests/upgrade/drupal-6.bare.database.php',
      drupal_get_path('module', 'simpletest') . '/tests/upgrade/drupal-6.user-no-password-token.database.php',
    );
    parent::setUp();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.user.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
