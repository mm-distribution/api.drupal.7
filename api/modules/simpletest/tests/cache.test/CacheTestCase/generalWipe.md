# CacheTestCase::generalWipe()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 83–89 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L83-L89)
- **Class:** [CacheTestCase](../CacheTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function generalWipe($bin = NULL)
```

## Documentation

```text
Perform the general wipe.
@param $bin
  The bin to perform the wipe on.
```

## Code

```php
  protected function generalWipe($bin = NULL) {
    if ($bin == NULL) {
      $bin = $this->default_bin;
    }

    cache_clear_all(NULL, $bin);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
