# CommonSizeTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/common.test`](_file.md), lines 591–686 · [local source](../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L591-L686)
- **Module/theme:** batch_test

## Signature

```php
class CommonSizeTestCase extends DrupalUnitTestCase
```

## Documentation

```text
Tests file size parsing and formatting functions.
```

## Properties

### $exact_test_cases

```php
protected $exact_test_cases;
```

### $rounded_test_cases

```php
protected $rounded_test_cases;
```

## Methods (derived index)

- [getInfo()](CommonSizeTestCase/getInfo.md)
- [setUp()](CommonSizeTestCase/setUp.md)
- [testCommonFormatSize()](CommonSizeTestCase/testCommonFormatSize.md) — Check that format_size() returns the expected string.
- [testCommonParseSize()](CommonSizeTestCase/testCommonParseSize.md) — Check that parse_size() returns the proper byte sizes.
- [testCommonParseSizeFormatSize()](CommonSizeTestCase/testCommonParseSizeFormatSize.md) — Cross-test parse_size() and format_size().

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
