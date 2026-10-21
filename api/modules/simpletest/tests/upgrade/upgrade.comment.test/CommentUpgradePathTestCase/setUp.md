# CommentUpgradePathTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.comment.test`](../_file.md), lines 15–24 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.comment.test#L15-L24)
- **Class:** [CommentUpgradePathTestCase](../CommentUpgradePathTestCase.md)
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
      drupal_get_path('module', 'simpletest') . '/tests/upgrade/drupal-6.comments.database.php',
    );
    parent::setUp();

    $this->uninstallModulesExcept(array('comment'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.comment.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
