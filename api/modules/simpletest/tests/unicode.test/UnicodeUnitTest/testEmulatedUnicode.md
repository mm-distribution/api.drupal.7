# UnicodeUnitTest::testEmulatedUnicode()

- **Type:** Method
- **File:** [`modules/simpletest/tests/unicode.test`](../_file.md), lines 56–71 · [local source](../../../../../../source/modules/simpletest/tests/unicode.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test#L56-L71)
- **Class:** [UnicodeUnitTest](../UnicodeUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testEmulatedUnicode()
```

## Documentation

```text
Test emulated unicode features.
```

## Code

```php
  function testEmulatedUnicode() {
    global $multibyte;

    $multibyte = UNICODE_SINGLEBYTE;

    $this->extendedMode = FALSE;

    $this->pass(t('Testing in emulated (best-effort) mode'));

    $this->helperTestStrToLower();
    $this->helperTestStrToUpper();
    $this->helperTestUcFirst();
    $this->helperTestStrLen();
    $this->helperTestSubStr();
    $this->helperTestTruncate();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/unicode.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test) · Licensed GPL-2.0-or-later (see LICENSE)._
