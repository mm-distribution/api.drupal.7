# StreamWrapperTest::testPharFile()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 3086–3115 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L3086-L3115)
- **Class:** [StreamWrapperTest](../StreamWrapperTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function testPharFile()
```

## Documentation

```text
Tests that only valid phar files can be used.
```

## Code

```php
  public function testPharFile() {
    if (!in_array('phar', stream_get_wrappers(), TRUE)) {
      $this->pass('There is no phar stream wrapper registered.');
      // Nothing else in this test is relevant when there's no phar stream
      // wrapper. testPharStreamWrapperRegistration() is sufficient for testing
      // the conditions of when the stream wrapper should or should not be
      // registered.
      return;
    }

    $base = dirname(dirname(__FILE__)) . '/files';

    // Ensure that file operations via the phar:// stream wrapper work for phar
    // files with the .phar extension.
    $this->assertFalse(file_exists("phar://$base/phar-1.phar/no-such-file.php"));
    $this->assertTrue(file_exists("phar://$base/phar-1.phar/index.php"));
    $file_contents = file_get_contents("phar://$base/phar-1.phar/index.php");
    $expected_hash = 'c7e7904ea573c5ebea3ef00bb08c1f86af1a45961fbfbeb1892ff4a98fd73ad5';
    $this->assertIdentical($expected_hash, hash('sha256', $file_contents));

    // Ensure that file operations via the phar:// stream wrapper throw an
    // exception for files without the .phar extension.
    try {
      file_exists("phar://$base/image-2.jpg/index.php");
      $this->fail('Expected exception failed to be thrown when accessing an invalid phar file.');
    }
    catch (Exception $e) {
      $this->assertEqual(get_class($e), 'TYPO3\PharStreamWrapper\Exception', 'Expected exception thrown when accessing an invalid phar file.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
