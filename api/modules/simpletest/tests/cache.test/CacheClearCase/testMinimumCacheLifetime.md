# CacheClearCase::testMinimumCacheLifetime()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 356–385 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L356-L385)
- **Class:** [CacheClearCase](../CacheClearCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMinimumCacheLifetime()
```

## Documentation

```text
Test minimum cache lifetime.
```

## Code

```php
  function testMinimumCacheLifetime() {
    // Set a minimum/maximum cache lifetime.
    $this->setupLifetime(300);
    // Login as a newly-created user.
    $account = $this->drupalCreateUser(array());
    $this->drupalLogin($account);

    // Set two cache objects in different bins.
    $data = $this->randomName(100);
    cache_set($data, $data, 'cache', CACHE_TEMPORARY);
    $cached = cache_get($data);
    $this->assertTrue(isset($cached->data) && $cached->data === $data, 'Cached item retrieved.');
    cache_set($data, $data, 'cache_page', CACHE_TEMPORARY);

    // Expire temporary items in the 'page' bin.
    cache_clear_all(NULL, 'cache_page');

    // Since the database cache uses REQUEST_TIME, set the $_SESSION variable
    // manually to force it to the current time.
    $_SESSION['cache_expiration']['cache_page'] = time();

    // Items in the default cache bin should not be expired.
    $cached = cache_get($data);
    $this->assertTrue(isset($cached->data) && $cached->data == $data, 'Cached item retrieved');

    // Despite the minimum cache lifetime, the item in the 'page' bin should
    // be invalidated for the current user.
    $cached = cache_get($data, 'cache_page');
    $this->assertFalse($cached, 'Cached item was invalidated');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
