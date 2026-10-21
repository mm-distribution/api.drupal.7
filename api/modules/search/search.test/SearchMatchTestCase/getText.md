# SearchMatchTestCase::getText()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 76–79 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L76-L79)
- **Class:** [SearchMatchTestCase](../SearchMatchTestCase.md)
- **Module/theme:** search

## Signature

```php
function getText($n)
```

## Documentation

```text
_test_: Helper method for generating snippets of content.

Generated items to test against:
  1  ipsum
  2  dolore sit
  3  sit am ut
  4  am ut enim am
  5  ut enim am minim veniam
  6  enim am minim veniam es cillum
  7  am minim veniam es cillum dolore eu
```

## Code

```php
  function getText($n) {
    $words = explode(' ', "Ipsum dolore sit am. Ut enim am minim veniam. Es cillum dolore eu.");
    return implode(' ', array_slice($words, $n - 1, $n));
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
