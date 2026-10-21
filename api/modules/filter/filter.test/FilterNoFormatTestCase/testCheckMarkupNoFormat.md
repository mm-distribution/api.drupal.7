# FilterNoFormatTestCase::testCheckMarkupNoFormat()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 822–830 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L822-L830)
- **Class:** [FilterNoFormatTestCase](../FilterNoFormatTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testCheckMarkupNoFormat()
```

## Documentation

```text
Tests text without format.

Tests if text with no format is filtered the same way as text in the
fallback format.
```

## Code

```php
  function testCheckMarkupNoFormat() {
    // Create some text. Include some HTML and line breaks, so we get a good
    // test of the filtering that is applied to it.
    $text = "<strong>" . $this->randomName(32) . "</strong>\n\n<div>" . $this->randomName(32) . "</div>";

    // Make sure that when this text is run through check_markup() with no text
    // format, it is filtered as though it is in the fallback format.
    $this->assertEqual(check_markup($text), check_markup($text, filter_fallback_format()), 'Text with no format is filtered the same as text in the fallback format.');
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
