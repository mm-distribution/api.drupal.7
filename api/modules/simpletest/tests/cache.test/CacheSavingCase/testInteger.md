# CacheSavingCase::testInteger()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 122–124 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L122-L124)
- **Class:** [CacheSavingCase](../CacheSavingCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testInteger()
```

## Documentation

```text
Test the saving and restoring of an integer.
```

## Code

```php
  function testInteger() {
    $this->checkVariable(100);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
