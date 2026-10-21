# modules/simpletest/tests/file.test

- **Source:** [local](../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · 3117 lines
- **Module/theme:** batch_test

## File documentation

```text
 @file
 This provides SimpleTests for the core file handling functionality.
 These include FileValidateTest and FileSaveTest.
```

## Functions (derived index)

- [file_test_validator()](file_test_validator.md) — Helper validator that returns the $errors parameter.
- [file_test_file_scan_callback()](file_test_file_scan_callback.md) — Helper function for testing file_scan_directory().
- [file_test_file_scan_callback_reset()](file_test_file_scan_callback_reset.md) — Reset static variables used by file_test_file_scan_callback().

## Classes and interfaces (derived index)

- [FileTestCase](FileTestCase.md) — Base class for file tests that adds some additional file specific assertions and helper functions.
- [FileHookTestCase](FileHookTestCase.md) — Base class for file tests that use the file_test module to test uploads and hooks.
- [FileSpaceUsedTest](FileSpaceUsedTest.md) — This will run tests against the file_space_used() function.
- [FileValidatorTest](FileValidatorTest.md) — This will run tests against the file validation functions (file_validate_*).
- [FileUnmanagedSaveDataTest](FileUnmanagedSaveDataTest.md) — Tests the file_unmanaged_save_data() function.
- [RemoteFileUnmanagedSaveDataTest](RemoteFileUnmanagedSaveDataTest.md) — Tests the file_unmanaged_save_data() function on remote filesystems.
- [FileSaveUploadTest](FileSaveUploadTest.md) — Test the file_save_upload() function.
- [RemoteFileSaveUploadTest](RemoteFileSaveUploadTest.md) — Test the file_save_upload() function on remote filesystems.
- [FileDirectoryTest](FileDirectoryTest.md) — Directory related tests.
- [RemoteFileDirectoryTest](RemoteFileDirectoryTest.md) — Directory related tests.
- [FileScanDirectoryTest](FileScanDirectoryTest.md) — Tests the file_scan_directory() function.
- [RemoteFileScanDirectoryTest](RemoteFileScanDirectoryTest.md) — Tests the file_scan_directory() function on remote filesystems.
- [FileUnmanagedDeleteTest](FileUnmanagedDeleteTest.md) — Deletion related tests.
- [RemoteFileUnmanagedDeleteTest](RemoteFileUnmanagedDeleteTest.md) — Deletion related tests on remote filesystems.
- [FileUnmanagedDeleteRecursiveTest](FileUnmanagedDeleteRecursiveTest.md) — Deletion related tests.
- [RemoteFileUnmanagedDeleteRecursiveTest](RemoteFileUnmanagedDeleteRecursiveTest.md) — Deletion related tests on remote filesystems.
- [FileUnmanagedMoveTest](FileUnmanagedMoveTest.md) — Unmanaged move related tests.
- [RemoteFileUnmanagedMoveTest](RemoteFileUnmanagedMoveTest.md) — Unmanaged move related tests on remote filesystems.
- [FileUnmanagedCopyTest](FileUnmanagedCopyTest.md) — Unmanaged copy related tests.
- [RemoteFileUnmanagedCopyTest](RemoteFileUnmanagedCopyTest.md) — Unmanaged copy related tests on remote filesystems.
- [FileDeleteTest](FileDeleteTest.md) — Deletion related tests.
- [FileMoveTest](FileMoveTest.md) — Move related tests
- [FileCopyTest](FileCopyTest.md) — Copy related tests.
- [FileLoadTest](FileLoadTest.md) — Tests the file_load() function.
- [FileSaveTest](FileSaveTest.md) — Tests the file_save() function.
- [FileUsageTest](FileUsageTest.md) — Tests file usage functions.
- [FileValidateTest](FileValidateTest.md) — Tests the file_validate() function..
- [FileSaveDataTest](FileSaveDataTest.md) — Tests the file_save_data() function.
- [FileDownloadTest](FileDownloadTest.md) — Tests for download/file transfer functions.
- [FileURLRewritingTest](FileURLRewritingTest.md) — Tests for file URL rewriting.
- [FileNameMungingTest](FileNameMungingTest.md) — Tests for file_munge_filename() and file_unmunge_filename().
- [FileMimeTypeTest](FileMimeTypeTest.md) — Tests for file_get_mimetype().
- [StreamWrapperTest](StreamWrapperTest.md) — Tests stream wrapper functions.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
