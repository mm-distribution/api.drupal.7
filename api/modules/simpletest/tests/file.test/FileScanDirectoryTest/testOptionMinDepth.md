# FileScanDirectoryTest::testOptionMinDepth()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1376–1382 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1376-L1382)
- **Class:** [FileScanDirectoryTest](../FileScanDirectoryTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testOptionMinDepth()
```

## Documentation

```text
Check that the min_depth options lets us ignore files in the starting
directory.
```

## Code

```php
  function testOptionMinDepth() {
    $files = file_scan_directory($this->path, '/^javascript-/', array('min_depth' => 0));
    $this->assertEqual(2, count($files), 'No minimum-depth gets files in current directory.');

    $files = file_scan_directory($this->path, '/^javascript-/', array('min_depth' => 1));
    $this->assertTrue(empty($files), "Minimum-depth of 1 successfully excludes files from current directory.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
