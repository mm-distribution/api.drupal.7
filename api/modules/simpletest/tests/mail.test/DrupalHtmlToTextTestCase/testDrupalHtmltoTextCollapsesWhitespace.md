# DrupalHtmlToTextTestCase::testDrupalHtmltoTextCollapsesWhitespace()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 373–383 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L373-L383)
- **Class:** [DrupalHtmlToTextTestCase](../DrupalHtmlToTextTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalHtmltoTextCollapsesWhitespace()
```

## Documentation

```text
Test that whitespace is collapsed.
```

## Code

```php
  function testDrupalHtmltoTextCollapsesWhitespace() {
    $input = "<p>Drupal  Drupal\n\nDrupal<pre>Drupal  Drupal\n\nDrupal</pre>Drupal  Drupal\n\nDrupal</p>";
    // @todo The whitespace should be collapsed.
    $collapsed = "Drupal  Drupal\n\nDrupalDrupal  Drupal\n\nDrupalDrupal  Drupal\n\nDrupal\n\n";
    $this->assertHtmlToText(
      $input,
      $collapsed,
      'Whitespace is collapsed',
      array('p')
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
