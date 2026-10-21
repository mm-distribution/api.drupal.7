# BlockCacheTestCase

- **Type:** Class
- **File:** [`modules/block/block.test`](_file.md), lines 488–673 · [local source](../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L488-L673)
- **Module/theme:** block

## Signature

```php
class BlockCacheTestCase extends DrupalWebTestCase
```

## Documentation

```text
Test block caching.
```

## Properties

### $admin_user

```php
protected $admin_user;
```

### $normal_user

```php
protected $normal_user;
```

### $normal_user_alt

```php
protected $normal_user_alt;
```

## Methods (derived index)

- [getInfo()](BlockCacheTestCase/getInfo.md)
- [setUp()](BlockCacheTestCase/setUp.md)
- [testCachePerRole()](BlockCacheTestCase/testCachePerRole.md) — Test DRUPAL_CACHE_PER_ROLE.
- [testCacheGlobal()](BlockCacheTestCase/testCacheGlobal.md) — Test DRUPAL_CACHE_GLOBAL.
- [testNoCache()](BlockCacheTestCase/testNoCache.md) — Test DRUPAL_NO_CACHE.
- [testCachePerUser()](BlockCacheTestCase/testCachePerUser.md) — Test DRUPAL_CACHE_PER_USER.
- [testCachePerPage()](BlockCacheTestCase/testCachePerPage.md) — Test DRUPAL_CACHE_PER_PAGE.
- [setCacheMode()](BlockCacheTestCase/setCacheMode.md) — Private helper method to set the test block's cache mode.

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
