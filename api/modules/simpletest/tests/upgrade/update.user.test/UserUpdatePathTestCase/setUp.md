# UserUpdatePathTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/update.user.test`](../_file.md), lines 20–26 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/update.user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.user.test#L20-L26)
- **Class:** [UserUpdatePathTestCase](../UserUpdatePathTestCase.md)
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
    $this->databaseDumpFiles = array(
      drupal_get_path('module', 'simpletest') . '/tests/upgrade/drupal-7.filled.standard_all.database.php.gz',
    );
    parent::setUp();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/update.user.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
