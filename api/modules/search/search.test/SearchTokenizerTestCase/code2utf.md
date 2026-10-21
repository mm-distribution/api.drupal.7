# SearchTokenizerTestCase::code2utf()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1847–1865 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1847-L1865)
- **Class:** [SearchTokenizerTestCase](../SearchTokenizerTestCase.md)
- **Module/theme:** search

## Signature

```php
function code2utf($num)
```

## Documentation

```text
Like PHP chr() function, but for unicode characters.

chr() only works for ASCII characters up to character 255. This function
converts a number to the corresponding unicode character. Adapted from
functions supplied in comments on several functions on php.net.
```

## Code

```php
  function code2utf($num) {
    if ($num < 128) {
      return chr($num);
    }

    if ($num < 2048) {
      return chr(($num >> 6) + 192) . chr(($num & 63) + 128);
    }

    if ($num < 65536) {
      return chr(($num >> 12) + 224) . chr((($num >> 6) & 63) + 128) . chr(($num & 63) + 128);
    }

    if ($num < 2097152) {
      return chr(($num >> 18) + 240) . chr((($num >> 12) & 63) + 128) . chr((($num >> 6) & 63) + 128) . chr(($num & 63) + 128);
    }

    return '';
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
