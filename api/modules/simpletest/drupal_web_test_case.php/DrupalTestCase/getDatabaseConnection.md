# DrupalTestCase::getDatabaseConnection()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 213–224 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L213-L224)
- **Class:** [DrupalTestCase](../DrupalTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
public static function getDatabaseConnection()
```

## Documentation

```text
Returns the database connection to the site running Simpletest.

@return DatabaseConnection
  The database connection to use for inserting assertions.
```

## Code

```php
  public static function getDatabaseConnection() {
    try {
      $connection = Database::getConnection('default', 'simpletest_original_default');
    }
    catch (DatabaseConnectionNotDefinedException $e) {
      // If the test was not set up, the simpletest_original_default
      // connection does not exist.
      $connection = Database::getConnection('default', 'default');
    }

    return $connection;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
