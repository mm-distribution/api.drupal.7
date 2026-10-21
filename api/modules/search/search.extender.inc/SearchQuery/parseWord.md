# SearchQuery::parseWord()

- **Type:** Method
- **File:** [`modules/search/search.extender.inc`](../_file.md), lines 325–342 · [local source](../../../../../source/modules/search/search.extender.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc#L325-L342)
- **Class:** [SearchQuery](../SearchQuery.md)
- **Module/theme:** search

## Signature

```php
protected function parseWord($word)
```

## Documentation

```text
Helper function for parseQuery().
```

## Code

```php
  protected function parseWord($word) {
    $num_new_scores = 0;
    $num_valid_words = 0;
    // Determine the scorewords of this word/phrase.
    $split = explode(' ', $word);
    foreach ($split as $s) {
      $num = is_numeric($s);
      if ($num || drupal_strlen($s) >= variable_get('minimum_word_size', 3)) {
        if (!isset($this->words[$s])) {
          $this->words[$s] = $s;
          $num_new_scores++;
        }
        $num_valid_words++;
      }
    }
    // Return matching snippet and number of added words.
    return array($num_new_scores, $num_valid_words);
  }
```

---
_Drupal 7.103 · [modules/search/search.extender.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
