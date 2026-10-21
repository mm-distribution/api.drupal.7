# DrupalWebTestCase::changeDatabasePrefix()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1433–1456 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1433-L1456)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function changeDatabasePrefix()
```

## Documentation

```text
Changes the database connection to the prefixed one.

@see DrupalWebTestCase::setUp()
```

## Code

```php
  protected function changeDatabasePrefix() {
    if (empty($this->databasePrefix)) {
      $this->prepareDatabasePrefix();
      // If $this->prepareDatabasePrefix() failed to work, return without
      // setting $this->setupDatabasePrefix to TRUE, so setUp() methods will
      // know to bail out.
      if (empty($this->databasePrefix)) {
        return;
      }
    }

    // Clone the current connection and replace the current prefix.
    $connection_info = Database::getConnectionInfo('default');
    Database::renameConnection('default', 'simpletest_original_default');
    foreach ($connection_info as $target => $value) {
      $connection_info[$target]['prefix'] = array(
        'default' => $value['prefix']['default'] . $this->databasePrefix,
      );
    }
    Database::addConnectionInfo('default', 'default', $connection_info['default']);

    // Indicate the database prefix was set up correctly.
    $this->setupDatabasePrefix = TRUE;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
