# PollUpgradePathTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.node.test`](../_file.md), lines 109–117 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.node.test#L109-L117)
- **Class:** [PollUpgradePathTestCase](../PollUpgradePathTestCase.md)
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
    );
    parent::setUp();

    $this->uninstallModulesExcept(array('poll'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.node.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
