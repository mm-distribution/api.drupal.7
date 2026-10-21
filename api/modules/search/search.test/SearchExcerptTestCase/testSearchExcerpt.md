# SearchExcerptTestCase::testSearchExcerpt()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1639–1665 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1639-L1665)
- **Class:** [SearchExcerptTestCase](../SearchExcerptTestCase.md)
- **Module/theme:** search

## Signature

```php
function testSearchExcerpt()
```

## Documentation

```text
Tests search_excerpt() with several simulated search keywords.

Passes keywords and a sample marked up string, "The quick
brown fox jumps over the lazy dog", and compares it to the
correctly marked up string. The correctly marked up string
contains either highlighted keywords or the original marked
up string if no keywords matched the string.
```

## Code

```php
  function testSearchExcerpt() {
    // Make some text with entities and tags.
    $text = 'The <strong>quick</strong> <a href="#">brown</a> fox &amp; jumps <h2>over</h2> the lazy dog';
    // Note: The search_excerpt() function adds some extra spaces -- not
    // important for HTML formatting. Remove these for comparison.
    $expected = 'The quick brown fox &amp; jumps over the lazy dog';
    $result = preg_replace('| +|', ' ', search_excerpt('nothing', $text));
    $this->assertEqual(preg_replace('| +|', ' ', $result), $expected, 'Entire string is returned when keyword is not found in short string');

    $result = preg_replace('| +|', ' ', search_excerpt('fox', $text));
    $this->assertEqual($result, 'The quick brown <strong>fox</strong> &amp; jumps over the lazy dog ...', 'Found keyword is highlighted');

    $longtext = str_repeat($text . ' ', 10);
    $result = preg_replace('| +|', ' ', search_excerpt('nothing', $longtext));
    $this->assertTrue(strpos($result, $expected) === 0, 'When keyword is not found in long string, return value starts as expected');

    $entities = str_repeat('k&eacute;sz&iacute;t&eacute;se ', 20);
    $result = preg_replace('| +|', ' ', search_excerpt('nothing', $entities));
    $this->assertFalse(strpos($result, '&'), 'Entities are not present in excerpt');
    $this->assertTrue(strpos($result, 'í') > 0, 'Entities are converted in excerpt');

    // The node body that will produce this rendered $text is:
    // 123456789 HTMLTest +123456789+&lsquo;  +&lsquo;  +&lsquo;  +&lsquo;  +12345678  &nbsp;&nbsp;  +&lsquo;  +&lsquo;  +&lsquo;   &lsquo;
    $text = "<div class=\"field field-name-body field-type-text-with-summary field-label-hidden\"><div class=\"field-items\"><div class=\"field-item even\" property=\"content:encoded\"><p>123456789 HTMLTest +123456789+‘  +‘  +‘  +‘  +12345678      +‘  +‘  +‘   ‘</p>\n</div></div></div> ";
    $result = search_excerpt('HTMLTest', $text);
    $this->assertFalse(empty($result),  'Rendered Multi-byte HTML encodings are not corrupted in search excerpts');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
