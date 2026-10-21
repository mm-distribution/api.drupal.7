# FileScanDirectoryTest::testReturn()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1276–1296 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1276-L1296)
- **Class:** [FileScanDirectoryTest](../FileScanDirectoryTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testReturn()
```

## Documentation

```text
Check the format of the returned values.
```

## Code

```php
  function testReturn() {
    // Grab a listing of all the JavaSscript files and check that they're
    // passed to the callback.
    $all_files = file_scan_directory($this->path, '/^javascript-/');
    ksort($all_files);
    $this->assertEqual(2, count($all_files), 'Found two, expected javascript files.');

    // Check the first file.
    $file = reset($all_files);
    $this->assertEqual(key($all_files), $file->uri, 'Correct array key was used for the first returned file.');
    $this->assertEqual($file->uri, $this->path . '/javascript-1.txt', 'First file name was set correctly.');
    $this->assertEqual($file->filename, 'javascript-1.txt', 'First basename was set correctly');
    $this->assertEqual($file->name, 'javascript-1', 'First name was set correctly.');

    // Check the second file.
    $file = next($all_files);
    $this->assertEqual(key($all_files), $file->uri, 'Correct array key was used for the second returned file.');
    $this->assertEqual($file->uri, $this->path . '/javascript-2.script', 'Second file name was set correctly.');
    $this->assertEqual($file->filename, 'javascript-2.script', 'Second basename was set correctly');
    $this->assertEqual($file->name, 'javascript-2', 'Second name was set correctly.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
