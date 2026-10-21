# FieldUpdatePathTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/update.field.test`](../_file.md), lines 20–31 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/update.field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.field.test#L20-L31)
- **Class:** [FieldUpdatePathTestCase](../FieldUpdatePathTestCase.md)
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
    // Use the filled update path and our field data.
    $path = drupal_get_path('module', 'simpletest') . '/tests/upgrade';
    $this->databaseDumpFiles = array(
      $path . '/drupal-7.filled.standard_all.database.php.gz',
      $path . '/drupal-7.field.database.php',
    );
    parent::setUp();

    // Our test data includes poll extra field settings.
    $this->uninstallModulesExcept(array('field', 'poll'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/update.field.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
