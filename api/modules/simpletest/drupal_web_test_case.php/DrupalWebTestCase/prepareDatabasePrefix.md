# DrupalWebTestCase::prepareDatabasePrefix()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1416–1426 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1416-L1426)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function prepareDatabasePrefix()
```

## Documentation

```text
Generates a database prefix for running tests.

The generated database table prefix is used for the Drupal installation
being performed for the test. It is also used as user agent HTTP header
value by the cURL-based browser of DrupalWebTestCase, which is sent
to the Drupal installation of the test. During early Drupal bootstrap, the
user agent HTTP header is parsed, and if it matches, all database queries
use the database table prefix that has been generated here.

@see DrupalWebTestCase::curlInitialize()
@see drupal_valid_test_ua()
@see DrupalWebTestCase::setUp()
```

## Code

```php
  protected function prepareDatabasePrefix() {
    $this->databasePrefix = 'simpletest' . mt_rand(1000, 1000000);

    // As soon as the database prefix is set, the test might start to execute.
    // All assertions as well as the SimpleTest batch operations are associated
    // with the testId, so the database prefix has to be associated with it.
    db_update('simpletest_test_id')
      ->fields(array('last_prefix' => $this->databasePrefix))
      ->condition('test_id', $this->testId)
      ->execute();
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
