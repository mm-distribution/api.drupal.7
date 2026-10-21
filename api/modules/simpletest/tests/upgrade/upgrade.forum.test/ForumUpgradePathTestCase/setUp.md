# ForumUpgradePathTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.forum.test`](../_file.md), lines 15–24 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.forum.test#L15-L24)
- **Class:** [ForumUpgradePathTestCase](../ForumUpgradePathTestCase.md)
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
      drupal_get_path('module', 'simpletest') . '/tests/upgrade/drupal-6.forum.database.php',
    );
    parent::setUp();

    $this->uninstallModulesExcept(array('comment', 'forum', 'taxonomy'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.forum.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
