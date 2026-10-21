# DrupalWebTestCase::refreshVariables()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1935–1939 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1935-L1939)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function refreshVariables()
```

## Documentation

```text
Refresh the in-memory set of variables. Useful after a page request is made
that changes a variable in a different thread.

In other words calling a settings page with $this->drupalPost() with a changed
value would update a variable to reflect that change, but in the thread that
made the call (thread running the test) the changed variable would not be
picked up.

This method clears the variables cache and loads a fresh copy from the database
to ensure that the most up-to-date set of variables is loaded.
```

## Code

```php
  protected function refreshVariables() {
    global $conf;
    cache_clear_all('variables', 'cache_bootstrap');
    $conf = variable_initialize();
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
