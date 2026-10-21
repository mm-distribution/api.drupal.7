# MenuUpgradePathTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.menu.test`](../_file.md), lines 15–24 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.menu.test#L15-L24)
- **Class:** [MenuUpgradePathTestCase](../MenuUpgradePathTestCase.md)
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
      drupal_get_path('module', 'simpletest') . '/tests/upgrade/drupal-6.filled.database.php',
      drupal_get_path('module', 'simpletest') . '/tests/upgrade/drupal-6.menu.database.php',
    );
    parent::setUp();

    $this->uninstallModulesExcept(array('menu'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
