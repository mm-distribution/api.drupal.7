# DrupalHtmlToTextTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/mail.test`](_file.md), lines 163–535 · [local source](../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L163-L535)
- **Module/theme:** batch_test

## Signature

```php
class DrupalHtmlToTextTestCase extends DrupalWebTestCase
```

## Documentation

```text
Unit tests for drupal_html_to_text().
```

## Methods (derived index)

- [getInfo()](DrupalHtmlToTextTestCase/getInfo.md)
- [stringToHtml()](DrupalHtmlToTextTestCase/stringToHtml.md) — Converts a string to its PHP source equivalent for display in test messages.
- [assertHtmlToText()](DrupalHtmlToTextTestCase/assertHtmlToText.md) — Helper function for testing drupal_html_to_text().
- [testTags()](DrupalHtmlToTextTestCase/testTags.md) — Test all supported tags of drupal_html_to_text().
- [testDrupalHtmlToTextArgs()](DrupalHtmlToTextTestCase/testDrupalHtmlToTextArgs.md) — Test $allowed_tags argument of drupal_html_to_text().
- [testDrupalHtmltoTextRemoveTrailingWhitespace()](DrupalHtmlToTextTestCase/testDrupalHtmltoTextRemoveTrailingWhitespace.md) — Tests that drupal_wrap_mail() removes trailing whitespace before newlines.
- [testDrupalHtmltoTextUsenetSignature()](DrupalHtmlToTextTestCase/testDrupalHtmltoTextUsenetSignature.md) — Tests drupal_wrap_mail() retains whitespace from Usenet style signatures.
- [testDrupalHtmltoTextCollapsesWhitespace()](DrupalHtmlToTextTestCase/testDrupalHtmltoTextCollapsesWhitespace.md) — Test that whitespace is collapsed.
- [testDrupalHtmlToTextBlockTagToNewline()](DrupalHtmlToTextTestCase/testDrupalHtmlToTextBlockTagToNewline.md) — Test that text separated by block-level tags in HTML get separated by (at least) a newline in the plaintext version.
- [testHeaderSeparation()](DrupalHtmlToTextTestCase/testHeaderSeparation.md) — Test that headers are properly separated from surrounding text.
- [testFootnoteReferences()](DrupalHtmlToTextTestCase/testFootnoteReferences.md) — Test that footnote references are properly generated.
- [testDrupalHtmlToTextParagraphs()](DrupalHtmlToTextTestCase/testDrupalHtmlToTextParagraphs.md) — Test that combinations of paragraph breaks, line breaks, linefeeds, and spaces are properly handled.
- [testVeryLongLineWrap()](DrupalHtmlToTextTestCase/testVeryLongLineWrap.md) — Tests that drupal_html_to_text() wraps before 1000 characters.

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
