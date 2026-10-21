# TextSummaryTestCase::testLength()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 287–392 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L287-L392)
- **Class:** [TextSummaryTestCase](../TextSummaryTestCase.md)
- **Module/theme:** text

## Signature

```php
function testLength()
```

## Documentation

```text
Test various summary length edge cases.
```

## Code

```php
  function testLength() {
    // This string tests a number of edge cases.
    $text = "<p>\nHi\n</p>\n<p>\nfolks\n<br />\n!\n</p>";

    // The summaries we expect text_summary() to return when $size is the index
    // of each array item.
    // Using no text format:
    $expected = array(
      "<p>\nHi\n</p>\n<p>\nfolks\n<br />\n!\n</p>",
      "<",
      "<p",
      "<p>",
      "<p>\n",
      "<p>\nH",
      "<p>\nHi",
      "<p>\nHi\n",
      "<p>\nHi\n<",
      "<p>\nHi\n</",
      "<p>\nHi\n</p",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>\n<p>\nfolks\n<br />\n!\n</p>",
      "<p>\nHi\n</p>\n<p>\nfolks\n<br />\n!\n</p>",
      "<p>\nHi\n</p>\n<p>\nfolks\n<br />\n!\n</p>",
    );

    // And using a text format WITH the line-break and htmlcorrector filters.
    $expected_lb = array(
      "<p>\nHi\n</p>\n<p>\nfolks\n<br />\n!\n</p>",
      "",
      "<p></p>",
      "<p></p>",
      "<p></p>",
      "<p></p>",
      "<p></p>",
      "<p>\nHi</p>",
      "<p>\nHi</p>",
      "<p>\nHi</p>",
      "<p>\nHi</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>",
      "<p>\nHi\n</p>\n<p>\nfolks\n<br />\n!\n</p>",
      "<p>\nHi\n</p>\n<p>\nfolks\n<br />\n!\n</p>",
      "<p>\nHi\n</p>\n<p>\nfolks\n<br />\n!\n</p>",
    );

    // Test text_summary() for different sizes.
    for ($i = 0; $i <= 37; $i++) {
      $this->callTextSummary($text, $expected[$i],    NULL, $i);

      // libxml2 library changed parsing behavior on version 2.9.14. Skip
      // specific edge-case testing for all further versions.
      // @see https://gitlab.gnome.org/GNOME/libxml2/-/issues/474
      // @see https://www.drupal.org/project/drupal/issues/3397882
      if ($i == 1 && defined('LIBXML_VERSION') && LIBXML_VERSION >= 20914) {
        continue;
      }

      $this->callTextSummary($text, $expected_lb[$i], 'plain_text', $i);
      $this->callTextSummary($text, $expected_lb[$i], 'filtered_html', $i);
    }
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._
