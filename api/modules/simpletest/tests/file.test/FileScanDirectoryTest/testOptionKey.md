# FileScanDirectoryTest::testOptionKey()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1334–1358 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1334-L1358)
- **Class:** [FileScanDirectoryTest](../FileScanDirectoryTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testOptionKey()
```

## Documentation

```text
Check that key parameter sets the return value's key.
```

## Code

```php
  function testOptionKey() {
    // "filename", for the path starting with $dir.
    $expected = array($this->path . '/javascript-1.txt', $this->path . '/javascript-2.script');
    $actual = array_keys(file_scan_directory($this->path, '/^javascript-/', array('key' => 'filepath')));
    sort($actual);
    $this->assertEqual($expected, $actual, 'Returned the correct values for the filename key.');

    // "basename", for the basename of the file.
    $expected = array('javascript-1.txt', 'javascript-2.script');
    $actual = array_keys(file_scan_directory($this->path, '/^javascript-/', array('key' => 'filename')));
    sort($actual);
    $this->assertEqual($expected, $actual, 'Returned the correct values for the basename key.');

    // "name" for the name of the file without an extension.
    $expected = array('javascript-1', 'javascript-2');
    $actual = array_keys(file_scan_directory($this->path, '/^javascript-/', array('key' => 'name')));
    sort($actual);
    $this->assertEqual($expected, $actual, 'Returned the correct values for the name key.');

    // Invalid option that should default back to "filename".
    $expected = array($this->path . '/javascript-1.txt', $this->path . '/javascript-2.script');
    $actual = array_keys(file_scan_directory($this->path, '/^javascript-/', array('key' => 'INVALID')));
    sort($actual);
    $this->assertEqual($expected, $actual, 'An invalid key defaulted back to the default.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
