# FileSaveUploadTest

- **Type:** Class
- **File:** [`modules/simpletest/tests/file.test`](_file.md), lines 565–1047 · [local source](../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L565-L1047)
- **Module/theme:** batch_test

## Signature

```php
class FileSaveUploadTest extends FileHookTestCase
```

## Documentation

```text
Test the file_save_upload() function.
```

## Properties

### $image

```php
protected $image;
```

```text
An image file path for uploading.
```

### $phpfile

```php
protected $phpfile;
```

```text
A PHP file path for upload security testing.
```

### $maxFidBefore

```php
protected $maxFidBefore;
```

```text
The largest file id when the test starts.
```

### $image_extension

```php
protected $image_extension;
```

```text
An image extension.
```

## Methods (derived index)

- [getInfo()](FileSaveUploadTest/getInfo.md)
- [setUp()](FileSaveUploadTest/setUp.md)
- [testNormal()](FileSaveUploadTest/testNormal.md) — Test the file_save_upload() function.
- [testHandleExtension()](FileSaveUploadTest/testHandleExtension.md) — Test extension handling.
- [testHandleDangerousFile()](FileSaveUploadTest/testHandleDangerousFile.md) — Test dangerous file handling.
- [testHandleFileMunge()](FileSaveUploadTest/testHandleFileMunge.md) — Test file munge handling.
- [testExistingRename()](FileSaveUploadTest/testExistingRename.md) — Test renaming when uploading over a file that already exists.
- [testExistingReplace()](FileSaveUploadTest/testExistingReplace.md) — Test replacement when uploading over a file that already exists.
- [testExistingError()](FileSaveUploadTest/testExistingError.md) — Test for failure when uploading over a file that already exists.
- [testNoUpload()](FileSaveUploadTest/testNoUpload.md) — Test for no failures when not uploading a file.

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
