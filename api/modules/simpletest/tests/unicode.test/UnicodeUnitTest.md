# UnicodeUnitTest

- **Type:** Class
- **File:** [`modules/simpletest/tests/unicode.test`](_file.md), lines 11–309 · [local source](../../../../../source/modules/simpletest/tests/unicode.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test#L11-L309)
- **Module/theme:** batch_test

## Signature

```php
class UnicodeUnitTest extends DrupalUnitTestCase
```

## Documentation

```text
Test unicode handling features implemented in unicode.inc.
```

## Properties

### $extendedMode

```php
protected $extendedMode = FALSE;
```

```text
Whether to run the extended version of the tests (including non latin1 characters).

@var boolean
```

## Methods (derived index)

- [getInfo()](UnicodeUnitTest/getInfo.md)
- [testMbStringUnicode()](UnicodeUnitTest/testMbStringUnicode.md) — Test full unicode features implemented using the mbstring extension.
- [testEmulatedUnicode()](UnicodeUnitTest/testEmulatedUnicode.md) — Test emulated unicode features.
- [helperTestStrToLower()](UnicodeUnitTest/helperTestStrToLower.md)
- [helperTestStrToUpper()](UnicodeUnitTest/helperTestStrToUpper.md)
- [helperTestUcFirst()](UnicodeUnitTest/helperTestUcFirst.md)
- [helperTestStrLen()](UnicodeUnitTest/helperTestStrLen.md)
- [helperTestSubStr()](UnicodeUnitTest/helperTestSubStr.md)
- [testDecodeEntities()](UnicodeUnitTest/testDecodeEntities.md) — Test decode_entities().
- [helperTestTruncate()](UnicodeUnitTest/helperTestTruncate.md) — Tests truncate_utf8().
- [runTruncateTests()](UnicodeUnitTest/runTruncateTests.md) — Runs test cases for helperTestTruncate().

---
_Drupal 7.103 · [modules/simpletest/tests/unicode.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test) · Licensed GPL-2.0-or-later (see LICENSE)._
