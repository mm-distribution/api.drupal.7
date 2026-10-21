# CacheGetMultipleUnitTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 177–183 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L177-L183)
- **Class:** [CacheGetMultipleUnitTest](../CacheGetMultipleUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Fetching multiple cache items',
      'description' => 'Confirm that multiple records are fetched correctly.',
      'group' => 'Cache',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
