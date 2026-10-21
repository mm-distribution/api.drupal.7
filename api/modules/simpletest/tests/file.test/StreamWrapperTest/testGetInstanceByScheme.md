# StreamWrapperTest::testGetInstanceByScheme()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 3017–3023 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L3017-L3023)
- **Class:** [StreamWrapperTest](../StreamWrapperTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testGetInstanceByScheme()
```

## Documentation

```text
Test the file_stream_wrapper_get_instance_by_scheme() function.
```

## Code

```php
  function testGetInstanceByScheme() {
    $instance = file_stream_wrapper_get_instance_by_scheme($this->scheme);
    $this->assertEqual($this->classname, get_class($instance), 'Got correct class type for dummy scheme.');

    $instance = file_stream_wrapper_get_instance_by_scheme('public');
    $this->assertEqual('DrupalPublicStreamWrapper', get_class($instance), 'Got correct class type for public scheme.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
