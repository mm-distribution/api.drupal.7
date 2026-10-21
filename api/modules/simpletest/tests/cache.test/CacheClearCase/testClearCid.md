# CacheClearCase::testClearCid()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 241–258 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L241-L258)
- **Class:** [CacheClearCase](../CacheClearCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testClearCid()
```

## Documentation

```text
Test clearing using a cid.
```

## Code

```php
  function testClearCid() {
    cache_set('test_cid_clear', $this->default_value, $this->default_bin);

    $this->assertCacheExists(t('Cache was set for clearing cid.'), $this->default_value, 'test_cid_clear');
    cache_clear_all('test_cid_clear', $this->default_bin);

    $this->assertCacheRemoved(t('Cache was removed after clearing cid.'), 'test_cid_clear');

    cache_set('test_cid_clear1', $this->default_value, $this->default_bin);
    cache_set('test_cid_clear2', $this->default_value, $this->default_bin);
    $this->assertTrue($this->checkCacheExists('test_cid_clear1', $this->default_value)
                      && $this->checkCacheExists('test_cid_clear2', $this->default_value),
                      'Two caches were created for checking cid "*" with wildcard false.');
    cache_clear_all('*', $this->default_bin);
    $this->assertTrue($this->checkCacheExists('test_cid_clear1', $this->default_value)
                      && $this->checkCacheExists('test_cid_clear2', $this->default_value),
                      'Two caches still exists after clearing cid "*" with wildcard false.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
