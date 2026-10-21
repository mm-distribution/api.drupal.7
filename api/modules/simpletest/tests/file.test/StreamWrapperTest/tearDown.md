# StreamWrapperTest::tearDown()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2999–3002 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2999-L3002)
- **Class:** [StreamWrapperTest](../StreamWrapperTest.md)
- **Module/theme:** batch_test

## Signature

```php
function tearDown()
```

## Documentation

_No docblock in source._

## Code

```php
  function tearDown() {
    parent::tearDown();
    stream_wrapper_unregister($this->scheme);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
