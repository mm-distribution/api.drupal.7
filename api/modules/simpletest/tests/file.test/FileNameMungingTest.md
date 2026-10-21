# FileNameMungingTest

- **Type:** Class
- **File:** [`modules/simpletest/tests/file.test`](_file.md), lines 2807–2891 · [local source](../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2807-L2891)
- **Module/theme:** batch_test

## Signature

```php
class FileNameMungingTest extends FileTestCase
```

## Documentation

```text
Tests for file_munge_filename() and file_unmunge_filename().
```

## Properties

### $bad_extension

```php
protected $bad_extension;
```

### $name

```php
protected $name;
```

### $name_with_uc_ext

```php
protected $name_with_uc_ext;
```

## Methods (derived index)

- [getInfo()](FileNameMungingTest/getInfo.md)
- [setUp()](FileNameMungingTest/setUp.md)
- [testMunging()](FileNameMungingTest/testMunging.md) — Create a file and munge/unmunge the name.
- [testMungeNullByte()](FileNameMungingTest/testMungeNullByte.md) — Tests munging with a null byte in the filename.
- [testMungeIgnoreInsecure()](FileNameMungingTest/testMungeIgnoreInsecure.md) — If the allow_insecure_uploads variable evaluates to true, the file should come out untouched, no matter how evil the filename.
- [testMungeIgnoreWhitelisted()](FileNameMungingTest/testMungeIgnoreWhitelisted.md) — White listed extensions are ignored by file_munge_filename().
- [testMungeUnsafe()](FileNameMungingTest/testMungeUnsafe.md) — Tests unsafe extensions are munged by file_munge_filename().
- [testUnMunge()](FileNameMungingTest/testUnMunge.md) — Ensure that unmunge gets your name back.

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
