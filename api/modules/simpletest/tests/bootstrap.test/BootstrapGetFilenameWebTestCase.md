# BootstrapGetFilenameWebTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/bootstrap.test`](_file.md), lines 501–663 · [local source](../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L501-L663)
- **Module/theme:** batch_test

## Signature

```php
class BootstrapGetFilenameWebTestCase extends DrupalWebTestCase
```

## Documentation

```text
Test drupal_get_filename() in the context of a full Drupal installation.
```

## Properties

### $getFilenameTestTriggeredError

```php
protected $getFilenameTestTriggeredError;
```

```text
The last file-related error message triggered by the filename test.

Used by BootstrapGetFilenameWebTestCase::testDrupalGetFilename().
```

## Methods (derived index)

- [getInfo()](BootstrapGetFilenameWebTestCase/getInfo.md)
- [setUp()](BootstrapGetFilenameWebTestCase/setUp.md)
- [testDrupalGetFilename()](BootstrapGetFilenameWebTestCase/testDrupalGetFilename.md) — Test that drupal_get_filename() works correctly with a full Drupal site.
- [fileNotFoundErrorHandler()](BootstrapGetFilenameWebTestCase/fileNotFoundErrorHandler.md) — Skips handling of "file not found" errors.
- [testWatchdog()](BootstrapGetFilenameWebTestCase/testWatchdog.md) — Test that watchdog messages about missing files are correctly recorded.
- [testRecursiveRebuilds()](BootstrapGetFilenameWebTestCase/testRecursiveRebuilds.md) — Test that drupal_get_filename() does not break recursive rebuilds.

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
