# HtaccessTest

- **Type:** Class
- **File:** [`modules/system/system.test`](_file.md), lines 3303–3392 · [local source](../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3303-L3392)
- **Module/theme:** system

## Signature

```php
class HtaccessTest extends DrupalWebTestCase
```

## Documentation

```text
Tests .htaccess is working correctly.
```

## Methods (derived index)

- [getInfo()](HtaccessTest/getInfo.md)
- [getProtectedFiles()](HtaccessTest/getProtectedFiles.md) — Get an array of file paths for access testing.
- [testFileAccess()](HtaccessTest/testFileAccess.md) — Iterates over protected files and calls assertNoFileAccess().
- [assertFileAccess()](HtaccessTest/assertFileAccess.md) — Asserts that a file exists and requesting it returns a specific response.

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
