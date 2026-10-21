# DrupalWebTestCase::loadSetupCache()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1541–1550 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1541-L1550)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function loadSetupCache($cache_key_prefix = '')
```

## Documentation

```text
Copies the cached tables and files for a cached installation setup.

@param string $cache_key_prefix
  (optional) Additional prefix for the cache key.

@return bool
  TRUE when the cache was usable and loaded, FALSE when cache was not
  available.

@see DrupalWebTestCase::setUp()
```

## Code

```php
  protected function loadSetupCache($cache_key_prefix = '') {
    $cache_key = $this->getSetupCacheKey($cache_key_prefix);
    $cache_file = $this->originalFileDirectory . '/simpletest/' . $cache_key . '/simpletest-cache-setup';

    if (file_exists($cache_file)) {
      return $this->copySetupCache($cache_key, substr($this->databasePrefix, 10));
    }

    return FALSE;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
