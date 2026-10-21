# CacheSavingCase::testString()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 115–117 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L115-L117)
- **Class:** [CacheSavingCase](../CacheSavingCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testString()
```

## Documentation

```text
Test the saving and restoring of a string.
```

## Code

```php
  function testString() {
    $this->checkVariable($this->randomName(100));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
