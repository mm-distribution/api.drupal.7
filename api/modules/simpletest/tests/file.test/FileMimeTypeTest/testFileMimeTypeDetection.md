# FileMimeTypeTest::testFileMimeTypeDetection()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2912–2975 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2912-L2975)
- **Class:** [FileMimeTypeTest](../FileMimeTypeTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function testFileMimeTypeDetection()
```

## Documentation

```text
Test mapping of mimetypes from filenames.
```

## Code

```php
  public function testFileMimeTypeDetection() {
    $prefix = 'public://';

    $test_case = array(
      'test.jar' => 'application/java-archive',
      'test.jpeg' => 'image/jpeg',
      'test.JPEG' => 'image/jpeg',
      'test.jpg' => 'image/jpeg',
      'test.jar.jpg' => 'image/jpeg',
      'test.jpg.jar' => 'application/java-archive',
      'test.pcf.Z' => 'application/x-font',
      'pcf.z' => 'application/octet-stream',
      'jar' => 'application/octet-stream',
      'some.junk' => 'application/octet-stream',
      'foo.file_test_1' => 'madeup/file_test_1',
      'foo.file_test_2' => 'madeup/file_test_2',
      'foo.doc' => 'madeup/doc',
      'test.ogg' => 'audio/ogg',
    );

    // Test using default mappings.
    foreach ($test_case as $input => $expected) {
      // Test stream [URI].
      $output = file_get_mimetype($prefix . $input);
      $this->assertIdentical($output, $expected, format_string('Mimetype for %input is %output (expected: %expected).', array('%input' => $input, '%output' => $output, '%expected' => $expected)));

      // Test normal path equivalent
      $output = file_get_mimetype($input);
      $this->assertIdentical($output, $expected, format_string('Mimetype (using default mappings) for %input is %output (expected: %expected).', array('%input' => $input, '%output' => $output, '%expected' => $expected)));
    }

    // Now test passing in the map.
    $mapping = array(
      'mimetypes' => array(
        0 => 'application/java-archive',
        1 => 'image/jpeg',
      ),
      'extensions' => array(
         'jar' => 0,
         'jpg' => 1,
      )
    );

    $test_case = array(
      'test.jar' => 'application/java-archive',
      'test.jpeg' => 'application/octet-stream',
      'test.jpg' => 'image/jpeg',
      'test.jar.jpg' => 'image/jpeg',
      'test.jpg.jar' => 'application/java-archive',
      'test.pcf.z' => 'application/octet-stream',
      'pcf.z' => 'application/octet-stream',
      'jar' => 'application/octet-stream',
      'some.junk' => 'application/octet-stream',
      'foo.file_test_1' => 'application/octet-stream',
      'foo.file_test_2' => 'application/octet-stream',
      'foo.doc' => 'application/octet-stream',
      'test.ogg' => 'application/octet-stream',
    );

    foreach ($test_case as $input => $expected) {
      $output = file_get_mimetype($input, $mapping);
      $this->assertIdentical($output, $expected, format_string('Mimetype (using passed-in mappings) for %input is %output (expected: %expected).', array('%input' => $input, '%output' => $output, '%expected' => $expected)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
