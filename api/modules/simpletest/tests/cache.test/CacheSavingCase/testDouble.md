# CacheSavingCase::testDouble()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 129–131 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L129-L131)
- **Class:** [CacheSavingCase](../CacheSavingCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDouble()
```

## Documentation

```text
Test the saving and restoring of a double.
```

## Code

```php
  function testDouble() {
    $this->checkVariable(1.29);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
