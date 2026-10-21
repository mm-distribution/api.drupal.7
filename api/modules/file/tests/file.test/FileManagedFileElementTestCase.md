# FileManagedFileElementTestCase

- **Type:** Class
- **File:** [`modules/file/tests/file.test`](_file.md), lines 375–529 · [local source](../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L375-L529)
- **Module/theme:** file_module_test

## Signature

```php
class FileManagedFileElementTestCase extends FileFieldTestCase
```

## Documentation

```text
Tests the 'managed_file' element type.

@todo Create a FileTestCase base class and move FileFieldTestCase methods
  that aren't related to fields into it.
```

## Properties

### $originalDisplayErrorsValue

```php
protected $originalDisplayErrorsValue;
```

## Methods (derived index)

- [getInfo()](FileManagedFileElementTestCase/getInfo.md)
- [setUp()](FileManagedFileElementTestCase/setUp.md)
- [tearDown()](FileManagedFileElementTestCase/tearDown.md)
- [testManagedFile()](FileManagedFileElementTestCase/testManagedFile.md) — Tests the managed_file element type.
- [testManagedFileExceedMaximumFileSize()](FileManagedFileElementTestCase/testManagedFileExceedMaximumFileSize.md) — Tests uploading a file that exceeds the maximum file size.
- [_postMaxSizeToInteger()](FileManagedFileElementTestCase/_postMaxSizeToInteger.md) — Converts php.ini post_max_size value to integer.

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
