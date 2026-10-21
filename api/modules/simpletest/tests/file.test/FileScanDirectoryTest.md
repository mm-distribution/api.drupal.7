# FileScanDirectoryTest

- **Type:** Class
- **File:** [`modules/simpletest/tests/file.test`](_file.md), lines 1257–1383 · [local source](../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1257-L1383)
- **Module/theme:** batch_test

## Signature

```php
class FileScanDirectoryTest extends FileTestCase
```

## Documentation

```text
Tests the file_scan_directory() function.
```

## Properties

### $path

```php
protected $path;
```

## Methods (derived index)

- [getInfo()](FileScanDirectoryTest/getInfo.md)
- [setUp()](FileScanDirectoryTest/setUp.md)
- [testReturn()](FileScanDirectoryTest/testReturn.md) — Check the format of the returned values.
- [testOptionCallback()](FileScanDirectoryTest/testOptionCallback.md) — Check that the callback function is called correctly.
- [testOptionNoMask()](FileScanDirectoryTest/testOptionNoMask.md) — Check that the no-mask parameter is honored.
- [testOptionKey()](FileScanDirectoryTest/testOptionKey.md) — Check that key parameter sets the return value's key.
- [testOptionRecurse()](FileScanDirectoryTest/testOptionRecurse.md) — Check that the recurse option decends into subdirectories.
- [testOptionMinDepth()](FileScanDirectoryTest/testOptionMinDepth.md) — Check that the min_depth options lets us ignore files in the starting directory.

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
