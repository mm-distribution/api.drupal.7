# FileScanDirectoryTest::testOptionCallback()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1301–1316 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1301-L1316)
- **Class:** [FileScanDirectoryTest](../FileScanDirectoryTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testOptionCallback()
```

## Documentation

```text
Check that the callback function is called correctly.
```

## Code

```php
  function testOptionCallback() {
    // When nothing is matched nothing should be passed to the callback.
    $all_files = file_scan_directory($this->path, '/^NONEXISTINGFILENAME/', array('callback' => 'file_test_file_scan_callback'));
    $this->assertEqual(0, count($all_files), 'No files were found.');
    $results = file_test_file_scan_callback();
    file_test_file_scan_callback_reset();
    $this->assertEqual(0, count($results), 'No files were passed to the callback.');

    // Grab a listing of all the JavaSscript files and check that they're
    // passed to the callback.
    $all_files = file_scan_directory($this->path, '/^javascript-/', array('callback' => 'file_test_file_scan_callback'));
    $this->assertEqual(2, count($all_files), 'Found two, expected javascript files.');
    $results = file_test_file_scan_callback();
    file_test_file_scan_callback_reset();
    $this->assertEqual(2, count($results), 'Files were passed to the callback.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
