# CacheSavingCase::testNoEmptyCids()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 166–169 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L166-L169)
- **Class:** [CacheSavingCase](../CacheSavingCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testNoEmptyCids()
```

## Documentation

```text
Test no empty cids are written in cache table.
```

## Code

```php
  function testNoEmptyCids() {
    $this->drupalGet('user/register');
    $this->assertFalse(cache_get(''), 'No cache entry is written with an empty cid.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
