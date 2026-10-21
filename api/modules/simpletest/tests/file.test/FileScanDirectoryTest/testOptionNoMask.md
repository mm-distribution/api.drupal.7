# FileScanDirectoryTest::testOptionNoMask()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1321–1329 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1321-L1329)
- **Class:** [FileScanDirectoryTest](../FileScanDirectoryTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testOptionNoMask()
```

## Documentation

```text
Check that the no-mask parameter is honored.
```

## Code

```php
  function testOptionNoMask() {
    // Grab a listing of all the JavaSscript files.
    $all_files = file_scan_directory($this->path, '/^javascript-/');
    $this->assertEqual(2, count($all_files), 'Found two, expected javascript files.');

    // Now use the nomast parameter to filter out the .script file.
    $filtered_files = file_scan_directory($this->path, '/^javascript-/', array('nomask' => '/.script$/'));
    $this->assertEqual(1, count($filtered_files), 'Filtered correctly.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
