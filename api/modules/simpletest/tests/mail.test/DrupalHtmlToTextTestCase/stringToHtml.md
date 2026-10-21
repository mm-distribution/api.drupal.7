# DrupalHtmlToTextTestCase::stringToHtml()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 182–189 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L182-L189)
- **Class:** [DrupalHtmlToTextTestCase](../DrupalHtmlToTextTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function stringToHtml($text)
```

## Documentation

```text
Converts a string to its PHP source equivalent for display in test messages.

@param $text
  The text string to convert.

@return
  An HTML representation of the text string that, when displayed in a
  browser, represents the PHP source code equivalent of $text.
```

## Code

```php
  function stringToHtml($text) {
    return '"' .
      str_replace(
        array("\n", ' '),
        array('\n', '&nbsp;'),
        check_plain($text)
      ) . '"';
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
