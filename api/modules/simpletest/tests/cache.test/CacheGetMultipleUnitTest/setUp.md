# CacheGetMultipleUnitTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 185–188 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L185-L188)
- **Class:** [CacheGetMultipleUnitTest](../CacheGetMultipleUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    $this->default_bin = 'cache_page';
    parent::setUp();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
