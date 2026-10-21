# TextSummaryTestCase::callTextSummary()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 405–408 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L405-L408)
- **Class:** [TextSummaryTestCase](../TextSummaryTestCase.md)
- **Module/theme:** text

## Signature

```php
function callTextSummary($text, $expected, $format = NULL, $size = NULL)
```

## Documentation

```text
Calls text_summary() and asserts that the expected teaser is returned.
```

## Code

```php
  function callTextSummary($text, $expected, $format = NULL, $size = NULL) {
    $summary = text_summary($text, $format, $size);
    $this->assertIdentical($summary, $expected, format_string('Generated summary "@summary" matches expected "@expected".', array('@summary' => $summary, '@expected' => $expected)));
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._
