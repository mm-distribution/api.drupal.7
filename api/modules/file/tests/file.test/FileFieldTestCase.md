# FileFieldTestCase

- **Type:** Class
- **File:** [`modules/file/tests/file.test`](_file.md), lines 11–245 · [local source](../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L11-L245)
- **Module/theme:** file_module_test

## Signature

```php
class FileFieldTestCase extends DrupalWebTestCase
```

## Documentation

```text
Provides methods specifically for testing File module's field handling.
```

## Properties

### $admin_user

```php
protected $admin_user;
```

## Methods (derived index)

- [setUp()](FileFieldTestCase/setUp.md)
- [getTestFile()](FileFieldTestCase/getTestFile.md) — Retrieves a sample file of the specified type.
- [getLastFileId()](FileFieldTestCase/getLastFileId.md) — Retrieves the fid of the last inserted file.
- [createFileField()](FileFieldTestCase/createFileField.md) — Creates a new file field.
- [attachFileField()](FileFieldTestCase/attachFileField.md) — Attaches a file field to an entity.
- [updateFileField()](FileFieldTestCase/updateFileField.md) — Updates an existing file field with new settings.
- [uploadNodeFile()](FileFieldTestCase/uploadNodeFile.md) — Uploads a file to a node.
- [removeNodeFile()](FileFieldTestCase/removeNodeFile.md) — Removes a file from a node.
- [replaceNodeFile()](FileFieldTestCase/replaceNodeFile.md) — Replaces a file within a node.
- [assertFileExists()](FileFieldTestCase/assertFileExists.md) — Asserts that a file exists physically on disk.
- [assertFileEntryExists()](FileFieldTestCase/assertFileEntryExists.md) — Asserts that a file exists in the database.
- [assertFileNotExists()](FileFieldTestCase/assertFileNotExists.md) — Asserts that a file does not exist on disk.
- [assertFileEntryNotExists()](FileFieldTestCase/assertFileEntryNotExists.md) — Asserts that a file does not exist in the database.
- [assertFileIsPermanent()](FileFieldTestCase/assertFileIsPermanent.md) — Asserts that a file's status is set to permanent in the database.
- [createTemporaryFile()](FileFieldTestCase/createTemporaryFile.md) — Creates a temporary file, for a specific user.

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
