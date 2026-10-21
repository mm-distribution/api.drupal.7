# BootstrapGetFilenameTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/bootstrap.test`](_file.md), lines 419–496 · [local source](../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L419-L496)
- **Module/theme:** batch_test

## Signature

```php
class BootstrapGetFilenameTestCase extends DrupalUnitTestCase
```

## Documentation

```text
Test drupal_get_filename()'s availability.
```

## Properties

### $getFilenameTestTriggeredError

```php
protected $getFilenameTestTriggeredError;
```

```text
The last file-related error message triggered by the filename test.

Used by BootstrapGetFilenameTestCase::testDrupalGetFilename().
```

## Methods (derived index)

- [getInfo()](BootstrapGetFilenameTestCase/getInfo.md)
- [testDrupalGetFilename()](BootstrapGetFilenameTestCase/testDrupalGetFilename.md) — Test that drupal_get_filename() works correctly when the file is not found in the database.
- [fileNotFoundErrorHandler()](BootstrapGetFilenameTestCase/fileNotFoundErrorHandler.md) — Skips handling of "file not found" errors.

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
