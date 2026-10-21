# SearchMatchTestCase::getText2()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 91–94 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L91-L94)
- **Class:** [SearchMatchTestCase](../SearchMatchTestCase.md)
- **Module/theme:** search

## Signature

```php
function getText2($n)
```

## Documentation

```text
_test2_: Helper method for generating snippets of content.

Generated items to test against:
  8  dear
  9  king philip
  10 philip came over
  11 came over from germany
  12 over from germany swimming
```

## Code

```php
  function getText2($n) {
    $words = explode(' ', "Dear King Philip came over from Germany swimming.");
    return implode(' ', array_slice($words, $n - 1, $n));
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
