# FileDirectoryTest::testFileCreateNewFilepath()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1158–1184 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1158-L1184)
- **Class:** [FileDirectoryTest](../FileDirectoryTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFileCreateNewFilepath()
```

## Documentation

```text
This will take a directory and path, and find a valid filepath that is not
taken by another file.
```

## Code

```php
  function testFileCreateNewFilepath() {
    // First we test against an imaginary file that does not exist in a
    // directory.
    $basename = 'xyz.txt';
    $directory = 'misc';
    $original = $directory . '/' . $basename;
    $path = file_create_filename($basename, $directory);
    $this->assertEqual($path, $original, format_string('New filepath %new equals %original.', array('%new' => $path, '%original' => $original)), 'File');

    // Then we test against a file that already exists within that directory.
    $basename = 'druplicon.png';
    $original = $directory . '/' . $basename;
    $expected = $directory . '/druplicon_0.png';
    $path = file_create_filename($basename, $directory);
    $this->assertEqual($path, $expected, format_string('Creating a new filepath from %original equals %new.', array('%new' => $path, '%original' => $original)), 'File');

    try {
      $filename = "a\xFFtest\x80€.txt";
      file_create_filename($filename, $directory);
      $this->fail('Expected exception not thrown');
    }
    catch (RuntimeException $e) {
      $this->assertEqual("Invalid filename '$filename'", $e->getMessage(), 'The invalid filename has been detected and RuntimeException has been thrown.');
    }

    // @TODO: Finally we copy a file into a directory several times, to ensure a properly iterating filename suffix.
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
