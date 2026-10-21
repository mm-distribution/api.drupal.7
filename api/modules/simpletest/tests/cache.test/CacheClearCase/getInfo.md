# CacheClearCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 223–229 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L223-L229)
- **Class:** [CacheClearCase](../CacheClearCase.md)
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
      'name' => 'Cache clear test',
      'description' => 'Check our clearing is done the proper way.',
      'group' => 'Cache'
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
