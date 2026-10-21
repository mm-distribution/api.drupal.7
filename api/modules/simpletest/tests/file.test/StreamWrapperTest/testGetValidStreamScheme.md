# StreamWrapperTest::testGetValidStreamScheme()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 3051–3055 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L3051-L3055)
- **Class:** [StreamWrapperTest](../StreamWrapperTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testGetValidStreamScheme()
```

## Documentation

```text
Test the scheme functions.
```

## Code

```php
  function testGetValidStreamScheme() {
    $this->assertEqual('foo', file_uri_scheme('foo://pork//chops'), 'Got the correct scheme from foo://asdf');
    $this->assertTrue(file_stream_wrapper_valid_scheme(file_uri_scheme('public://asdf')), 'Got a valid stream scheme from public://asdf');
    $this->assertFalse(file_stream_wrapper_valid_scheme(file_uri_scheme('foo://asdf')), 'Did not get a valid stream scheme from foo://asdf');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
