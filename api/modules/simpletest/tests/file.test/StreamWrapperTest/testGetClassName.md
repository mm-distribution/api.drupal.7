# StreamWrapperTest::testGetClassName()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 3007–3012 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L3007-L3012)
- **Class:** [StreamWrapperTest](../StreamWrapperTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testGetClassName()
```

## Documentation

```text
Test the getClassName() function.
```

## Code

```php
  function testGetClassName() {
    // Check the dummy scheme.
    $this->assertEqual($this->classname, file_stream_wrapper_get_class($this->scheme), 'Got correct class name for dummy scheme.');
    // Check core's scheme.
    $this->assertEqual('DrupalPublicStreamWrapper', file_stream_wrapper_get_class('public'), 'Got correct class name for public scheme.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
