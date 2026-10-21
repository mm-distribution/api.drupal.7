# DrupalWebTestCase::storeSetupCache()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1578–1607 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1578-L1607)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function storeSetupCache($cache_key_prefix = '')
```

## Documentation

```text
Store the installation setup to a cache.

@param string $cache_key_prefix
  (optional) Additional prefix for the cache key.

@return bool
  TRUE if the installation was stored in the cache, FALSE otherwise.
```

## Code

```php
  protected function storeSetupCache($cache_key_prefix = '') {
    $cache_key = $this->getSetupCacheKey($cache_key_prefix);
    $lock_key = 'simpletest_store_cache_' . $cache_key . '_' . $this->testId;

    // All concurrent tests share the same test id. Therefore it is possible to
    // use the lock to ensure that only one process will store the cache. This
    // is important as else DB tables created by one process could be deleted
    // by another as the cache copying is idempotent.
    if (! lock_acquire($lock_key)) {
      return FALSE;
    }

    // Try to copy the installation to the setup cache - now that we have a
    // lock to do so.
    if (!$this->copySetupCache(substr($this->databasePrefix, 10), $cache_key)) {
      // It is non-fatal if the cache cannot be copied as the next test run
      // will try it again.
      $this->assert('debug', t('Storing cache with key @key failed', array('@key' => $cache_key)), 'storeSetupCache');

      lock_release($lock_key);
      return FALSE;
    }

    // Inform others that this cache is usable now.
    $cache_file = $this->originalFileDirectory . '/simpletest/' . $cache_key . '/simpletest-cache-setup';
    file_put_contents($cache_file, time());

    lock_release($lock_key);
    return TRUE;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
