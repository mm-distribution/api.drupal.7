# DrupalWebTestCase::cronRun()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 2670–2672 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L2670-L2672)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function cronRun()
```

## Documentation

```text
Runs cron in the Drupal installed by Simpletest.
```

## Code

```php
  protected function cronRun() {
    $this->drupalGet($GLOBALS['base_url'] . '/cron.php', array('external' => TRUE, 'query' => array('cron_key' => variable_get('cron_key', 'drupal'))));
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
