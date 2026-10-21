# CacheSavingCase::checkVariable()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 157–161 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L157-L161)
- **Class:** [CacheSavingCase](../CacheSavingCase.md)
- **Module/theme:** batch_test

## Signature

```php
function checkVariable($var)
```

## Documentation

```text
Check or a variable is stored and restored properly.
```

## Code

```php
  function checkVariable($var) {
    cache_set('test_var', $var, 'cache');
    $cache = cache_get('test_var', 'cache');
    $this->assertTrue(isset($cache->data) && $cache->data === $var, format_string('@type is saved and restored properly.', array('@type' => ucfirst(gettype($var)))));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
