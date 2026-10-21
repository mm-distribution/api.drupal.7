# SearchTokenizerTestCase::testNoTokenizer()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1827–1838 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1827-L1838)
- **Class:** [SearchTokenizerTestCase](../SearchTokenizerTestCase.md)
- **Module/theme:** search

## Signature

```php
function testNoTokenizer()
```

## Documentation

```text
Verifies that strings of non-CJK characters are not tokenized.

This is just a sanity check - it verifies that strings of letters are
not tokenized.
```

## Code

```php
  function testNoTokenizer() {
    // Set the minimum word size to 1 (to split all CJK characters) and make
    // sure CJK tokenizing is turned on.
    variable_set('minimum_word_size', 1);
    variable_set('overlap_cjk', TRUE);
    $this->refreshVariables();

    $letters = 'abcdefghijklmnopqrstuvwxyz';
    $out = trim(search_simplify($letters));

    $this->assertEqual($letters, $out, 'Letters are not CJK tokenized');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
