# DrupalHtmlToTextTestCase::testDrupalHtmlToTextArgs()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 315–343 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L315-L343)
- **Class:** [DrupalHtmlToTextTestCase](../DrupalHtmlToTextTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalHtmlToTextArgs()
```

## Documentation

```text
Test $allowed_tags argument of drupal_html_to_text().
```

## Code

```php
  function testDrupalHtmlToTextArgs() {
    // The second parameter of drupal_html_to_text() overrules the allowed tags.
    $this->assertHtmlToText(
      'Drupal <b>Drupal</b> Drupal',
      "Drupal *Drupal* Drupal\n",
      'Allowed <b> tag found',
      array('b')
    );
    $this->assertHtmlToText(
      'Drupal <h1>Drupal</h1> Drupal',
      "Drupal Drupal Drupal\n",
      'Disallowed <h1> tag not found',
      array('b')
    );

    $this->assertHtmlToText(
      'Drupal <p><em><b>Drupal</b></em><p> Drupal',
      "Drupal Drupal Drupal\n",
      'Disallowed <p>, <em>, and <b> tags not found',
      array('a', 'br', 'h1')
    );

    $this->assertHtmlToText(
      '<html><body>Drupal</body></html>',
      "Drupal\n",
      'Unsupported <html> and <body> tags not found',
      array('html', 'body')
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
