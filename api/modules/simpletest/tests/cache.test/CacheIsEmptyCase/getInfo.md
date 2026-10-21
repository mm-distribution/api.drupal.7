# CacheIsEmptyCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 392–398 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L392-L398)
- **Class:** [CacheIsEmptyCase](../CacheIsEmptyCase.md)
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
      'name' => 'Cache emptiness test',
      'description' => 'Check if a cache bin is empty after performing clear operations.',
      'group' => 'Cache'
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
