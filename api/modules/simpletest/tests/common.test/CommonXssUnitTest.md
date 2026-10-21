# CommonXssUnitTest

- **Type:** Class
- **File:** [`modules/simpletest/tests/common.test`](_file.md), lines 489–586 · [local source](../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L489-L586)
- **Module/theme:** batch_test

## Signature

```php
class CommonXssUnitTest extends DrupalUnitTestCase
```

## Documentation

```text
Tests for check_plain(), filter_xss(), format_string(), and check_url().
```

## Methods (derived index)

- [getInfo()](CommonXssUnitTest/getInfo.md)
- [testInvalidMultiByte()](CommonXssUnitTest/testInvalidMultiByte.md) — Check that invalid multi-byte sequences are rejected.
- [testEscaping()](CommonXssUnitTest/testEscaping.md) — Check that special characters are escaped.
- [testFormatStringAndT()](CommonXssUnitTest/testFormatStringAndT.md) — Test t() and format_string() replacement functionality.
- [testBadProtocolStripping()](CommonXssUnitTest/testBadProtocolStripping.md) — Check that harmful protocols are stripped.

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
