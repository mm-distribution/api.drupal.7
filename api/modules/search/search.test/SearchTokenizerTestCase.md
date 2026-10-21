# SearchTokenizerTestCase

- **Type:** Class
- **File:** [`modules/search/search.test`](_file.md), lines 1720–1866 · [local source](../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1720-L1866)
- **Module/theme:** search

## Signature

```php
class SearchTokenizerTestCase extends DrupalWebTestCase
```

## Documentation

```text
Test the CJK tokenizer.
```

## Methods (derived index)

- [getInfo()](SearchTokenizerTestCase/getInfo.md)
- [setUp()](SearchTokenizerTestCase/setUp.md)
- [testTokenizer()](SearchTokenizerTestCase/testTokenizer.md) — Verifies that strings of CJK characters are tokenized.
- [testNoTokenizer()](SearchTokenizerTestCase/testNoTokenizer.md) — Verifies that strings of non-CJK characters are not tokenized.
- [code2utf()](SearchTokenizerTestCase/code2utf.md) — Like PHP chr() function, but for unicode characters.

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
