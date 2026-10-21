# DrupalWebTestCase::getSetupCacheKey()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1562–1567 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1562-L1567)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function getSetupCacheKey($cache_key_prefix = '')
```

## Documentation

```text
Returns the cache key used for the setup caching.

@param string $cache_key_prefix
  (optional) Additional prefix for the cache key.

@return string
  The cache key to use, by default only based on the profile used by the
  test.
```

## Code

```php
  protected function getSetupCacheKey($cache_key_prefix = '') {
    // The cache key needs to start with a numeric character, so that the cached
    // installation gets cleaned up properly.
    $cache_key_prefix = hash('crc32b', $cache_key_prefix . $this->profile);
    return '1c' . $cache_key_prefix;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
