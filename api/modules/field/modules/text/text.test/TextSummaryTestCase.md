# TextSummaryTestCase

- **Type:** Class
- **File:** [`modules/field/modules/text/text.test`](_file.md), lines 242–427 · [local source](../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L242-L427)
- **Module/theme:** text

## Signature

```php
class TextSummaryTestCase extends DrupalWebTestCase
```

## Documentation

_No docblock in source._

## Properties

### $article_creator

```php
protected $article_creator;
```

## Methods (derived index)

- [getInfo()](TextSummaryTestCase/getInfo.md)
- [setUp()](TextSummaryTestCase/setUp.md)
- [testFirstSentenceQuestion()](TextSummaryTestCase/testFirstSentenceQuestion.md) — Tests an edge case where the first sentence is a question and subsequent sentences are not. This edge case is documented at http://drupal.org/node/180425.
- [testLongSentence()](TextSummaryTestCase/testLongSentence.md) — Test summary with long example.
- [testLength()](TextSummaryTestCase/testLength.md) — Test various summary length edge cases.
- [testNullSentence()](TextSummaryTestCase/testNullSentence.md) — Test for the NULL value.
- [callTextSummary()](TextSummaryTestCase/callTextSummary.md) — Calls text_summary() and asserts that the expected teaser is returned.
- [testOnlyTextSummary()](TextSummaryTestCase/testOnlyTextSummary.md) — Test sending only summary.

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._
