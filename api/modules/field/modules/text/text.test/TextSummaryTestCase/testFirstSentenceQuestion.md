# TextSummaryTestCase::testFirstSentenceQuestion()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 263–267 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L263-L267)
- **Class:** [TextSummaryTestCase](../TextSummaryTestCase.md)
- **Module/theme:** text

## Signature

```php
function testFirstSentenceQuestion()
```

## Documentation

```text
Tests an edge case where the first sentence is a question and
subsequent sentences are not. This edge case is documented at
http://drupal.org/node/180425.
```

## Code

```php
  function testFirstSentenceQuestion() {
    $text = 'A question? A sentence. Another sentence.';
    $expected = 'A question? A sentence.';
    $this->callTextSummary($text, $expected, NULL, 30);
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._
