# CacheSavingCase::testArray()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 136–138 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L136-L138)
- **Class:** [CacheSavingCase](../CacheSavingCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testArray()
```

## Documentation

```text
Test the saving and restoring of an array.
```

## Code

```php
  function testArray() {
    $this->checkVariable(array('drupal1', 'drupal2' => 'drupal3', 'drupal4' => array('drupal5', 'drupal6')));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
