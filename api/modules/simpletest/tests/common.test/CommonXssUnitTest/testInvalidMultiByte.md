# CommonXssUnitTest::testInvalidMultiByte()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 502–524 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L502-L524)
- **Class:** [CommonXssUnitTest](../CommonXssUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testInvalidMultiByte()
```

## Documentation

```text
Check that invalid multi-byte sequences are rejected.
```

## Code

```php
  function testInvalidMultiByte() {
     // Ignore PHP 8.0+ null deprecations.
     $text = check_plain(NULL);
     $this->assertEqual($text, '', 'check_plain() casts null to string');
     $text = check_plain(FALSE);
     $this->assertEqual($text, '', 'check_plain() casts boolean to string');
     $text = filter_xss(NULL);
     $this->assertEqual($text, '', 'filter_xss() casts null to string');
     $text = filter_xss(FALSE);
     $this->assertEqual($text, '', 'filter_xss() casts boolean to string');
     // Ignore PHP 5.3+ invalid multibyte sequence warning.
     $text = @check_plain("Foo\xC0barbaz");
     $this->assertEqual($text, '', 'check_plain() rejects invalid sequence "Foo\xC0barbaz"');
     // Ignore PHP 5.3+ invalid multibyte sequence warning.
     $text = @check_plain("\xc2\"");
     $this->assertEqual($text, '', 'check_plain() rejects invalid sequence "\xc2\""');
     $text = check_plain("Fooÿñ");
     $this->assertEqual($text, "Fooÿñ", 'check_plain() accepts valid sequence "Fooÿñ"');
     $text = filter_xss("Foo\xC0barbaz");
     $this->assertEqual($text, '', 'filter_xss() rejects invalid sequence "Foo\xC0barbaz"');
     $text = filter_xss("Fooÿñ");
     $this->assertEqual($text, "Fooÿñ", 'filter_xss() accepts valid sequence Fooÿñ');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
