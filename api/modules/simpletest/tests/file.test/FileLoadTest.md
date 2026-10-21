# FileLoadTest

- **Type:** Class
- **File:** [`modules/simpletest/tests/file.test`](_file.md), lines 2111–2189 · [local source](../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2111-L2189)
- **Module/theme:** batch_test

## Signature

```php
class FileLoadTest extends FileHookTestCase
```

## Documentation

```text
Tests the file_load() function.
```

## Methods (derived index)

- [getInfo()](FileLoadTest/getInfo.md)
- [testLoadMissingFid()](FileLoadTest/testLoadMissingFid.md) — Try to load a non-existent file by fid.
- [testLoadMissingFilepath()](FileLoadTest/testLoadMissingFilepath.md) — Try to load a non-existent file by URI.
- [testLoadInvalidStatus()](FileLoadTest/testLoadInvalidStatus.md) — Try to load a non-existent file by status.
- [testSingleValues()](FileLoadTest/testSingleValues.md) — Load a single file and ensure that the correct values are returned.
- [testMultiple()](FileLoadTest/testMultiple.md) — This will test loading file data from the database.

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
