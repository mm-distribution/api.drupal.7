# FileDirectoryTest::testFileDestination()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1198–1223 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1198-L1223)
- **Class:** [FileDirectoryTest](../FileDirectoryTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFileDestination()
```

## Documentation

```text
This will test the filepath for a destination based on passed flags and
whether or not the file exists.

If a file exists, file_destination($destination, $replace) will either
return:
- the existing filepath, if $replace is FILE_EXISTS_REPLACE
- a new filepath if FILE_EXISTS_RENAME
- an error (returning FALSE) if FILE_EXISTS_ERROR.
If the file doesn't currently exist, then it will simply return the
filepath.
```

## Code

```php
  function testFileDestination() {
    // First test for non-existent file.
    $destination = 'misc/xyz.txt';
    $path = file_destination($destination, FILE_EXISTS_REPLACE);
    $this->assertEqual($path, $destination, 'Non-existing filepath destination is correct with FILE_EXISTS_REPLACE.', 'File');
    $path = file_destination($destination, FILE_EXISTS_RENAME);
    $this->assertEqual($path, $destination, 'Non-existing filepath destination is correct with FILE_EXISTS_RENAME.', 'File');
    $path = file_destination($destination, FILE_EXISTS_ERROR);
    $this->assertEqual($path, $destination, 'Non-existing filepath destination is correct with FILE_EXISTS_ERROR.', 'File');

    $destination = 'misc/druplicon.png';
    $path = file_destination($destination, FILE_EXISTS_REPLACE);
    $this->assertEqual($path, $destination, 'Existing filepath destination remains the same with FILE_EXISTS_REPLACE.', 'File');
    $path = file_destination($destination, FILE_EXISTS_RENAME);
    $this->assertNotEqual($path, $destination, 'A new filepath destination is created when filepath destination already exists with FILE_EXISTS_RENAME.', 'File');
    $path = file_destination($destination, FILE_EXISTS_ERROR);
    $this->assertEqual($path, FALSE, 'An error is returned when filepath destination already exists with FILE_EXISTS_ERROR.', 'File');

    try {
      file_destination("core/misc/a\xFFtest\x80€.txt", FILE_EXISTS_REPLACE);
      $this->fail('Expected exception not thrown');
    }
    catch (RuntimeException $e) {
      $this->assertEqual("Invalid filename 'a\xFFtest\x80€.txt'", $e->getMessage(), 'The invalid destination has been detected and RuntimeException has been thrown.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
