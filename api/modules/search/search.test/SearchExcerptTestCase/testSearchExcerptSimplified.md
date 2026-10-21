# SearchExcerptTestCase::testSearchExcerptSimplified()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1674–1714 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1674-L1714)
- **Class:** [SearchExcerptTestCase](../SearchExcerptTestCase.md)
- **Module/theme:** search

## Signature

```php
function testSearchExcerptSimplified()
```

## Documentation

```text
Tests search_excerpt() with search keywords matching simplified words.

Excerpting should handle keywords that are matched only after going through
search_simplify(). This test passes keywords that match simplified words
and compares them with strings that contain the original unsimplified word.
```

## Code

```php
  function testSearchExcerptSimplified() {
    $lorem1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam vitae arcu at leo cursus laoreet. Curabitur dui tortor, adipiscing malesuada tempor in, bibendum ac diam. Cras non tellus a libero pellentesque condimentum. What is a Drupalism? Suspendisse ac lacus libero. Ut non est vel nisl faucibus interdum nec sed leo. Pellentesque sem risus, vulputate eu semper eget, auctor in libero.';
    $lorem2 = 'Ut fermentum est vitae metus convallis scelerisque. Phasellus pellentesque rhoncus tellus, eu dignissim purus posuere id. Quisque eu fringilla ligula. Morbi ullamcorper, lorem et mattis egestas, tortor neque pretium velit, eget eleifend odio turpis eu purus. Donec vitae metus quis leo pretium tincidunt a pulvinar sem. Morbi adipiscing laoreet mauris vel placerat. Nullam elementum, nisl sit amet scelerisque malesuada, dolor nunc hendrerit quam, eu ultrices erat est in orci.';

    // Make some text with some keywords that will get simplified.
    $text = $lorem1 . ' Number: 123456.7890 Hyphenated: one-two abc,def ' . $lorem2;
    // Note: The search_excerpt() function adds some extra spaces -- not
    // important for HTML formatting. Remove these for comparison.
    $result = preg_replace('| +|', ' ', search_excerpt('123456.7890', $text));
    $this->assertTrue(strpos($result, 'Number: <strong>123456.7890</strong>') !== FALSE, 'Numeric keyword is highlighted with exact match');

    $result = preg_replace('| +|', ' ', search_excerpt('1234567890', $text));
    $this->assertTrue(strpos($result, 'Number: <strong>123456.7890</strong>') !== FALSE, 'Numeric keyword is highlighted with simplified match');

    $result = preg_replace('| +|', ' ', search_excerpt('Number 1234567890', $text));
    $this->assertTrue(strpos($result, '<strong>Number</strong>: <strong>123456.7890</strong>') !== FALSE, 'Punctuated and numeric keyword is highlighted with simplified match');

    $result = preg_replace('| +|', ' ', search_excerpt('"Number 1234567890"', $text));
    $this->assertTrue(strpos($result, '<strong>Number: 123456.7890</strong>') !== FALSE, 'Phrase with punctuated and numeric keyword is highlighted with simplified match');

    $result = preg_replace('| +|', ' ', search_excerpt('"Hyphenated onetwo"', $text));
    $this->assertTrue(strpos($result, '<strong>Hyphenated: one-two</strong>') !== FALSE, 'Phrase with punctuated and hyphenated keyword is highlighted with simplified match');

    $result = preg_replace('| +|', ' ', search_excerpt('"abc def"', $text));
    $this->assertTrue(strpos($result, '<strong>abc,def</strong>') !== FALSE, 'Phrase with keyword simplified into two separate words is highlighted with simplified match');

    // Test phrases with characters which are being truncated.
    $result = preg_replace('| +|', ' ', search_excerpt('"ipsum _"', $text));
    $this->assertTrue(strpos($result, '<strong>ipsum </strong>') !== FALSE, 'Only valid part of the phrase is highlighted and invalid part containing "_" is ignored.');

    $result = preg_replace('| +|', ' ', search_excerpt('"ipsum 0000"', $text));
    $this->assertTrue(strpos($result, '<strong>ipsum </strong>') !== FALSE, 'Only valid part of the phrase is highlighted and invalid part "0000" is ignored.');

    // Test combination of the valid keyword and keyword containing only
    // characters which are being truncated during simplification.
    $result = preg_replace('| +|', ' ', search_excerpt('ipsum _', $text));
    $this->assertTrue(strpos($result, '<strong>ipsum</strong>') !== FALSE, 'Only valid keyword is highlighted and invalid keyword "_" is ignored.');

    $result = preg_replace('| +|', ' ', search_excerpt('ipsum 0000', $text));
    $this->assertTrue(strpos($result, '<strong>ipsum</strong>') !== FALSE, 'Only valid keyword is highlighted and invalid keyword "0000" is ignored.');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
