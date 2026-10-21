# DrupalHtmlToTextTestCase::testHeaderSeparation()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 439–459 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L439-L459)
- **Class:** [DrupalHtmlToTextTestCase](../DrupalHtmlToTextTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testHeaderSeparation()
```

## Documentation

```text
Test that headers are properly separated from surrounding text.
```

## Code

```php
  function testHeaderSeparation() {
    $html = 'Drupal<h1>Drupal</h1>Drupal';
    // @todo There should be more space above the header than below it.
    $text = "Drupal\n======== DRUPAL ==============================================================\n\nDrupal\n";
    $this->assertHtmlToText($html, $text,
      'Text before and after <h1> tag');
    $html = '<p>Drupal</p><h1>Drupal</h1>Drupal';
    // @todo There should be more space above the header than below it.
    $text = "Drupal\n\n======== DRUPAL ==============================================================\n\nDrupal\n";
    $this->assertHtmlToText($html, $text,
      'Paragraph before and text after <h1> tag');
    $html = 'Drupal<h1>Drupal</h1><p>Drupal</p>';
    // @todo There should be more space above the header than below it.
    $text = "Drupal\n======== DRUPAL ==============================================================\n\nDrupal\n\n";
    $this->assertHtmlToText($html, $text,
      'Text before and paragraph after <h1> tag');
    $html = '<p>Drupal</p><h1>Drupal</h1><p>Drupal</p>';
    $text = "Drupal\n\n======== DRUPAL ==============================================================\n\nDrupal\n\n";
    $this->assertHtmlToText($html, $text,
      'Paragraph before and after <h1> tag');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
