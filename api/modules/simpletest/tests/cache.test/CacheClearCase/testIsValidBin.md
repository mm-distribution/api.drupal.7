# CacheClearCase::testIsValidBin()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 332–351 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L332-L351)
- **Class:** [CacheClearCase](../CacheClearCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testIsValidBin()
```

## Documentation

```text
Test DrupalDatabaseCache::isValidBin().
```

## Code

```php
  function testIsValidBin() {
    // Retrieve existing cache bins.
    $valid_bins = array('cache', 'cache_filter', 'cache_page', 'cache_boostrap', 'cache_path');
    $valid_bins = array_merge(module_invoke_all('flush_caches'), $valid_bins);
    foreach ($valid_bins as $id => $bin) {
      $cache = _cache_get_object($bin);
      if ($cache instanceof DrupalDatabaseCache) {
        $this->assertTrue($cache->isValidBin(), format_string('Cache bin @bin is valid.', array('@bin' => $bin)));
      }
    }

    // Check for non-cache tables and invalid bins.
    $invalid_bins = array('block', 'filter', 'missing_table', $this->randomName());
    foreach ($invalid_bins as $id => $bin) {
      $cache = _cache_get_object($bin);
      if ($cache instanceof DrupalDatabaseCache) {
        $this->assertFalse($cache->isValidBin(), format_string('Cache bin @bin is not valid.', array('@bin' => $bin)));
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
