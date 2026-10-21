# DrupalHtmlToTextTestCase::testDrupalHtmlToTextParagraphs()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 489–504 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L489-L504)
- **Class:** [DrupalHtmlToTextTestCase](../DrupalHtmlToTextTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalHtmlToTextParagraphs()
```

## Documentation

```text
Test that combinations of paragraph breaks, line breaks, linefeeds,
and spaces are properly handled.
```

## Code

```php
  function testDrupalHtmlToTextParagraphs() {
    $tests = array();
    $tests[] = array(
        'html' => "<p>line 1<br />\nline 2<br />line 3\n<br />line 4</p><p>paragraph</p>",
        // @todo Trailing line breaks should be trimmed.
        'text' => "line 1\nline 2\nline 3\nline 4\n\nparagraph\n\n",
    );
    $tests[] = array(
      'html' => "<p>line 1<br /> line 2</p> <p>line 4<br /> line 5</p> <p>0</p>",
      // @todo Trailing line breaks should be trimmed.
      'text' => "line 1\nline 2\n\nline 4\nline 5\n\n0\n\n",
    );
    foreach ($tests as $test) {
      $this->assertHtmlToText($test['html'], $test['text'], 'Paragraph breaks');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
