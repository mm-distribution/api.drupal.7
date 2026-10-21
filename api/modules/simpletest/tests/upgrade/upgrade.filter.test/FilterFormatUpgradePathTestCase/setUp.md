# FilterFormatUpgradePathTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.filter.test`](../_file.md), lines 19–25 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.filter.test#L19-L25)
- **Class:** [FilterFormatUpgradePathTestCase](../FilterFormatUpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    // Path to the database dump.
    $this->databaseDumpFiles = array(
      drupal_get_path('module', 'simpletest') . '/tests/upgrade/drupal-6.filled.database.php',
    );
    parent::setUp();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.filter.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
