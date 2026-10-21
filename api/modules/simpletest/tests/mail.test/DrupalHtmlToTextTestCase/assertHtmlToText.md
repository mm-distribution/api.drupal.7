# DrupalHtmlToTextTestCase::assertHtmlToText()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 204–218 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L204-L218)
- **Class:** [DrupalHtmlToTextTestCase](../DrupalHtmlToTextTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertHtmlToText($html, $text, $message, $allowed_tags = NULL)
```

## Documentation

```text
Helper function for testing drupal_html_to_text().

@param $html
  The source HTML string to be converted.
@param $text
  The expected result of converting $html to text.
@param $message
  A text message to display in the assertion message.
@param $allowed_tags
  (optional) An array of allowed tags, or NULL to default to the full
  set of tags supported by drupal_html_to_text().
```

## Code

```php
  function assertHtmlToText($html, $text, $message, $allowed_tags = NULL) {
    preg_match_all('/<([a-z0-6]+)/', drupal_strtolower($html), $matches);
    $tested_tags = implode(', ', array_unique($matches[1]));
    $message .= ' (' . $tested_tags . ')';
    $result = drupal_html_to_text($html, $allowed_tags);
    $pass = $this->assertEqual($result, $text, check_plain($message));
    $verbose = 'html = <pre>' . $this->stringToHtml($html)
      . '</pre><br />' . 'result = <pre>' . $this->stringToHtml($result)
      . '</pre><br />' . 'expected = <pre>' . $this->stringToHtml($text)
      . '</pre>';
    $this->verbose($verbose);
    if (!$pass) {
      $this->pass("Previous test verbose info:<br />$verbose");
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
