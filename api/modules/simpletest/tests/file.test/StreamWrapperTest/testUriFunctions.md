# StreamWrapperTest::testUriFunctions()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 3028–3046 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L3028-L3046)
- **Class:** [StreamWrapperTest](../StreamWrapperTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testUriFunctions()
```

## Documentation

```text
Test the URI and target functions.
```

## Code

```php
  function testUriFunctions() {
    $instance = file_stream_wrapper_get_instance_by_uri($this->scheme . '://foo');
    $this->assertEqual($this->classname, get_class($instance), 'Got correct class type for dummy URI.');

    $instance = file_stream_wrapper_get_instance_by_uri('public://foo');
    $this->assertEqual('DrupalPublicStreamWrapper', get_class($instance), 'Got correct class type for public URI.');

    // Test file_uri_target().
    $this->assertEqual(file_uri_target('public://foo/bar.txt'), 'foo/bar.txt', 'Got a valid stream target from public://foo/bar.txt.');
    $this->assertFalse(file_uri_target('foo/bar.txt'), 'foo/bar.txt is not a valid stream.');

    // Test file_build_uri() and DrupalLocalStreamWrapper::getDirectoryPath().
    $this->assertEqual(file_build_uri('foo/bar.txt'), 'public://foo/bar.txt', 'Expected scheme was added.');
    $this->assertEqual(file_stream_wrapper_get_instance_by_scheme('public')->getDirectoryPath(), variable_get('file_public_path'), 'Expected default directory path was returned.');
    $this->assertEqual(file_stream_wrapper_get_instance_by_scheme('temporary')->getDirectoryPath(), variable_get('file_temporary_path'), 'Expected temporary directory path was returned.');

    variable_set('file_default_scheme', 'private');
    $this->assertEqual(file_build_uri('foo/bar.txt'), 'private://foo/bar.txt', 'Got a valid URI from foo/bar.txt.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
