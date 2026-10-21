# StreamWrapperTest::testPharStreamWrapperRegistration()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 3062–3081 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L3062-L3081)
- **Class:** [StreamWrapperTest](../StreamWrapperTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function testPharStreamWrapperRegistration()
```

## Documentation

```text
Tests that phar stream wrapper is registered as expected.

@see file_get_stream_wrappers()
```

## Code

```php
  public function testPharStreamWrapperRegistration() {
    if (!class_exists('Phar', FALSE)) {
      $this->assertFalse(in_array('phar', stream_get_wrappers(), TRUE), 'PHP is compiled without phar support. Therefore, no phar stream wrapper is registered.');
    }
    elseif (version_compare(PHP_VERSION, '5.3.3', '<')) {
      $this->assertFalse(in_array('phar', stream_get_wrappers(), TRUE), 'The PHP version is <5.3.3. The built-in phar stream wrapper has been unregistered and not replaced.');
    }
    else {
      $this->assertTrue(in_array('phar', stream_get_wrappers(), TRUE), 'A phar stream wrapper is registered.');
      $this->assertFalse(file_stream_wrapper_valid_scheme('phar'), 'The phar scheme is not a valid scheme for Drupal File API usage.');
    }

    // Ensure that calling file_get_stream_wrappers() multiple times, both
    // without and with a drupal_static_reset() in between, does not create
    // errors due to the PharStreamWrapperManager singleton.
    file_get_stream_wrappers();
    file_get_stream_wrappers();
    drupal_static_reset('file_get_stream_wrappers');
    file_get_stream_wrappers();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
