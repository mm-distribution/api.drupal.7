# UnicodeUnitTest::testMbStringUnicode()

- **Type:** Method
- **File:** [`modules/simpletest/tests/unicode.test`](../_file.md), lines 31–51 · [local source](../../../../../../source/modules/simpletest/tests/unicode.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test#L31-L51)
- **Class:** [UnicodeUnitTest](../UnicodeUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testMbStringUnicode()
```

## Documentation

```text
Test full unicode features implemented using the mbstring extension.
```

## Code

```php
  function testMbStringUnicode() {
    global $multibyte;

    // mbstring was not detected on this installation, there is no way to test
    // multibyte features. Treat that as an exception.
    if ($multibyte == UNICODE_SINGLEBYTE) {
      $this->error(t('Unable to test Multibyte features: mbstring extension was not detected.'));
    }

    $multibyte = UNICODE_MULTIBYTE;

    $this->extendedMode = TRUE;
    $this->pass(t('Testing in mbstring mode'));

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
