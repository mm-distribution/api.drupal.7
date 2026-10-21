# DrupalHtmlToTextTestCase::testDrupalHtmltoTextUsenetSignature()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 360–368 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L360-L368)
- **Class:** [DrupalHtmlToTextTestCase](../DrupalHtmlToTextTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalHtmltoTextUsenetSignature()
```

## Documentation

```text
Tests drupal_wrap_mail() retains whitespace from Usenet style signatures.

RFC 3676 says, "This is a special case; an (optionally quoted or quoted and
stuffed) line consisting of DASH DASH SP is neither fixed nor flowed."
```

## Code

```php
  function testDrupalHtmltoTextUsenetSignature() {
    $text = "Hi there!\n-- \nHerp Derp";
    $mail_lines = explode("\n", drupal_wrap_mail($text));
    $this->assertEqual("-- ", $mail_lines[1], 'Trailing whitespace not removed for dash-dash-space signatures.');

    $text = "Hi there!\n--  \nHerp Derp";
    $mail_lines = explode("\n", drupal_wrap_mail($text));
    $this->assertEqual("--", $mail_lines[1], 'Trailing whitespace removed for incorrect dash-dash-space signatures.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
