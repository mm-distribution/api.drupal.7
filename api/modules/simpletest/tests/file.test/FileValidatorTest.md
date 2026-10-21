# FileValidatorTest

- **Type:** Class
- **File:** [`modules/simpletest/tests/file.test`](_file.md), lines 365–509 · [local source](../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L365-L509)
- **Module/theme:** batch_test

## Signature

```php
class FileValidatorTest extends DrupalWebTestCase
```

## Documentation

```text
 This will run tests against the file validation functions (file_validate_*).
```

## Properties

### $image

```php
protected $image;
```

### $non_image

```php
protected $non_image;
```

## Methods (derived index)

- [getInfo()](FileValidatorTest/getInfo.md)
- [setUp()](FileValidatorTest/setUp.md)
- [testFileValidateExtensions()](FileValidatorTest/testFileValidateExtensions.md) — Test the file_validate_extensions() function.
- [testFileValidateIsImage()](FileValidatorTest/testFileValidateIsImage.md) — This ensures a specific file is actually an image.
- [testFileValidateImageResolution()](FileValidatorTest/testFileValidateImageResolution.md) — This ensures the resolution of a specific file is within bounds. The image will be resized if it's too large.
- [testFileValidateNameLength()](FileValidatorTest/testFileValidateNameLength.md) — This will ensure the filename length is valid.
- [testFileValidateSize()](FileValidatorTest/testFileValidateSize.md) — Test file_validate_size().

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
