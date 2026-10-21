# AJAXFormPageCacheTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/ajax.test`](../_file.md), lines 526–530 · [local source](../../../../../../source/modules/simpletest/tests/ajax.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test#L526-L530)
- **Class:** [AJAXFormPageCacheTestCase](../AJAXFormPageCacheTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  public function setUp() {
    parent::setUp();

    variable_set('cache', TRUE);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test) · Licensed GPL-2.0-or-later (see LICENSE)._
