# UpgradePathTriggerTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.trigger.test`](../_file.md), lines 19–26 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.trigger.test#L19-L26)
- **Class:** [UpgradePathTriggerTestCase](../UpgradePathTriggerTestCase.md)
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
    // Path to the database dump.
    $this->databaseDumpFiles = array(
      drupal_get_path('module', 'simpletest') . '/tests/upgrade/drupal-6.filled.database.php',
      drupal_get_path('module', 'simpletest') . '/tests/upgrade/drupal-6.trigger.database.php',
    );
    parent::setUp();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
