# AggregatorUpdatePathTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/update.aggregator.test`](../_file.md), lines 16–27 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/update.aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.aggregator.test#L16-L27)
- **Class:** [AggregatorUpdatePathTestCase](../AggregatorUpdatePathTestCase.md)
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
    // Use the normal installation and add our feed data.
    $path = drupal_get_path('module', 'simpletest') . '/tests/upgrade';
    $this->databaseDumpFiles = array(
      $path . '/drupal-7.bare.standard_all.database.php.gz',
      $path . '/drupal-7.aggregator.database.php',
    );
    parent::setUp();

    // Our test data only relies on aggregator.module.
    $this->uninstallModulesExcept(array('aggregator'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/update.aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
