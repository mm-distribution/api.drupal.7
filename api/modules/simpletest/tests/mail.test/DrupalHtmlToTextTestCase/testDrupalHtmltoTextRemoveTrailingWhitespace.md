# DrupalHtmlToTextTestCase::testDrupalHtmltoTextRemoveTrailingWhitespace()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 348–352 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L348-L352)
- **Class:** [DrupalHtmlToTextTestCase](../DrupalHtmlToTextTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalHtmltoTextRemoveTrailingWhitespace()
```

## Documentation

```text
Tests that drupal_wrap_mail() removes trailing whitespace before newlines.
```

## Code

```php
  function testDrupalHtmltoTextRemoveTrailingWhitespace() {
    $text = "Hi there! \nHerp Derp";
    $mail_lines = explode("\n", drupal_wrap_mail($text));
    $this->assertNotEqual(" ", substr($mail_lines[0], -1), 'Trailing whitespace removed.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
