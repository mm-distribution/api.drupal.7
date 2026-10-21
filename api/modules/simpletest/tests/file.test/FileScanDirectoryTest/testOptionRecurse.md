# FileScanDirectoryTest::testOptionRecurse()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1363–1369 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1363-L1369)
- **Class:** [FileScanDirectoryTest](../FileScanDirectoryTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testOptionRecurse()
```

## Documentation

```text
Check that the recurse option decends into subdirectories.
```

## Code

```php
  function testOptionRecurse() {
    $files = file_scan_directory(drupal_get_path('module', 'simpletest'), '/^javascript-/', array('recurse' => FALSE));
    $this->assertTrue(empty($files), "Without recursion couldn't find javascript files.");

    $files = file_scan_directory(drupal_get_path('module', 'simpletest'), '/^javascript-/', array('recurse' => TRUE));
    $this->assertEqual(2, count($files), 'With recursion we found the expected javascript files.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
