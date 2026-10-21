# DrupalHtmlToTextTestCase::testVeryLongLineWrap()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 518–534 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L518-L534)
- **Class:** [DrupalHtmlToTextTestCase](../DrupalHtmlToTextTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testVeryLongLineWrap()
```

## Documentation

```text
Tests that drupal_html_to_text() wraps before 1000 characters.

RFC 3676 says, "The Text/Plain media type is the lowest common
denominator of Internet email, with lines of no more than 998 characters."

RFC 2046 says, "SMTP [RFC-821] allows a maximum of 998 octets before the
next CRLF sequence."

RFC 821 says, "The maximum total length of a text line including the
<CRLF> is 1000 characters."
```

## Code

```php
  function testVeryLongLineWrap() {
    $input = 'Drupal<br /><p>' . str_repeat('x', 2100) . '</p><br />Drupal';
    $output = drupal_html_to_text($input);
    // This awkward construct comes from includes/mail.inc lines 8-13.
    $eol = variable_get('mail_line_endings', MAIL_LINE_ENDINGS);
    // We must use strlen() rather than drupal_strlen() in order to count
    // octets rather than characters.
    $line_length_limit = 1000 - drupal_strlen($eol);
    $maximum_line_length = 0;
    foreach (explode($eol, $output) as $line) {
      // We must use strlen() rather than drupal_strlen() in order to count
      // octets rather than characters.
      $maximum_line_length = max($maximum_line_length, strlen($line . $eol));
    }
    $verbose = 'Maximum line length found was ' . $maximum_line_length . ' octets.';
    $this->assertTrue($maximum_line_length <= 1000, $verbose);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
