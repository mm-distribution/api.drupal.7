# UpgradePathTaxonomyTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.taxonomy.test`](../_file.md), lines 15–21 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.taxonomy.test#L15-L21)
- **Class:** [UpgradePathTaxonomyTestCase](../UpgradePathTaxonomyTestCase.md)
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
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
