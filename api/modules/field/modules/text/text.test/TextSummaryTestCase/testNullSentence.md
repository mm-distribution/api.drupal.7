# TextSummaryTestCase::testNullSentence()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 397–400 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L397-L400)
- **Class:** [TextSummaryTestCase](../TextSummaryTestCase.md)
- **Module/theme:** text

## Signature

```php
function testNullSentence()
```

## Documentation

```text
Test for the NULL value.
```

## Code

```php
  function testNullSentence() {
    $summary = text_summary(NULL);
    $this->assertNull($summary, 'text_summary() casts returned null');
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._
