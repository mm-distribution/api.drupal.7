# DrupalWebTestCase::resetAll()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1904–1921 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1904-L1921)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function resetAll()
```

## Documentation

```text
Reset all data structures after having enabled new modules.

This method is called by DrupalWebTestCase::setUp() after enabling
the requested modules. It must be called again when additional modules
are enabled later.
```

## Code

```php
  protected function resetAll() {
    // Reset all static variables.
    drupal_static_reset();
    // Reset the list of enabled modules.
    module_list(TRUE);

    // Reset cached schema for new database prefix. This must be done before
    // drupal_flush_all_caches() so rebuilds can make use of the schema of
    // modules enabled on the cURL side.
    drupal_get_schema(NULL, TRUE);

    // Perform rebuilds and flush remaining caches.
    drupal_flush_all_caches();

    // Reload global $conf array and permissions.
    $this->refreshVariables();
    $this->checkPermissions(array(), TRUE);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
