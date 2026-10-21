# FileScanDirectory

- **Type:** Class
- **File:** [`modules/file/tests/file.test`](_file.md), lines 1951–2003 · [local source](../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1951-L2003)
- **Module/theme:** file_module_test

## Signature

```php
class FileScanDirectory extends FileFieldTestCase
```

## Documentation

```text
Tests the file_scan_directory() function.
```

## Properties

### $path

```php
protected $path;
```

```text
@var string
```

## Methods (derived index)

- [getInfo()](FileScanDirectory/getInfo.md) — {@inheritdoc}
- [setUp()](FileScanDirectory/setUp.md) — {@inheritdoc}
- [testNoMask()](FileScanDirectory/testNoMask.md) — Tests file_scan_directory() obeys 'file_scan_ignore_directories' setting. If nomask is not passed as argument, it should use the default settings. If nomask is passed as argument, it should obey this rule.

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
