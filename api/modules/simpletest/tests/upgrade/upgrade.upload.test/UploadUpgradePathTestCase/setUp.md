# UploadUpgradePathTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.upload.test`](../_file.md), lines 15–26 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.upload.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.upload.test#L15-L26)
- **Class:** [UploadUpgradePathTestCase](../UploadUpgradePathTestCase.md)
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
      drupal_get_path('module', 'simpletest') . '/tests/upgrade/drupal-6.upload.database.php',
    );
    parent::setUp();
    // Set a small batch size to test multiple iterations of the batch.
    $this->variable_set('upload_update_batch_size', 2);

    $this->uninstallModulesExcept(array('upload'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.upload.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.upload.test) · Licensed GPL-2.0-or-later (see LICENSE)._
