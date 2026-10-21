# TriggerUpdatePathTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/update.trigger.test`](../_file.md), lines 19–29 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/update.trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.trigger.test#L19-L29)
- **Class:** [TriggerUpdatePathTestCase](../TriggerUpdatePathTestCase.md)
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
    // Use the filled upgrade path and our trigger data.
    $this->databaseDumpFiles = array(
      drupal_get_path('module', 'simpletest') . '/tests/upgrade/drupal-7.filled.standard_all.database.php.gz',
      drupal_get_path('module', 'simpletest') . '/tests/upgrade/drupal-7.trigger.database.php',
    );
    parent::setUp();

    // Our test data includes node and comment trigger assignments.
    $this->uninstallModulesExcept(array('comment', 'trigger'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/update.trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
