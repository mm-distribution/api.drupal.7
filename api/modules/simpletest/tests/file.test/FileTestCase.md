# FileTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/file.test`](_file.md), lines 49–233 · [local source](../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L49-L233)
- **Module/theme:** batch_test

## Signature

```php
class FileTestCase extends DrupalWebTestCase
```

## Documentation

```text
Base class for file tests that adds some additional file specific
assertions and helper functions.
```

## Methods (derived index)

- [assertFileUnchanged()](FileTestCase/assertFileUnchanged.md) — Check that two files have the same values for all fields other than the timestamp.
- [assertDifferentFile()](FileTestCase/assertDifferentFile.md) — Check that two files are not the same by comparing the fid and filepath.
- [assertSameFile()](FileTestCase/assertSameFile.md) — Check that two files are the same by comparing the fid and filepath.
- [assertFilePermissions()](FileTestCase/assertFilePermissions.md) — Helper function to test the permissions of a file.
- [assertDirectoryPermissions()](FileTestCase/assertDirectoryPermissions.md) — Helper function to test the permissions of a directory.
- [createDirectory()](FileTestCase/createDirectory.md) — Create a directory and assert it exists.
- [createFile()](FileTestCase/createFile.md) — Create a file and save it to the files table and assert that it occurs correctly.

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
