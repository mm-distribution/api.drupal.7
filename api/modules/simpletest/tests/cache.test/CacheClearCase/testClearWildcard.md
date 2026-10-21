# CacheClearCase::testClearWildcard()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 263–283 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L263-L283)
- **Class:** [CacheClearCase](../CacheClearCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testClearWildcard()
```

## Documentation

```text
Test clearing using wildcard.
```

## Code

```php
  function testClearWildcard() {
    cache_set('test_cid_clear1', $this->default_value, $this->default_bin);
    cache_set('test_cid_clear2', $this->default_value, $this->default_bin);
    $this->assertTrue($this->checkCacheExists('test_cid_clear1', $this->default_value)
                      && $this->checkCacheExists('test_cid_clear2', $this->default_value),
                      'Two caches were created for checking cid "*" with wildcard true.');
    cache_clear_all('*', $this->default_bin, TRUE);
    $this->assertFalse($this->checkCacheExists('test_cid_clear1', $this->default_value)
                      || $this->checkCacheExists('test_cid_clear2', $this->default_value),
                      'Two caches removed after clearing cid "*" with wildcard true.');

    cache_set('test_cid_clear1', $this->default_value, $this->default_bin);
    cache_set('test_cid_clear2', $this->default_value, $this->default_bin);
    $this->assertTrue($this->checkCacheExists('test_cid_clear1', $this->default_value)
                      && $this->checkCacheExists('test_cid_clear2', $this->default_value),
                      'Two caches were created for checking cid substring with wildcard true.');
    cache_clear_all('test_', $this->default_bin, TRUE);
    $this->assertFalse($this->checkCacheExists('test_cid_clear1', $this->default_value)
                      || $this->checkCacheExists('test_cid_clear2', $this->default_value),
                      'Two caches removed after clearing cid substring with wildcard true.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
