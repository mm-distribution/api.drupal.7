# SystemArchiverTest

- **Type:** Class
- **File:** [`modules/system/system.test`](_file.md), lines 3210–3298 · [local source](../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3210-L3298)
- **Module/theme:** system

## Signature

```php
class SystemArchiverTest extends DrupalWebTestCase
```

## Documentation

```text
Test case for Archiver classes.

Cannot be a DrupalUnitTestCase as it requires access to the db and files.
```

## Methods (derived index)

- [getInfo()](SystemArchiverTest/getInfo.md)
- [testArchiverTarball()](SystemArchiverTest/testArchiverTarball.md) — Tests interacting with a tarball archive.
- [testArchiverOutOfPath()](SystemArchiverTest/testArchiverOutOfPath.md) — Tests out-of-path extraction protection.
- [_testArchiverOutOfPath()](SystemArchiverTest/_testArchiverOutOfPath.md) — Helper to test out-of-path extraction protection.

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
